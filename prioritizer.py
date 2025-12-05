# prioritizer.py

import os
import re
import statistics
from openai import OpenAI

# -----------------------------
# 1. LLM Client Setup (Safe)
# -----------------------------
def get_llm_client():
    """Returns an OpenAI client if an API key is set. Otherwise None."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


# -----------------------------
# 2. Priority Label Helper
# -----------------------------
def priority_label(score: int) -> str:
    if score >= 80:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"


# -----------------------------
# 3. LLM Prioritization Logic
# -----------------------------
def llm_score_tasks(tasks):
    """Uses an LLM to assign urgency, impact, effort, dependencies → score."""

    client = get_llm_client()
    if client is None:
        return None  # Fall back to offline scoring

    system_prompt = """
You are an expert productivity analyst. 
Score each task from 0–100 based on:
- Urgency (time sensitivity)
- Impact (business or personal value)
- Effort (lower effort = higher score)
- Dependencies (blocked tasks get lower priority)
- Consequences of delay

Return results ONLY in this JSON format:
[
  {
    "task": "...",
    "score": 0-100,
    "reasoning": "..."
  }
]
"""

    user_prompt = "Here are the tasks:\n" + "\n".join(f"- {t}" for t in tasks)

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",   # Fast + cheap option
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2
        )
        content = response.choices[0].message.content

        import json
        return json.loads(content)

    except Exception as e:
        print("LLM error:", e)
        return None


# -----------------------------
# 4. Offline Fallback Scoring
# -----------------------------
def fallback_score_tasks(tasks):
    """
    Deterministic scoring when no LLM is available.
    Uses keyword heuristics + length penalties.
    Not as smart as LLM, but stable & predictable.
    """

    urgency_words = ["today", "tomorrow", "urgent", "asap", "deadline", "soon"]
    impact_words = ["report", "meeting", "client", "deliverable", "presentation"]

    results = []

    for task in tasks:
        task_lower = task.lower()

        # Base score
        score = 40

        # Urgency boosts
        for w in urgency_words:
            if w in task_lower:
                score += 15

        # Impact boosts
        for w in impact_words:
            if w in task_lower:
                score += 10

        # Length penalty (longer tasks tend to be more complex)
        score -= min(len(task) // 30, 10)

        # Clamp score
        score = max(5, min(95, score))

        results.append({
            "task": task,
            "score": score,
            "reasoning": "Offline heuristic: estimated based on urgency/impact keywords and task length."
        })

    return results


# -----------------------------
# 5. Normalize Scores
# -----------------------------
def normalize_scores(results):
    """Ensures scores are scaled 0–100."""
    scores = [r["score"] for r in results]
    min_s, max_s = min(scores), max(scores)

    if max_s == min_s:
        return results  # all the same

    normalized = []
    for r in results:
        new_score = int(100 * (r["score"] - min_s) / (max_s - min_s))
        normalized.append({
            **r,
            "score": new_score
        })
    return normalized


# -----------------------------
# 6. Main Entry Function
# -----------------------------
def prioritize_tasks(tasks, model="LLM (GPT)"):
    """
    Returns a list of:
    {
        "task": str,
        "score": int,
        "priority": "High/Medium/Low",
        "reasoning": str
    }
    """

    # Try LLM first (if enabled + available)
    results = None
    if "LLM" in model:
        results = llm_score_tasks(tasks)

    # If LLM unavailable or fails → offline scoring
    if results is None:
        results = fallback_score_tasks(tasks)

    # Normalize + sort
    results = normalize_scores(results)
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    # Add priority labels
    for r in results:
        r["priority"] = priority_label(r["score"])

    return results
