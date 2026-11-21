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
<img width="1374" height="1061" alt="test1" src="https://github.com/user-attachments/assets/ab6ddd7f-86c8-4b23-9994-2438920ea8d2" />
<img width="1220" height="1055" alt="test3" src="https://github.com/user-attachments/assets/dd41775f-b28e-496b-afef-86f44c7c935c" />

