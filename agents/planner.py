import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def create_plan(idea, answers):

    prompt = f"""
Create a structured game development plan.

Game Idea:
{idea}

User Answers:
{answers}

Include:
- Game mechanics
- Controls
- Game loop
- Rendering method
- File structure
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
