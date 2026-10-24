"""Slothly — nightly orchestration: inbox -> report."""

import shutil
from datetime import date
from pathlib import Path

from summarize import generate_haiku, summarize

BASE = Path(r"C:\Users\param\Documents\Projects\Slothly")
INBOX = BASE / "inbox"
REPORTS = BASE / "reports"
ARCHIVE = BASE / "archive"

AUDIO_EXTS = {".m4a", ".mp3", ".wav", ".m4b"}


def transcribe(path: Path) -> str:
    from faster_whisper import WhisperModel

    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    return model.transcribe(str(path)).text


def process_file(path: Path) -> str | None:
    if path.suffix.lower() == ".txt":
        text = path.read_text(encoding="utf-8", errors="ignore")
        summary = summarize(text)
    elif path.suffix.lower() in AUDIO_EXTS:
        text = transcribe(path)
        summary = summarize(text)
    else:
        return None

    report = f"# Slothly — {date.today():%Y-%m-%d}\n\n{summary}\n\n{generate_haiku(text)}\n"
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / f"{date.today():%Y-%m-%d}.md").write_text(report, encoding="utf-8")
    shutil.move(str(path), str(ARCHIVE / path.name))
    return summary


def main() -> None:
    INBOX.mkdir(parents=True, exist_ok=True)
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    for f in sorted(INBOX.iterdir()):
        if f.is_file():
            summary = process_file(f)
            print(f"[{date.today():%Y-%m-%d}] processed {f.name}: {summary}")


if __name__ == "__main__":
    main()
