import json
from core.llm_openrouter import ask_llm

PLANNER_PROMPT = """
You are a command-to-JSON translator.

RULES:
- Output ONLY valid JSON
- No text outside JSON
- No explanations

Allowed actions:
- open_app(app_name)
- open_website(url)
- system_time()
- lock_system()

Examples:

User: what time is it
Output:
{"action":"system_time","params":{}}

User: open chrome
Output:
{"action":"open_app","params":{"app_name":"chrome"}}

User: open google.com
Output:
{"action":"open_website","params":{"url":"google.com"}}
"""

def plan(user_input: str) -> dict:
    text = user_input.lower().strip()

    # 🔥 RULE-BASED FIRST (FAST & SAFE)
    if "time" in text:
        return {"action": "system_time", "params": {}}

    if text.startswith("open "):
        target = text.replace("open ", "").strip()
        if "." in target:
            return {"action": "open_website", "params": {"url": target}}
        else:
            return {"action": "open_app", "params": {"app_name": target}}

    if "lock" in text:
        return {"action": "lock_system", "params": {}}

    # 🤖 LLM FALLBACK (STRICT JSON)
    raw = ask_llm(PLANNER_PROMPT, user_input).strip()

    try:
        parsed = json.loads(raw)
        if "action" not in parsed:
            raise ValueError
        return parsed
    except Exception:
        return {"action": "unknown", "params": {}}
