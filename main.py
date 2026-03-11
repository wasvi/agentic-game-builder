from agents.clarifier import clarify_requirements
from agents.planner import create_plan
from agents.builder import build_game

def run_agent():

    print("Agentic Game Builder AI\n")

    idea = input("Enter game idea:\n")

    print("\n--- Clarification Phase ---\n")

    questions = clarify_requirements(idea)

    print(questions)

    answers = input("\nAnswer the questions:\n")

    print("\n--- Planning Phase ---\n")

    plan = create_plan(idea, answers)

    print(plan)

    print("\n--- Execution Phase ---\n")

    build_game(plan)

if __name__ == "__main__":
    run_agent()