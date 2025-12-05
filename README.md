# 🧠 AI Task Prioritizer

**From chaos to clarity** — AI ranks your tasks by urgency, importance, dependencies, and effort, helping you focus on what really matters.

---

## Features

- Paste tasks in plain text or JSON format
- AI-driven **prioritization** with scores and reasoning
- **Eisenhower Matrix** visualization:
  - ✅ Do Now (Important + Urgent)
  - 📅 Schedule (Important + Not Urgent)
  - 🤝 Delegate (Not Important + Urgent)
  - 🗑️ Delete / Minimize (Not Important + Not Urgent)
- **Export** prioritized tasks to CSV or JSON, including quadrant info
- Sidebar options:
  - Select model (LLM or local fallback)
  - Show/hide Eisenhower matrix

---

## Installation

1. Clone this repo:

```bash
git clone https://github.com/yourusername/AI_Task_Prioritizer.git
cd AI_Task_Prioritizer
````

2. (Optional but recommended) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Run the app:

```bash
streamlit run app.py
```

2. Paste your tasks into the text area:

   * One task per line, or
   * JSON array of tasks

3. Click **“Prioritize Tasks”**

4. View the **ranked task list** and **Eisenhower matrix**

5. Download **CSV** or **JSON** with quadrant info

---

## Example

**Input:**

```
Finish quarterly report
Buy groceries
Prepare slides for Monday meeting
Call mom
```

**Output:**

| Task                      | Score | Urgency | Importance | Quadrant |
| ------------------------- | ----- | ------- | ---------- | -------- |
| Finish quarterly report   | 92    | 0.9     | 0.95       | do_now   |
| Prepare slides for Monday | 85    | 0.8     | 0.9        | do_now   |
| Buy groceries             | 60    | 0.6     | 0.6        | schedule |
| Call mom                  | 50    | 0.5     | 0.5        | schedule |

---

## Future Enhancements

* Add confidence scores for prioritization
* Integrate real LLM API (OpenAI) for smarter scoring
* “Do / Delegate / Automate / Delete” actionable suggestions
* Export to Google Sheets or Notion directly

---

## License

MIT License

---
