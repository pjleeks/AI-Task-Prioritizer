# app.py
import streamlit as st
from prioritizer import prioritize_tasks  # We'll create this logic separately

# ===============================
# AI Task Prioritizer - Streamlit UI
# ===============================

st.set_page_config(
    page_title="AI Task Prioritizer",
    page_icon="🧠",
    layout="wide"
)

st.title("AI Task Prioritizer")
st.subheader("From chaos to clarity: AI ranks your tasks and explains why.")

# --- Sidebar Options ---
st.sidebar.header("Settings")
model_option = st.sidebar.selectbox("Select model:", ["LLM (GPT)", "Local fallback"])
show_matrix = st.sidebar.checkbox("Show Eisenhower Matrix", value=False)
export_csv = st.sidebar.checkbox("Enable CSV export", value=True)

# --- Task Input ---
st.header("Enter your tasks")
task_input = st.text_area(
    "Paste tasks here (one per line, or as a JSON array)",
    placeholder="- Finish quarterly report\n- Buy groceries\n- Prepare slides for Monday meeting"
)

# --- Process Button ---
if st.button("Prioritize Tasks"):
    if not task_input.strip():
        st.warning("Please enter at least one task.")
    else:
        # Convert input into list
        if task_input.strip().startswith("["):
            import json
            try:
                tasks = json.loads(task_input)
            except json.JSONDecodeError:
                st.error("Invalid JSON format. Please fix it.")
                tasks = []
        else:
            tasks = [line.strip() for line in task_input.split("\n") if line.strip()]

        if tasks:
            # Call prioritizer logic
            prioritized_tasks = prioritize_tasks(tasks, model=model_option)

            # --- Display Results ---
            st.header("Prioritized Tasks")
            for t in prioritized_tasks:
                st.markdown(f"**{t['task']}** — Score: {t['score']} — Priority: {t['priority']}")
                st.caption(t['reasoning'])

            # Optional: Eisenhower Matrix
            if show_matrix:
                st.subheader("Eisenhower Matrix (Simplified)")
                # Placeholder for matrix visualization
                st.info("Matrix view coming soon...")

            # Optional: Export
            if export_csv:
                import pandas as pd
                df = pd.DataFrame(prioritized_tasks)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="prioritized_tasks.csv",
                    mime="text/csv"
                )

st.sidebar.markdown("---")
st.sidebar.markdown("📌 Built with Streamlit & LLM logic")
