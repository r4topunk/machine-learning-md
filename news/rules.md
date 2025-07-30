# AI Agents News Research Rules

## Purpose
This document provides standardized instructions for using the ml-agent-researcher to gather daily AI agents news and updates for the machine learning vault.

## Research Agent Instructions

### Search Parameters
Use the ml-agent-researcher with the following prompt template:

```
Search for recent AI agents research and scientific developments from the past week (around [DATE_RANGE]). Find 5-8 significant scientific advances covering:

1. New research papers and studies with novel findings
2. Technical breakthroughs and algorithmic advances
3. Framework updates with scientific improvements
4. Experimental results and benchmark achievements
5. Academic collaborations and research insights

For each item provide:
- Title and clear description focusing on the scientific contribution (2-3 sentences)
- Source link and publication (prefer arxiv, academic journals, research labs)
- Scientific significance and implications for the field
- Key technical details, metrics, or experimental results
- How it advances current understanding or capabilities

Prioritize scientific knowledge and research evolution over commercial announcements or funding news.

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

2. **Technical Advances**
   - New methodologies and techniques
   - Architectural innovations
   - Experimental validations

3. **Academic Publications**
   - Recent papers from top venues (NeurIPS, ICML, ICLR, etc.)
   - Preprints with significant contributions
   - Survey papers and meta-analyses

4. **Framework/Tool Evolution**
   - Scientific improvements in existing tools
   - Open-source research contributions
   - Benchmark datasets and evaluation methods

5. **Knowledge Synthesis**
   - Cross-disciplinary connections
   - Theoretical insights and proofs
   - Replication studies and negative results

### File Naming Convention
- Create news files with date format: `YYYY-MM-DD.md`
- Store in `/news/` folder
- Mirror the same date as the daily note being updated

### Integration Workflow
1. Run research agent with current date parameters
2. Create dated news file in `/news/` folder with full research output
3. Extract key highlights for daily note update
4. Add concise summary to main daily note under "## AI Agents News - [DATE]" section

### Quality Standards
- Focus on scientific and educational value
- Include source links to papers, arxiv, research labs
- Prioritize scientific discoveries over commercial developments
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