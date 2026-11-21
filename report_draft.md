# PS30 – Lesson Plan Generator for Teachers
Name: <your name> | Roll No: 30 | Class: <class> | GitHub: llm-ps30-<RollNo> link: <url>

## Problem statement
School teachers spend a lot of time preparing structured lesson plans. This project generates a
40-minute lesson plan (objectives, timed activities, assessment) from a topic, grade and duration.
It helps school teachers and trainee teachers save preparation time.

## Tools & model
Python 3, Streamlit (UI), google-genai SDK, python-dotenv, python-docx. LLM: Gemini 2.5 Flash via API.

## Procedure
1. Created a free Gemini API key in Google AI Studio and stored it in a .env file.
2. Tested the prompt in the AI Studio playground with 3–5 topics (e.g. Photosynthesis, Fractions).
3. Wrote the prompt template with fixed sections and a rule that activity minutes add up to the duration.
4. Wrote app.py: take topic/grade/duration -> build prompt -> call Gemini -> display Markdown.
5. Built the Streamlit UI (text input, grade dropdown, duration box, notes) and .txt/.docx download buttons.
6. Tested on 5 inputs, took screenshots, added .gitignore and requirements.txt, pushed to GitHub.

## Prompt used
"You are an experienced school teacher and curriculum designer. Create a {duration}-minute lesson plan
for Grade {grade} on the topic {topic}... Use EXACTLY these sections: Lesson Title, Learning Objectives,
Materials, Lesson Activities (table with time, activity, teacher action, student action; minutes must add
up to {duration}), Assessment, Homework. Keep vocabulary suitable for Grade {grade}."
Improvement: <e.g. first version gave activity times that did not sum to 40; I added "minutes must add up to exactly {duration}".>

## Results
<Insert 1–2 screenshots. Sample input: Topic = Photosynthesis, Grade 7, 40 min. Output: full plan with timed table.>

## Challenges
<Fill with your real ones, e.g. API quota/rate limit error -> waited / added try-except; times not adding up -> stricter prompt; key leaking risk -> .env + .gitignore.>

## Conclusion
The app produces usable, well-structured lesson plans quickly. It sometimes needs teacher edits for
local curriculum. Future improvement: align plans to a chosen board syllabus (CBSE/State) using RAG.
