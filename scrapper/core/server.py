from fastapi import FastAPI
from core.logger import logger
from core.safety import start_kill_switch, KILL_FLAG

app = FastAPI(title="Jarvis Core", version="0.0.1")

@app.on_event("startup")
def startup_event():
    logger.info("🚀 Jarvis Core starting up")
    start_kill_switch()

@app.get("/health")
def health_check():
    if KILL_FLAG:
        return {"status": "KILLED"}
    return {"status": "OK"}

@app.get("/ping")
def ping():
    logger.info("Ping received")
    return {"msg": "Jarvis core alive"}
