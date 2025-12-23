from core.planner import plan
from core.executor import execute

def main():
    print("JARVIS READY (WORK MODE)")
    while True:
        user_input = input("> ").strip()
        if user_input in ["exit", "quit"]:
            break

        action_plan = plan(user_input)
        result = execute(action_plan)
        print(result)

if __name__ == "__main__":
    main()
