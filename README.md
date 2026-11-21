# PS30 – Lesson Plan Generator for Teachers

**Problem statement:** School teachers need structured lesson plans. This app generates a
40-minute (adjustable) lesson plan with objectives, timed activities and assessment from a
topic and grade, using an LLM (Gemini 2.5 Flash).

## How to run
```bash
pip install -r requirements.txt
cp .env.example .env      # then put your free Gemini key in .env
streamlit run app.py
```
Get a free key at https://aistudio.google.com/apikey

## Features
- Inputs: topic, grade (1–12), duration, optional notes
- Fixed sections: title, objectives, materials, timed activity table, assessment, homework
- Download as .txt or .docx

## Screenshots
(add 1–2 screenshots here)
