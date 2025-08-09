# AI Agents News Research Rules

## Purpose
This document provides standardized instructions for using the ml-agent-researcher to gather daily AI agents news and updates for the machine learning vault.

## Research Agent Instructions

### Search Parameters
Use the ml-agent-researcher with the following prompt template:

```
IMPORTANT: First check recent news files (last 2-3 days) to identify already covered topics and avoid duplicates.

Search for recent AI agents research and scientific developments from the past week (around [DATE_RANGE]). Find 5-8 significant advances covering:

1. New research papers and studies with novel findings
2. Major model releases and frontier AI announcements (GPT, Claude, Gemini, etc.) - ONLY if not already covered in recent news
3. Technical breakthroughs and algorithmic advances
4. Framework updates with scientific improvements
5. Experimental results and benchmark achievements
6. Academic collaborations and research insights

DUPLICATE PREVENTION:
- AVOID repeating topics already covered in recent news files unless there are significant NEW developments
- If covering a previously mentioned topic, clearly state what's NEW and use "UPDATE:" prefix
- Focus on fresh developments, not previously reported content

For each item provide:
- Title and clear description focusing on the scientific/technical contribution (2-3 sentences)
- **Source links**: ALWAYS include clickable external links to original research papers, official announcements, or press releases
- Scientific significance and implications for the field
- Key technical details, metrics, or experimental results
- How it advances current understanding or capabilities

Prioritize scientific knowledge and significant technical advances. Include major industry model releases that represent meaningful capability improvements, while avoiding routine funding announcements or minor commercial updates.

IMPORTANT: When creating news files, ALWAYS use Obsidian formatting for better readability:
- Use ==highlights== for key metrics, performance improvements, dates, and breakthrough findings
- Add callouts to emphasize important developments:
  - > [!info] for significant research developments
  - > [!warning] for concerning trends or limitations
  - > [!note] for interesting insights or connections
- Highlight specific numbers, percentages, model names, and benchmark results
- Use callouts to break up content and draw attention to major breakthroughs
```

### Content Categories
Always include these sections when available:

1. **Research Breakthroughs**
   - Novel algorithmic approaches
   - Scientific discoveries and insights  
   - Performance benchmarks and comparisons

2. **Major Model Releases**
   - Frontier model launches (GPT, Claude, Gemini, LLaMA, etc.)
   - Significant capability improvements and technical advances
   - Performance benchmarks and architectural innovations
   - New model variants and specialized versions

3. **Technical Advances**
   - New methodologies and techniques
   - Architectural innovations
   - Experimental validations

4. **Academic Publications**
   - Recent papers from top venues (NeurIPS, ICML, ICLR, etc.)
   - Preprints with significant contributions
   - Survey papers and meta-analyses

5. **Framework/Tool Evolution**
   - Scientific improvements in existing tools
   - Open-source research contributions
   - Benchmark datasets and evaluation methods

6. **Knowledge Synthesis**
   - Cross-disciplinary connections
   - Theoretical insights and proofs
   - Replication studies and negative results

### File Naming Convention
- Create news files with date format: `YYYY-MM-DD.md`
- Store in `/news/` folder
- Mirror the same date as the daily note being updated

### Integration Workflow
1. **CHECK FOR DUPLICATES FIRST**: Read the 2-3 most recent news files to identify what has already been covered
2. Run research agent with current date parameters, explicitly instructing to avoid repeating recently covered topics
3. Create dated news file in `/news/` folder with full research output, focusing on NEW developments only
4. **ADD EXTERNAL REFERENCE LINKS**: Research and include clickable links to primary sources for each major topic
5. Create comprehensive "## Read More" section with organized external links
6. Extract key highlights for daily note update
7. Add concise summary to main daily note under "## AI Agents News - [DATE]" section

### Duplicate Prevention Rules
- **MANDATORY**: Always check the last 2-3 news files before creating new content
- **Only repeat topics if**: There are significant NEW updates, developments, or announcements (e.g., new capabilities, major updates, different benchmark results)
- **For repeated topics**: Use format like "UPDATE: [Topic] - [New Development]" and clearly state what's new
- **Avoid repeating**: Same model releases, identical research papers, or previously covered developments unless there are major updates
- **Focus on**: Fresh research papers, new experimental results, recent conference presentations, latest industry developments

### External Reference Links Requirements
- **MANDATORY**: Every major research topic must include a `**Source**:` line with external links
- Use format: `**Source**: [Link Title](URL) | [Additional Link](URL)`
- Prioritize: Original research papers, official institutional announcements, peer-reviewed publications
- Include comprehensive "## Read More" section with categorized external links:
  - Primary Research Sources
  - Academic Conferences and Workshops
  - Market Research and Analysis
  - Technical Research Papers

### Quality Standards
- Focus on scientific and educational value
- **ALWAYS include external reference links**: Each major topic MUST have clickable links to primary sources (research papers, official announcements, press releases)
- Include source links to papers, arxiv, research labs, and official company blogs
- Balance academic research with significant industry developments that advance the field
- Include major model releases from OpenAI, Anthropic, Google DeepMind, Meta AI, etc.
- Emphasize technical depth and research methodology
- Maintain neutral, academic tone
- Verify claims against peer-reviewed sources when possible
- Include experimental details and reproducibility information
- **Use Obsidian formatting**: Apply ==highlights== and callouts consistently for better readability
- **Emphasize key data**: Highlight performance metrics, model sizes, benchmark results, and breakthrough findings

## Example Usage

To update today's news:
1. Use Task tool with ml-agent-researcher subagent
2. Apply search template with current date range
3. Save full output to `news/YYYY-MM-DD.md`
4. Extract highlights for daily note integration