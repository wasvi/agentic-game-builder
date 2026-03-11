# Agentic Game Builder AI

This project implements an AI agent that generates a playable browser game from a natural language description.

Agent Workflow

1 Clarification Phase
The agent asks follow-up questions to understand requirements.

2 Planning Phase
The agent creates a structured game design plan.

3 Execution Phase
The agent generates HTML/CSS/JS files to create a playable game.

Architecture

main.py
Orchestrates the agent workflow.

clarifier.py
Generates requirement clarification questions.

planner.py
Builds a structured game design.

builder.py
Generates playable game code.

How to Run

Docker Build

docker build -t game-agent .

Docker Run

docker run -it game-agent

Output

Generated files appear in:

generated_game/

Open index.html in a browser to play the game.

Tradeoffs

Used vanilla JS for simplicity.
Limited asset generation.

Future Improvements

Multi-agent architecture
Game asset generation
Automated testing agent

Live game preview


User Input
   ↓
Agent Controller
   ↓
Clarifier Agent
   ↓
Planner Agent
   ↓
Builder Agent
   ↓
Generated Game Files
