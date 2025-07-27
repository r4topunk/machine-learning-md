# AI Agents News Research Rules

## Purpose
This document provides standardized instructions for using the ml-agent-researcher to gather daily AI agents news and updates for the machine learning vault.

## Research Agent Instructions

### Search Parameters
Use the ml-agent-researcher with the following prompt template:

```
Search for recent news and developments in the AI agents field from the past week (around [DATE_RANGE]). Focus on finding:

1. New research papers or breakthroughs in multi-agent systems
2. Industry news about AI agent frameworks and tools
3. Notable developments in agent coordination and collaboration
4. Updates on major AI agent projects or companies
5. Technical advances in agent architectures or capabilities

Please provide a curated list of the most significant findings with:
- Brief descriptions of each news item
- Source links where available
- Relevance to machine learning research and development
- Focus on educational and research value

Return the findings in a format suitable for adding to a daily learning note in an Obsidian vault.
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