# app.py
import streamlit as st
from prioritizer import prioritize_tasks
from prioritizer import eisenhower_matrix

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
        # Handle JSON input OR line input
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

            # ---------------------------------------
            # RUN PRIORITIZER LOGIC
            # ---------------------------------------
            results = prioritize_tasks(tasks, model=model_option)

            # ---------------------------------------
            # DISPLAY PRIORITIZED TASK LIST
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
            # DISPLAY EISENHOWER MATRIX
            # ---------------------------------------
            if show_matrix:
                st.subheader("🧭 Eisenhower Matrix")

                matrix = eisenhower_matrix(results)

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### ✅ Do Now (Important + Urgent)")
                    for item in matrix["do_now"]:
                        st.write(f"- **{item['task']}** (Score: {item['score']})")

                with col2:
                    st.markdown("### 📅 Schedule (Important + Not Urgent)")
                    for item in matrix["schedule"]:
                        st.write(f"- **{item['task']}** (Score: {item['score']})")

                # second row
                col3, col4 = st.columns(2)

                with col3:
                    st.markdown("### 🤝 Delegate (Not Important + Urgent)")
                    for item in matrix["delegate"]:
                        st.write(f"- **{item['task']}** (Score: {item['score']})")

                with col4:
                    st.markdown("### 🗑️ Delete / Minimize (Not Important + Not Urgent)")
                    for item in matrix["delete"]:
                        st.write(f"- **{item['score']}** (Score: {item['score']})")
