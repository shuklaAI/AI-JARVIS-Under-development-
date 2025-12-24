# JARVIS - Just A Rather Very Intelligent System

A powerful AI assistant that can control your computer, execute commands, and engage in intelligent conversations.

## Features

- 🎯 **System Control**: Open apps, websites, lock system, shutdown, restart
- 🤖 **AI-Powered**: Uses LLaMA 3 via OpenRouter for intelligent command understanding
- 🗣️ **Voice Output**: Text-to-speech using Edge TTS
- 🛡️ **Safety**: Emergency kill switch (CTRL+SHIFT+K)
- 🌐 **API Server**: REST API for remote control
- 📝 **Comprehensive Logging**: Full activity logs

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/shuklaAI/AI-JARVIS-Under-development-.git
cd AI-JARVIS-Under-development-
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file:
```
OPENROUTER_API_KEY=your_api_key_here
```

Get your API key from: https://openrouter.ai/

## Usage

### Interactive Terminal Mode
```bash
python main.py
```

### With Voice Output
```bash
python main.py --voice
```

### API Server Mode
```bash
python main.py --server --port 8000
```

## Commands

### System Commands
- `open chrome` - Open Chrome browser
- `open notepad` - Open Notepad
- `open google.com` - Open website
- `what time is it` - Get current time
- `what's the date` - Get current date
- `lock system` - Lock computer
- `shutdown` - Shutdown computer (10 sec delay)
- `restart` - Restart computer (10 sec delay)

### Conversational
- `hello` - Greet JARVIS
- `how are you` - Have a conversation
- `who are you` - Ask about JARVIS

## Project Structure

```
scrapper/core/
├── actions.py        # System action functions
├── registry.py       # Action registry
├── executor.py       # Action execution logic
├── planner.py        # Command planning (NLP → Actions)
├── llm_openrouter.py # LLM interface
├── chat.py           # Interactive chat loop
├── voice.py          # Text-to-speech
├── logger.py         # Logging system
├── safety.py         # Kill switch
├── server.py         # FastAPI server
└── main.py           # Entry point
```

## API Endpoints

- `GET /` - API info
- `GET /health` - Health check
- `GET /actions` - List available actions
- `POST /command` - Execute command
  ```json
  {
    "command": "open chrome",
    "use_voice": false
  }
  ```

## Safety Features

### Emergency Kill Switch
Press **CTRL + SHIFT + K** to immediately stop JARVIS.

### Logging
All activities are logged to `logs/jarvis_TIMESTAMP.log`

## Configuration

### Change Voice
Edit `voice.py`:
```python
VOICE = "en-IN-NeerjaNeural"  # Indian English Female
# Other options:
# "en-US-JennyNeural"  # US English Female
# "en-GB-RyanNeural"   # British English Male
```

### Add Custom Actions
1. Add function to `actions.py`
2. Register in `registry.py`
3. Update planner rules in `planner.py`

## Troubleshooting

### "OPENROUTER_API_KEY not set"
Set your API key in `.env` file.

### Chrome won't open
Update the Chrome path in `actions.py` for your system.

### Voice not working
Install pygame: `pip install pygame`

### Kill switch not working
Run as administrator (keyboard library needs elevated privileges).

## License

MIT License - Feel free to use and modify!

## Credits

Created by Abhinav Shukla
- Uses OpenRouter API for LLM
- Edge TTS for voice synthesis
- FastAPI for API server
