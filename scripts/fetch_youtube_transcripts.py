"""
fetch_youtube_transcripts.py
────────────────────────────
Fetches YouTube transcripts for free — no API key required.
Uses the open-source `youtube-transcript-api` package.

SETUP
─────
    pip install youtube-transcript-api

USAGE
─────
1. Add your video entries to the VIDEOS list below.
   Each entry is a tuple of:
     (author_slug, title_slug, video_id, full_url, published_date)

   video_id = the part after "v=" in a YouTube URL
   e.g. https://www.youtube.com/watch?v=dQw4w9WgXcQ → "dQw4w9WgXcQ"

2. Run:
     python scripts/fetch_youtube_transcripts.py

3. Each transcript is saved to research/youtube-transcripts/ as:
     AuthorSlug_TitleSlug.md

HOW CODEX USES THIS
────────────────────
When you give Codex the task prompt from scripts/codex_task_prompts.md,
Codex will fill in the VIDEOS list with the URLs you paste and run
this script automatically.
"""

import os
from datetime import date

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    raise SystemExit(
        "\n[ERROR] youtube-transcript-api is not installed.\n"
        "Run:  pip install youtube-transcript-api\n"
    )

# ─── OUTPUT DIRECTORY ────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "research", "youtube-transcripts"
)

# ─── VIDEO LIST ──────────────────────────────────────────────────────────────
# Format: (author_slug, title_slug, video_id, url, published_date)
#
# FILL THIS IN — either manually or let Codex populate it from a list of URLs.
# Keep author_slug consistent with the folder names in research/linkedin-posts/
#
VIDEOS = [
    # Examples — replace with real entries:
    # ("Alex_Berman",    "cold_email_teardown_2026",  "VIDEO_ID", "https://youtube.com/watch?v=VIDEO_ID", "2026-06-01"),
    # ("Morgan_Ingram",  "sdr_outbound_sequence",     "VIDEO_ID", "https://youtube.com/watch?v=VIDEO_ID", "2026-05-15"),
    # ("Armand_Farrokh", "30mpc_prospecting_ep200",   "VIDEO_ID", "https://youtube.com/watch?v=VIDEO_ID", "2026-06-10"),
]

# ─── TEMPLATE ────────────────────────────────────────────────────────────────
TEMPLATE = """\
# {author} — {title}

- Source: {url}
- Date published: {published}
- Date collected: {collected}
- Format: YouTube video

---

## Raw transcript

{transcript}

---

## Key tactic(s) extracted

- TODO (fill in manually, or ask Codex: "Fill in the key tactics extracted section for every file in research/youtube-transcripts/")

---

## Where this agrees / disagrees with other experts in this repo

- TODO
"""

# ─── RUNNER ──────────────────────────────────────────────────────────────────
def fetch_and_save(author, slug, video_id, url, published):
    print(f"  Fetching: {author} / {slug} ({video_id}) ...", end=" ")
    try:
        segments = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as err:
        print(f"SKIPPED — {err}")
        return

    transcript_text = "\n".join(seg["text"] for seg in segments)
    filename = f"{author}_{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(
            author=author.replace("_", " "),
            title=slug.replace("_", " ").title(),
            url=url,
            published=published,
            collected=date.today().isoformat(),
            transcript=transcript_text,
        ))
    print(f"saved → {filename}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not VIDEOS:
        print("\n[INFO] No videos in the VIDEOS list yet.")
        print("Add entries manually, or paste a list of YouTube URLs to Codex")
        print("using the prompt in scripts/codex_task_prompts.md (Task 1).\n")
    else:
        print(f"\nFetching {len(VIDEOS)} video(s)...\n")
        for entry in VIDEOS:
            fetch_and_save(*entry)
        print("\nDone. Check research/youtube-transcripts/ for output files.\n")
