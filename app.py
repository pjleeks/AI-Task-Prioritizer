# app.py
import streamlit as st
from prioritizer import prioritize_tasks, eisenhower_matrix
import pandas as pd
import json
from io import StringIO

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
show_matrix = st.sidebar.checkbox("Show Eisenhower Matrix", value=True)

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
        # Parse tasks
        if task_input.strip().startswith("["):
            try:
                tasks = json.loads(task_input)
            except json.JSONDecodeError:
                st.error("Invalid JSON format. Please fix it.")
                tasks = []
        else:
            tasks = [line.strip() for line in task_input.split("\n") if line.strip()]

        if tasks:
            # Run prioritizer logic
            results = prioritize_tasks(tasks, model=model_option)

            # Generate Eisenhower matrix
            matrix = eisenhower_matrix(results)

            # Assign quadrant info to each task for export
            for task in results:
                for quadrant, items in matrix.items():
                    if task in items:
                        task['quadrant'] = quadrant
                        break
                else:
                    task['quadrant'] = "unknown"

            # ---------------------------------------
            # Display Prioritized Task List
            # ---------------------------------------
            st.subheader("📊 Prioritized Task List")
            for idx, item in enumerate(results, start=1):
                st.markdown(f"### {idx}. **{item['task']}**")
                st.write(f"**Score:** {item['score']}")
                st.write(f"**Urgency:** {item.get('urgency', 'N/A')}")
                st.write(f"**Importance:** {item.get('importance', 'N/A')}")
                if "rationale" in item:
                    with st.expander("Rationale"):
                        st.write(item["rationale"])
                st.markdown("---")

            # ---------------------------------------
            # Export Buttons (CSV + JSON)
            # ---------------------------------------
            df = pd.DataFrame(results)

            # CSV Export
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv_buffer.getvalue(),
                file_name="prioritized_tasks.csv",
                mime="text/csv"
            )

            # JSON Export
            json_buffer = json.dumps(results, indent=2)
            st.download_button(
                label="📥 Download JSON",
                data=json_buffer,
                file_name="prioritized_tasks.json",
                mime="application/json"
            )

            # ---------------------------------------
            # Display Eisenhower Matrix
            # ---------------------------------------
            if show_matrix:
                st.subheader("🧭 Eisenhower Matrix")
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### ✅ Do Now (Important + Urgent)")
                    for item in matrix["do_now"]:
                        st.write(f"- **{item['task']}** (Score: {item['score']})")

                    st.markdown("### 🤝 Delegate (Not Important + Urgent)")
                    for item in matrix["delegate"]:
                        st.write(f"- **{item['task']}** (Score: {item['score']})")

                with col2:
                    st.markdown("### 📅 Schedule (Important + Not Urgent)")
                    for item in matrix["schedule"]:
                        st.write(f"- **{item['task']}** (Score: {item['score']})")

                    st.markdown("### 🗑️ Delete / Minimize (Not Important + Not Urgent)")
                    for item in matrix["delete"]:
                        st.write(f"- **{item['task']}** (Score: {item['score']})")# Paste the full final app.py code here (from the previous step)
