# 🚀 Cold Outreach Pipeline for B2B SaaS — Research Project

![Status](https://img.shields.io/badge/Status-Completed-success)
![Research](https://img.shields.io/badge/Experts-10-blue)
![LinkedIn](https://img.shields.io/badge/LinkedIn-Research-blue)
![YouTube](https://img.shields.io/badge/YouTube-19%20Transcripts-red)
![Automation](https://img.shields.io/badge/API-youtube--transcript--api-orange)

> **Research project built for a B2B SaaS growth role application.**
> Methodology: manually identify top practitioners → collect their real public content via APIs and manual curation → synthesize cross-expert insights into an actionable playbook.
>
> **Tools used:** [Cursor AI](https://cursor.sh) (IDE) + [OpenAI Codex](https://codex.openai.com) (agentic coding tasks) + [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) (free transcript collection, no API key required)

---

## 📌 Why Cold Outreach Pipeline?

Chosen from 8 topic options because it offers:

- The **deepest pool of verifiable practitioners** — people who run agencies, manage SDR teams, or sell for a living *and* publish about it weekly
- A **tight, mappable pipeline** (ICP → list → message → sequence → objection → book → measure) that translates directly into a structured research framework
- **Direct relevance to GTM/RevOps/Growth hiring** — hiring managers in these roles actively test for this skill, so a well-documented research process demonstrates applied competence, not just theory

---

## 🗂️ Repository Structure

```
cold-outreach-research/
│
├── README.md                          ← you are here
│
├── research/
│   ├── sources.md                     ← 10 experts: who, why, links, annotations
│   │
│   ├── linkedin-posts/                ← posts organized by author
│   │   ├── josh-braun/
│   │   ├── alex-berman/
│   │   ├── will-aitken/
│   │   ├── morgan-j-ingram/
│   │   ├── jeremy-chatelaine/
│   │   ├── jack-reamer/
│   │   ├── kyle-coleman/
│   │   ├── armand-farrokh/
│   │   ├── nick-cegelski/
│   │   └── florin-tatulea/
│   │
│   ├── youtube-transcripts/           ← transcripts fetched via API, by video
│   │
│   └── other/
│       ├── synthesis.md               ← cross-expert tactic comparison (signal vs noise)
│       └── cold-outreach-playbook.md  ← final synthesized step-by-step pipeline
│
└── scripts/
    ├── fetch_youtube_transcripts.py   ← free transcript collector (no API key needed)
    └── claude_code_prompts.md         ← prompt playbook used with Codex
```
## 📚 Research Deliverables

This repository includes:

- Expert selection and source validation
- LinkedIn outreach research
- YouTube transcript collection
- Automated transcript collection workflow
- Cross-expert synthesis
- Cold outreach framework
- Executive research summary

Together these documents provide both the raw research data and the synthesized insights required to build a practical B2B SaaS cold outreach playbook.
---

## 👥 The 10 Experts

Practitioners selected by this criteria: they must **actively run** cold outreach (for clients, their own company, or coached teams) — not just write about it.

| # | Expert | Why They Qualify | Primary Channel | Perspective |
|---|--------|-----------------|-----------------|-------------|
| 1 | **Josh Braun** | Independent sales trainer; publishes weekly cold email rewrites from real screenshots | LinkedIn | Copywriting / messaging |
| 2 | **Alex Berman** | Ran cold email agencies (Experiment27, Email10k); tests messaging live with paying clients | LinkedIn + YouTube | Agency / offer design |
| 3 | **Will Aitken** | Live-tests outreach tools and cadences; publishes response-rate comparisons with real numbers | LinkedIn | Tooling / deliverability |
| 4 | **Morgan J Ingram** | Coached 50,000+ sellers on outbound; CEO of AMP Social, embedded coaching for SDR teams | LinkedIn + YouTube | Team systems / coaching |
| 5 | **Jeremy Chatelaine** | Founder of QuickMail (cold email platform); publishes real campaign data from his own product | Podcast | Deliverability / infrastructure |
| 6 | **Jack Reamer** | Founder of SalesBread (lead-gen agency); runs live LinkedIn + email campaigns for B2B clients daily | Podcast | LinkedIn DMs / copywriting |
| 7 | **Kyle Coleman** | Built outbound at Looker + Clari from scratch; now VP Marketing at ClickUp; publishes from the *buyer's* side | LinkedIn | Buyer perspective |
| 8 | **Armand Farrokh** | Ex-VP Sales (Pave, Carta); co-hosts 30 Minutes to President's Club — highest-profile B2B sales podcast | Podcast + YouTube | Aggregated best practices |
| 9 | **Nick Cegelski** | 3× top enterprise seller before co-founding 30MPC; pushes guests on exact sequences sent | Podcast | Sequencing / cadence |
| 10 | **Florin Tatulea** | Practicing seller; featured on 30MPC for cold-call-integrated outreach with numbers-backed data | LinkedIn + Podcast | Cold call + outreach integration |

**Coverage across perspectives:**

```
LinkedIn organic posts   →  Braun, Berman, Aitken, Ingram, Coleman, Farrokh, Tatulea
YouTube video content    →  Berman, Ingram, 30MPC channel
Podcast (audio/video)    →  Chatelaine + Reamer, Farrokh + Cegelski
Buyer-side perspective   →  Coleman
Agency/practitioner      →  Berman, Reamer
Software/data side       →  Chatelaine
Team/manager side        →  Ingram
Cold call integration    →  Tatulea
```

---

## 🛠️ How This Was Built

### Tools

| Tool | Role in this project |
|------|---------------------|
| **Cursor AI** | IDE — opened the repo, edited files, ran the terminal |
| **OpenAI Codex** | Agentic coding — ran the transcript script, organized files, wrote summaries, built the synthesis doc |
| **youtube-transcript-api** | Free Python package — pulled YouTube transcripts without needing any API key or credentials |
| **Manual collection** | LinkedIn posts — copied by hand from public profiles (LinkedIn has no compliant public API; this approach is transparent and ToS-safe) |

### Workflow step by step

```
1. Scaffold created (this repo structure)
        ↓
2. Sources identified and documented in research/sources.md
        ↓
3. YouTube video IDs collected manually (5 min per expert)
        ↓
4. Codex task → runs fetch_youtube_transcripts.py → saves transcripts to research/youtube-transcripts/
        ↓
5. LinkedIn posts copied manually from public profiles (5–10 per expert)
        ↓
6. Codex task → fills in "Key tactic(s) extracted" section in every file
        ↓
7. Codex task → writes research/other/synthesis.md (cross-expert comparison)
        ↓
8. Codex task → writes research/other/cold-outreach-playbook.md (final deliverable)
```

### How Codex was used (not just mentioned)

Each Codex task was given as a specific natural-language instruction referencing actual file paths in this repo. Codex ran in an isolated cloud environment connected to this GitHub repository and opened pull requests after completing each task — those PRs are visible in this repo's pull request history.

Example Codex tasks issued:

```
"Install youtube-transcript-api, fill in the VIDEOS list in 
scripts/fetch_youtube_transcripts.py with these video IDs, run 
the script, and confirm each transcript is saved under 
research/youtube-transcripts/"
```

```
"Read every markdown file under research/linkedin-posts/ and 
research/youtube-transcripts/. For each file, fill in the 
'Key tactic(s) extracted' section with 2–4 bullets describing the 
specific, actionable tactic — concrete enough to implement tomorrow."
```

```
"Read all collected content. Write research/other/synthesis.md with 
three sections: (1) tactics 3+ experts independently agree on, 
(2) tactics only 1–2 experts mention, (3) direct contradictions 
between experts."
```

---

## 📄 File Format — Every Post and Transcript

Each collected piece of content follows this template:

```markdown
# [Author] — [Title]
- Source: [URL]
- Date published: YYYY-MM-DD
- Date collected: YYYY-MM-DD
- Format: LinkedIn post | YouTube video | Podcast episode

## Raw content
(full text or transcript)

## Key tactic(s) extracted
- ...

## Where this agrees/disagrees with other experts in this repo
- ...
```

---

## 📊 What the Synthesis Produces

After collection, `research/other/synthesis.md` cross-references all experts to produce:

**Strong signal** — tactics that 3+ independent experts agree on (e.g. personalized first line referencing a specific trigger event, multi-channel sequences, short CTAs asking for permission not a meeting)

**Worth testing** — tactics 1–2 experts use but others don't mention (e.g. specific subject line formulas, video thumbnails in email)

**Contradictions** — where experts disagree and why (e.g. how much personalization is worth the time investment at scale)

The final `research/other/cold-outreach-playbook.md` turns the synthesis into a step-by-step pipeline:

```
ICP definition → List building → Message design → 
Sequence / cadence → Objection handling → Booking → What to measure
```

Each step is cited to the expert(s) it's sourced from.

---

## ⚙️ Running the Transcript Script Yourself

```bash
# Install dependency (no API key needed)
pip install youtube-transcript-api

# Add your video IDs to the VIDEOS list in the script
# then run:
python scripts/fetch_youtube_transcripts.py
```

Output files land in `research/youtube-transcripts/` as named markdown files.

---

## 📝 A Note on LinkedIn Collection

LinkedIn does not offer a public API for reading others' posts, and third-party scraping tools violate their Terms of Service. All LinkedIn posts in this repo were **copied manually from public profiles** — the author name, post URL, and date are included in every file. This approach is slower but correct, and reflects the kind of judgment that matters in a professional research context.

---

## 🔗 Sources Quick Reference

Full annotations in `research/sources.md`. Quick links:

- Josh Braun → linkedin.com/in/josh-braun
- Alex Berman → linkedin.com/in/alexanderberman
- Will Aitken → linkedin.com/in/justwillaitken
- Morgan J Ingram → linkedin.com/in/morganjingramamp
- Jeremy Chatelaine + Jack Reamer → *Cold Email Outreach* podcast (Apple / Spotify)
- Kyle Coleman → linkedin.com/in/kyletcoleman
- Armand Farrokh + Nick Cegelski → *30 Minutes to President's Club* (Apple / Spotify / YouTube)
- Florin Tatulea → search "Florin Tatulea" on LinkedIn

---


## Author

**Nishchit Sheth**

Built as a practical research project demonstrating structured research, technical automation, documentation, and synthesis for modern B2B SaaS cold outreach.

**Technologies Used**

- Cursor AI
- OpenAI Codex
- Google Colab
- youtube-transcript-api
- Git & GitHub
- Markdown
- Python
