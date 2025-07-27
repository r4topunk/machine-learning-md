# AI Agents News Research Rules

## Purpose
This document provides standardized instructions for using the ml-agent-researcher to gather daily AI agents news and updates for the machine learning vault.

## Research Agent Instructions

### Search Parameters
Use the ml-agent-researcher with the following prompt template:

```
Search for recent AI agents news from the past week (around [DATE_RANGE]). Find the 3-5 most significant developments covering:

1. Major product releases or breakthroughs
2. Notable research papers or studies
3. Framework updates or new tools

For each item provide ONLY:
- Title and 1-sentence description
- Source link
- Why it's significant (1 line)

Keep responses concise and focused. Avoid lengthy explanations or technical deep-dives.
```

### Content Categories
Always include these sections when available:

1. **Major Industry Breakthroughs**
   - New product launches
   - Significant technical achievements
   - Performance benchmarks

2. **Framework Updates**
   - Popular framework releases
   - Feature updates
   - Comparison insights

3. **Research Developments**
   - Academic papers
   - Performance studies
   - Survey results

4. **Industry Funding**
   - New companies
   - Funding rounds
   - Acquisitions

5. **Government/Enterprise Adoption**
   - Policy changes
   - Large-scale deployments
   - Strategic partnerships

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
- Focus on educational and research value
- Include source links when available
- Prioritize technical developments over marketing announcements
- Maintain neutral, informative tone
- Verify claims against multiple sources when possible

## Example Usage

To update today's news:
1. Use Task tool with ml-agent-researcher subagent
2. Apply search template with current date range
3. Save full output to `news/YYYY-MM-DD.md`
4. Extract highlights for daily note integration