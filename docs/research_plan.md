# Research Collection Plan

## Collection Workflow

1. Identify expert and source.
2. Use OpenAI Codex to assist with repository tasks and transcript collection.
3. Retrieve YouTube transcripts using `youtube-transcript-api`.
4. Collect LinkedIn posts manually from public profiles.
5. Store all source material as markdown.
6. Review and extract actionable tactics.
7. Cross-reference findings across experts.

## Objective

Collect consistent, traceable public research for the Cold Outreach Pipeline project by gathering high-signal content from 10 selected practitioners across LinkedIn, YouTube, and podcasts, then storing that material in a repository structure that supports later synthesis and cross-expert comparison.

## Experts Included

| Expert | Primary platform | Secondary platform | Primary expertise |
|---|---|---|---|
| Josh Braun | LinkedIn | Podcasts | Cold email copywriting and messaging |
| Alex Berman | LinkedIn | YouTube | Cold email campaigns, list building, and offers |
| Will Aitken | LinkedIn | YouTube | Outreach tooling, AI usage, and response-rate testing |
| Morgan J Ingram | LinkedIn | YouTube | Outbound coaching, SDR systems, and team execution |
| Jeremy Chatelaine | Podcast | LinkedIn | Deliverability, infrastructure, and cold email systems |
| Jack Reamer | Podcast | LinkedIn | LinkedIn DMs, prospecting copy, and agency execution |
| Kyle Coleman | LinkedIn | Podcasts | Buyer-side outbound feedback and messaging quality |
| Armand Farrokh | Podcast | LinkedIn | Prospecting systems and cross-expert outbound tactics |
| Nick Cegelski | Podcast | LinkedIn | Sequencing, cadence, and practical prospecting specifics |
| Florin Tatulea | LinkedIn | Podcast | Cold call and cold email integration |

## Collection Targets

Each expert should be collected using the same baseline target so the final dataset is comparable across sources.

### Josh Braun

Target:

- Up to 5 recent LinkedIn posts
- Up to 3 recent YouTube videos
- Relevant podcast episodes when available

### Alex Berman

- 5 LinkedIn posts, or latest available
- 2-3 YouTube videos if available
- Relevant podcast appearances where applicable

### Will Aitken

- 5 LinkedIn posts, or latest available
- 2-3 YouTube videos if available
- Relevant podcast appearances where applicable

### Morgan J Ingram

- 5 LinkedIn posts, or latest available
- 2-3 YouTube videos if available
- Relevant podcast episodes or guest appearances where applicable

### Jeremy Chatelaine

- 5 LinkedIn posts, or latest available
- 2-3 YouTube videos if available
- Podcast episodes from *Cold Email Outreach with Jeremy & Jack* and other relevant appearances

### Jack Reamer

- 5 LinkedIn posts, or latest available
- 2-3 YouTube videos if available
- Podcast episodes from *Cold Email Outreach with Jeremy & Jack* and other relevant appearances

### Kyle Coleman

- 5 LinkedIn posts, or latest available
- 2-3 YouTube videos if available
- Relevant podcast appearances where applicable

### Armand Farrokh

- 5 LinkedIn posts, or latest available
- 2-3 YouTube videos if available
- Relevant episodes from *30 Minutes to President's Club* and other appearances

### Nick Cegelski

- 5 LinkedIn posts, or latest available
- 2-3 YouTube videos if available
- Relevant episodes from *30 Minutes to President's Club* and other appearances

### Florin Tatulea

- 5 LinkedIn posts, or latest available
- 2-3 YouTube videos if available
- Podcast episodes where applicable, especially interviews focused on outbound execution

## Folder Mapping

Collected material should be stored in repository folders by source type so raw inputs stay easy to review and compare.

- LinkedIn posts should be stored under `research/linkedin-posts/<expert-slug>/` as individual markdown files, one file per post.
- YouTube transcripts should be stored under `research/youtube-transcripts/` as individual markdown files, named clearly with expert name and video topic or ID.
- Podcast episodes should be stored under `research/podcasts/<expert-slug>/` if a dedicated folder is created, or under `research/other/` as clearly labeled markdown notes until a dedicated podcast folder exists.
- Cross-expert comparison notes, synthesis documents, and final pipeline outputs should be stored under `research/other/`.
- High-level process documentation and collection guidance should be stored under `docs/`.

Suggested expert slugs should match the existing LinkedIn folder naming:

- `josh-braun`
- `alex-berman`
- `will-aitken`
- `morgan-j-ingram`
- `jeremy-chatelaine`
- `jack-reamer`
- `kyle-coleman`
- `armand-farrokh`
- `nick-cegelski`
- `florin-tatulea`

## Quality Checklist

Every collected item should include:

- [ ] Source URL
- [ ] Publication date
- [ ] Collection date
- [ ] Raw content
- [ ] Extracted tactics
- [ ] Cross-reference notes

Quality is prioritized over quantity: if a source is incomplete, ambiguous, or weakly relevant, it is better to collect fewer items and keep the dataset clean, attributable, and useful.
