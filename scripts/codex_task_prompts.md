# Codex Task Prompts
# Cold Outreach Pipeline — Research Project
# Tools: Cursor AI + OpenAI Codex (codex.openai.com)

Run these one at a time in Codex. Wait for each task to complete and
merge the pull request before starting the next one.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## TASK 1 — Install dependencies and fetch YouTube transcripts

Paste this into Codex, replacing the URLs with real ones you found:

─────────────────────────────────────────────────────────────────────
Install youtube-transcript-api using pip.

Then open scripts/fetch_youtube_transcripts.py and fill in the VIDEOS
list with the following YouTube video IDs. Extract the video_id from
each URL (the part after "v="), set the author_slug to match the folder
name in research/linkedin-posts/, and use today's date as the
collected date.

Video URLs:
[PASTE 2-3 YOUTUBE URLS PER EXPERT HERE — example format below]
- https://www.youtube.com/watch?v=XXXXXXXXX   (Alex Berman — cold email teardown)
- https://www.youtube.com/watch?v=XXXXXXXXX   (Morgan Ingram — outbound sequence)
- https://www.youtube.com/watch?v=XXXXXXXXX   (30MPC — prospecting episode)

After filling in the list, run the script and confirm each .md file
was saved to research/youtube-transcripts/.
─────────────────────────────────────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## TASK 2 — Save LinkedIn posts (one author at a time)

Paste this into Codex for each author after manually copying their posts:

─────────────────────────────────────────────────────────────────────
Create a new markdown file in research/linkedin-posts/[AUTHOR-FOLDER]/
named [YYYY-MM-DD]_[short-topic-slug].md

Use this exact template:

# [Author Name] — [Post topic]

- Source: [LinkedIn post URL]
- Date published: [YYYY-MM-DD]
- Date collected: [today's date]
- Format: LinkedIn post

---

## Raw content

[PASTE THE POST TEXT HERE]

---

## Key tactic(s) extracted

- TODO

---

## Where this agrees / disagrees with other experts in this repo

- TODO

Here is the post to save:
Author: [name]
URL: [paste URL]
Date: [paste date]
Text: [paste full post text]
─────────────────────────────────────────────────────────────────────

Repeat for each post. Aim for 5–10 posts per author, only those
directly about cold outreach tactics (skip career updates, memes,
congratulations posts).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## TASK 3 — Fill in "Key tactic(s) extracted" for all files

Run this after Tasks 1 and 2 are complete and merged:

─────────────────────────────────────────────────────────────────────
Read every markdown file under research/linkedin-posts/ and
research/youtube-transcripts/.

For each file, fill in the "Key tactic(s) extracted" section with
2–4 bullet points. Each bullet must describe a specific, actionable
tactic — concrete enough to implement tomorrow morning.

Good example:
  - Opens cold emails with a single sentence referencing a recent
    trigger event (funding round, new job title, product launch)
    rather than a generic compliment

Bad example (too vague — reject this style):
  - Be more personal in your outreach

Also fill in "Where this agrees / disagrees with other experts in
this repo" using what you've read across all files so far.
─────────────────────────────────────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## TASK 4 — Write the cross-expert synthesis

Run this after Task 3 is merged:

─────────────────────────────────────────────────────────────────────
Read all files under research/linkedin-posts/ and
research/youtube-transcripts/.

Write a new file research/other/synthesis.md with this structure:

# Cross-Expert Synthesis — Cold Outreach Tactics

## 1. Strong Signal (3+ experts independently agree)
(list tactics multiple experts mention without referencing each other)

## 2. Worth Testing (1–2 experts mention, not widely validated)
(list tactics from fewer sources — interesting but less proven)

## 3. Direct Contradictions Between Experts
(where experts disagree — note who says what, and which view seems
better supported by evidence or context)

## 4. Gaps — What No One Talks About
(angles or pipeline stages that are underrepresented across all sources)

Be specific. Cite which expert each point comes from.
─────────────────────────────────────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## TASK 5 — Write the final cold outreach playbook

Run this last, after Task 4 is merged:

─────────────────────────────────────────────────────────────────────
Using research/other/synthesis.md and research/sources.md, write a
new file research/other/cold-outreach-playbook.md

Structure it as a step-by-step cold outreach pipeline for a B2B SaaS
company with the following sections:

1. ICP Definition — who to target and why
2. List Building — where to source leads and how to qualify them
3. Message Design — subject lines, opening lines, CTAs
4. Sequence & Cadence — how many touches, which channels, what timing
5. Objection Handling — most common objections and how top performers respond
6. Booking — what the actual ask should be and how to frame it
7. What to Measure — the metrics that actually matter vs vanity metrics

For each section, cite which expert(s) the recommendation is based on.
Where experts disagree, note both views.

Write it as a practical reference document, not a summary of the research.
─────────────────────────────────────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Tips for using Codex efficiently

- Give ONE task at a time. Codex works best with focused, scoped instructions.
- Always merge the pull request Codex opens before giving it the next task.
- If Codex asks a clarifying question, answer it briefly and let it continue.
- For Task 2 (LinkedIn posts), batch 2–3 posts per Codex session rather than
  one at a time — paste multiple posts in one prompt and let Codex create all
  the files at once.
- Free tier tip: smaller, specific tasks use fewer credits than large vague ones.
  The prompts above are already scoped to stay within free tier limits per session.
