import edge_tts
import asyncio

async def speak(text: str):
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-IN-NeerjaNeural"
    )

    async for _ in communicate.stream():
        pass
