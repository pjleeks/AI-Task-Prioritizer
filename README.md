---

# **AI Task Prioritizer**

An intelligent task-ranking tool that analyzes urgency, impact, effort, and dependencies using LLM-powered reasoning. Paste in your tasks and get a ranked, structured, and explainable priority list — perfect for productivity systems, project planning, and workflow automation.

---

## 🚀 **Features**

* **LLM-Powered Prioritization**
  Assigns a 0–100 priority score for each task.

* **Multi-Factor Evaluation**
  Based on:

  * Urgency
  * Impact
  * Effort
  * Dependencies
  * Time sensitivity

* **Explainable Results**
  Each score comes with a rationale so users understand *why* it ranked there.

* **Flexible Input Formats**
  Accepts:

  * Bullet lists
  * Paragraphs
  * JSON arrays

* **Optional Extensions**
  (Modular — can be added at any time)

  * Eisenhower Matrix view
  * “Do / Delegate / Automate / Delete” grouping
  * Export results to CSV or JSON
  * Offline fallback logic (deterministic scoring if no LLM)

---

## 🧠 **How It Works**

1. User enters a list of tasks.
2. Tasks are sent to the prioritization engine.
3. The LLM evaluates each task using an internal scoring rubric.
4. Results are normalized, sorted, and displayed with explanations.
5. Optional matrix and export tools enhance workflow usability.

---

## 📂 **Project Structure**

```
ai-task-prioritizer/
│
├── app.py                # Streamlit UI (Option B)
├── prioritizer.py        # LLM + fallback scoring engine
├── requirements.txt
├── README.md
│
├── examples/
│   ├── sample_tasks.txt
│   └── sample_output.json
│
└── assets/
    └── screenshots/      # Optional UI images
```

---

## 🧩 **Example Input**

```
- Finish the quarterly report
- Buy groceries
- Prepare slides for Monday meeting
- Respond to client emails
- Clean the garage
```

---

## 🧾 **Example Output (Simplified)**

| Task                              | Score | Priority | Reasoning                                              |
| --------------------------------- | ----- | -------- | ------------------------------------------------------ |
| Prepare slides for Monday meeting | 92    | High     | Time-sensitive, high visibility, impacts team workflow |
| Finish the quarterly report       | 88    | High     | Deadline-driven, high business value                   |
| Respond to client emails          | 72    | Medium   | Important, but not as time-critical                    |
| Buy groceries                     | 34    | Low      | Personal, low urgency                                  |
| Clean the garage                  | 15    | Low      | No deadline, low impact                                |

---

## 🛠️ **Tech Stack**

* **Streamlit** — front-end UI
* **Python**
* **OpenAI API** (or any LLM backend)
* Optional: local fallback scoring

---

## 🔮 **Roadmap**

* [ ] Add model selection (GPT, local models, etc.)
* [ ] Add Eisenhower Matrix
* [ ] Add CSV + JSON export
* [ ] Add web API endpoint
* [ ] Add Chrome extension version
* [ ] Add collaborative task mode

---

## 📜 **License**

MIT License. Free for personal and commercial use.

---
