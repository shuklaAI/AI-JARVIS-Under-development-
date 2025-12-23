from core.registry import ACTION_REGISTRY

def execute(plan: dict):
    action = plan.get("action")
    params = plan.get("params", {})

    if action not in ACTION_REGISTRY:
        return "Action not supported."

    try:
        return ACTION_REGISTRY[action](**params)
    except Exception as e:
        return f"Execution failed: {e}"
