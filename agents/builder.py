import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def extract_code(content, lang):

    pattern = rf"```{lang}(.*?)```"
    match = re.search(pattern, content, re.DOTALL)

    if match:
        return match.group(1).strip()

    return ""

def build_game(plan):

    prompt = f"""
You are an expert JavaScript game developer.

Using this plan:

{plan}

Generate a COMPLETE playable browser game.

Requirements:
- Must run locally by opening index.html
- Use HTML + CSS + Vanilla JavaScript
- Use HTML Canvas for rendering
- No external libraries
- Include score system
- Include restart button

Return ONLY these code blocks:

```html
index.html code
style.css code
game.js code
"""

    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role":"user","content":prompt}]
)
    content = response.choices[0].message.content
    

    html = extract_code(content, "html")
    css = extract_code(content, "css")
    js = extract_code(content, "javascript")

    os.makedirs("generated_game", exist_ok=True)

    with open("generated_game/index.html","w",encoding="utf-8") as f:
     f.write(html)

    with open("generated_game/style.css","w",encoding="utf-8") as f:
     f.write(css)

    with open("generated_game/game.js","w",encoding="utf-8") as f:
     f.write(js)

    print("\nGame generated successfully!")
    print("generated_game/index.html")
    print("generated_game/style.css")
    print("generated_game/game.js")

    return "done"

