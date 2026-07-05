# Methodology

## Objective

Document a practical, evidence-based cold outreach research process by collecting public material from experienced B2B sales practitioners and organizing it into a reusable repository.

## Research Scope

This repository focuses on cold outreach tactics relevant to B2B SaaS growth and sales workflows. The current scope includes expert commentary gathered from public LinkedIn posts, YouTube transcripts, and curated notes stored in the research directories.

## Expert Selection Criteria

Experts are included when they demonstrate active, real-world experience with cold outreach through one or more of the following:

- Operating as a practitioner, advisor, founder, or sales leader with direct outbound experience
- Publishing repeatable tactical guidance rather than only high-level opinion
- Sharing material often enough to allow comparison across experts
- Contributing perspectives from different parts of the outreach process, such as messaging, sequencing, deliverability, or coaching

## Data Collection Method

Data is collected from public sources and stored as markdown for traceability. The current repository structure supports:

- Manual collection of expert insights and public posts
- Scripted retrieval of YouTube transcripts using the Python script in `scripts/fetch_youtube_transcripts.py`
- Source attribution within repository files so each note can be traced back to its origin

## Data Validation Approach

Validation is based on transparency and cross-checking rather than automated scoring. The working approach is to:

- Preserve the original source link and publication context where available
- Compare similar claims across multiple experts to identify repeated patterns
- Separate raw collected material from later synthesis to keep interpretation reviewable
- Prefer tactics that appear across multiple independent practitioners

## Repository Organization

The repository is organized to keep source collection, automation, and documentation separate:

- `research/` stores collected source material and synthesized notes
- `research/linkedin-posts/` groups markdown notes by expert
- `research/other/` holds supporting research outputs
- `scripts/` contains Python utilities used during collection
- `docs/` stores higher-level project documentation, including this methodology file

## Limitations

This repository has several practical limitations:

- Coverage depends on publicly available content rather than private campaign data
- Manual collection can introduce inconsistency in detail or formatting
- Transcript-based sources may miss tone, visuals, or context from the original media
- The current dataset reflects a selected subset of experts rather than the full market

## Ethical Considerations

The repository should rely on public, attributable material and avoid misrepresenting expert views. Collection and synthesis should:

- Respect platform terms and avoid unauthorized scraping of restricted content
- Keep source attribution intact
- Distinguish clearly between raw source material and interpretation
- Avoid presenting anecdotal tactics as universal truth without context

## Future Improvements

Future iterations could strengthen the research process by:

- Standardizing metadata across all collected files
- Adding a repeatable review checklist for each new source
- Expanding validation through more cross-expert comparison notes
- Introducing lightweight summaries or tags to improve navigation
- Adding tests or checks for collection scripts as the repository grows

## AI-Assisted Workflow

Artificial intelligence was used as a productivity tool during this project.

OpenAI Codex assisted with repository organization, transcript collection workflows, markdown generation, and repetitive development tasks.

All expert selection, source verification, research interpretation, and final conclusions were manually reviewed before being committed to the repository.

## Reproducibility

Anyone can reproduce this repository by following the documented workflow, collecting public source material, and running the provided Python scripts without requiring proprietary software or paid APIs.