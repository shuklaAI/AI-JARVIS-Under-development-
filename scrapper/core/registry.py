import os
import webbrowser
import subprocess
import datetime

def open_app(app_name: str):
    apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": "notepad",
        "cmd": "cmd",
        "explorer": "explorer"
    }

    if app_name not in apps:
        return f"Unknown app: {app_name}"

    subprocess.Popen(apps[app_name])
    return f"{app_name} opened."


def open_website(url: str):
    webbrowser.open(url)
    return f"Opened {url}"


def system_time():
    return datetime.datetime.now().strftime("%H:%M")


def lock_system():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "System locked."
