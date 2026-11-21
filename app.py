"""PS30 - Lesson Plan Generator for Teachers (Streamlit + Gemini)."""
import io
import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
MODEL = "gemini-3.8-flash"

PROMPT_TEMPLATE = """You are an experienced school teacher and curriculum designer.
Create a {duration}-minute lesson plan for Grade {grade} on the topic: "{topic}".
Teaching style / extra notes: {notes}

Use EXACTLY these sections, in this order, in Markdown:
## 1. Lesson Title
## 2. Learning Objectives
(3 objectives, each starting with an action verb like "explain", "identify", "solve")
## 3. Materials Needed
## 4. Lesson Activities
A table with columns: Time (minutes) | Activity | Teacher Action | Student Action.
The minutes must add up to exactly {duration}. Include: Introduction/Hook, Main Teaching, Guided Practice, Group/Individual Activity, Wrap-up.
## 5. Assessment
(one quick formative check and 3 exit-ticket questions with answers)
## 6. Homework

Keep vocabulary suitable for Grade {grade} students. Be concrete and practical."""


def build_prompt(topic, grade, duration, notes):
    return PROMPT_TEMPLATE.format(
        topic=topic, grade=grade, duration=duration, notes=notes or "None"
    )


def get_client():
    key = os.getenv("GEMINI_API_KEY") or st.session_state.get("key", "")
    if not key:
        return None
    return genai.Client(api_key=key)


def to_docx_bytes(text):
    from docx import Document

    doc = Document()
    for line in text.splitlines():
        if line.startswith("## "):
            doc.add_heading(line[3:], level=2)
        elif line.strip():
            doc.add_paragraph(line)
    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


st.set_page_config(page_title="Lesson Plan Generator", page_icon="📘")
st.title("📘 Lesson Plan Generator for Teachers")
st.caption("Enter a topic, grade and duration to get a structured lesson plan.")

if not os.getenv("GEMINI_API_KEY"):
    st.session_state["key"] = st.sidebar.text_input("Gemini API key", type="password")

topic = st.text_input("Topic", placeholder="e.g. Photosynthesis")
col1, col2 = st.columns(2)
grade = col1.selectbox("Grade", list(range(1, 13)), index=6)
duration = col2.number_input("Duration (minutes)", 20, 120, 40, step=5)
notes = st.text_area("Extra notes (optional)", placeholder="e.g. include a group activity")

if st.button("Generate lesson plan", type="primary"):
    client = get_client()
    if not topic.strip():
        st.warning("Please enter a topic.")
    elif client is None:
        st.error("Add your Gemini API key (.env or sidebar).")
    else:
        with st.spinner("Generating..."):
            try:
                resp = client.models.generate_content(
                    model=MODEL, contents=build_prompt(topic, grade, duration, notes)
                )
                st.session_state["plan"] = resp.text
            except Exception as e:  # API limit, network, bad key
                st.error(f"LLM call failed: {e}")

plan = st.session_state.get("plan")
if plan:
    st.markdown(plan)
    d1, d2 = st.columns(2)
    d1.download_button("Download .txt", plan, "lesson_plan.txt")
    try:
        d2.download_button("Download .docx", to_docx_bytes(plan), "lesson_plan.docx")
    except Exception:
        pass
