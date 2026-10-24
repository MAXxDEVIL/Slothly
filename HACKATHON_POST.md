# Slothly — the overnight agent that works while you sleep

**Theme: Slow and Steady** (International Sloth Day, Oct 20)

Most AI agents are built to move fast — a firehose of notifications, always-on cloud calls, per-token billing, data leaving your device. This week, I built the sloth edition.

## What I built

**Slothly** is a fully local, overnight AI agent.

- You drop a voice note or written note into `inbox/`
- Overnight, Slothly transcribes (faster-whisper) and summarizes (llama3.2 via Ollama) into a two-line morning report
- Writes it to `reports/YYYY-MM-DD.md`, archives the source
- Optional sloth haiku appended for calm

## Why open innovation matters

- **Does it run on a laptop with no internet?** Yes — after the one-time model download, everything runs locally. No cloud APIs required.
- **Keep someone's data off a server they don't control?** Yes — notes never leave the device.
- **Fine-tune, swap models, or change agent behavior?** Yes — open-weight model means the brain is swappable; open-source Agents SDK means the harness is swappable.
- **Cost nothing to run?** Yes — local inference, zero API spend.

## Where the open approach worked better than a closed one

A closed stack would have meant cloud transcription + cloud LLM + API keys + per-run cost + third-party data flow. With Slothly, the entire loop — transcribe, summarize, report — runs offline, on-device, free. The open pieces (Ollama, faster-whisper, OpenAI Agents SDK) made the whole thing possible where a closed stack would have made it impractical.

## Sloth edition

The agent moves slow and steady, conserves energy, and does the work so you don't have to. You sleep; the agent works. You wake to a two-line report — and maybe a sloth haiku.

Built in public with open-source AI. 🦥
