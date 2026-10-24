"""Slothly — agent layer."""

from agents import Agent, Runner, function_tool

from summarize import summarize


@function_tool
def transcribe_audio(file_path: str) -> str:
    """Transcribe an audio file (e.g. .m4a/.mp3 voice memo) into text."""
    from faster_whisper import WhisperModel

    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    result = model.transcribe(file_path)
    return result.text


@function_tool
def summarize_tool(text: str) -> str:
    """Summarize a text note into exactly two lines."""
    return summarize(text)


@function_tool
def compose_report(transcript: str) -> str:
    """Compose the final two-line morning report from a transcript/text."""
    if not transcript or not transcript.strip():
        return "No content to summarize."
    return summarize(transcript)


agent = Agent(
    name="Slothly",
    model="llama3.2",
    instructions=(
        "You are Slothly, a lazy but brilliant assistant. "
        "When given a note or transcript, you produce exactly two lines: "
        "the first line is the summary, the second is the key action/takeaway."
    ),
    tools=[transcribe_audio, summarize_tool, compose_report],
)


if __name__ == "__main__":
    result = Runner.run_sync(
        agent,
        input=(
            "Summarize this note into the two-line report: "
            "Just had a long day. The client demo went well but the slides were a mess. "
            "Still need to send the recap email to the team and book a follow-up call with the stakeholder before the week ends."
        ),
    )
    print(result.final_output)
