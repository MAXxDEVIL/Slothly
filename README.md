# 🦥 Slothly

**Slothly** is a fully local, overnight AI agent that does a dreaded task for you — so you don't have to.

Drop a voice note or a written note into the `inbox/` folder before bed. Overnight, Slothly transcribes (if audio) and summarizes it into a crisp **two-line morning report**, writes it to `reports/YYYY-MM-DD.md`, and archives the source.

Built during **"Slow and Steady"** week — in honor of International Sloth Day, Oct 20.

## The open-source stack (the open pieces that make it work)

- **Agent harness:** [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) (open source)
- **LLM inference:** [Ollama](https://ollama.com) + open-weight model `llama3.2`
- **Transcription:** [faster-whisper](https://github.com/m-bain/faster-whisper) (open source)
- **Runtime:** fully local, CPU

## How it works

1. User drops notes / voice memos into `inbox/`
2. Nightly scheduled run processes new files
3. Transcribe (audio) → summarize (llama3.2) → two-line report → archive

## Quick start

```bash
# 1. Install Ollama and pull the model
ollama pull llama3.2

# 2. Create venv and install deps
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install openai faster-whisper openai-agents

# 3. Drop a note / voice memo into inbox/

# 4. Run the nightly flow (or wait for the SlothlyNightly task at 23:00)
python nightly.py
```

## Why open beats closed

- **Runs on a laptop with no internet** — local inference via Ollama + faster-whisper; no cloud APIs needed
- **Keeps user data off servers they don't control** — everything runs on-device
- **Fine-tune / swap models / change behavior** — open-weight model means the agent is swappable
- **Cost nothing to run** — local inference, zero API spend

## Status

- ✅ Environment & foundation
- ✅ Text summarization core
- ✅ Agent layer
- ✅ Scheduling & delivery
- 🚧 Hackathon week in progress
