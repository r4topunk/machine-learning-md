# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Obsidian vault for documenting machine learning learnings and research. The vault contains daily notes with curated links to videos, articles, and resources about various ML/AI topics including:

- AI agents and multi-agent workflows
- Neural networks (CNNs, GANs, Transformers)
- Memory systems for AI applications
- Development tools and frameworks
- Research papers and tutorials

## Vault Structure

The vault follows a simple daily note structure with organized research:
- **Daily Notes**: Files named `YYYY-MM-DD.md` in the `/daily/` directory containing learning resources for that day
- **News Folder**: `/news/` directory containing detailed AI agents research and updates
- **Research Folder**: `/research/` directory for structured topic analysis
- **Content Format**: Each note contains YouTube video embeds and links to relevant resources
- **News Integration**: Daily notes include AI agents news summaries from corresponding news files

## Obsidian Configuration

The vault uses standard Obsidian features:
- **File Explorer**: For navigating daily notes
- **Search**: For finding specific topics across all notes
- **Backlinks/Outgoing Links**: For discovering connections between topics
- **Tags**: For categorizing content (though not heavily used currently)
- **Git Integration**: Via obsidian-git plugin for version control

## Working with Content

When adding or organizing content:
- Follow the daily note naming convention (`YYYY-MM-DD.md`) in the `/daily/` directory
- Include descriptive titles for YouTube videos using the `![Title](URL)` format
- Add direct links to articles, documentation, and tools
- Keep content focused on ML/AI learning resources
- Use the existing simple format - no complex templating needed

### AI Agents News Workflow

For daily AI agents news updates:
1. **Research**: Use ml-agent-researcher with standardized prompt from `/news/rules.md`
2. **Storage**: Create detailed news file in `/news/YYYY-MM-DD.md` with full research output
3. **Integration**: Add concise summary to daily note under "## AI Agents News - [DATE]" section
4. **Categories**: Include industry breakthroughs, framework updates, research developments, funding, and government adoption
5. **Quality**: Focus on educational value, include source links, maintain neutral tone

### Research Workflow

For structured topic research and analysis:
1. **Discovery**: Follow `/research/rules.md` methodology to search existing content and identify connections
2. **Research**: Use appropriate research agents (ml-agent-researcher for AI topics, general-purpose for others)
3. **Documentation**: Create comprehensive research files using `/research/template.md` format
4. **Topic Relationships**: Identify and document connections between research topics
5. **Integration**: Reference research files from daily notes using `[[research/topic-name]]` format
6. **Maintenance**: Update research files when new developments or connections are discovered

## Note Organization

Content is organized chronologically by date with structured research support:
- **Daily Notes**: Chronological organization for tracking learning progression over time
- **Research Files**: Topic-based organization for deep analysis
- **Natural Discovery**: Related topics through Obsidian's linking features
- **Flexible Structure**: Simple daily notes with optional deep-dive research when needed

## Common Topics Covered

Based on existing notes, the vault covers:
- **AI Development Tools**: Claude Code, Cursor, LangChain
- **Neural Network Architectures**: CNNs, GANs, Transformers
- **Agent Systems**: Multi-agent workflows, memory systems
- **Educational Resources**: Tutorial videos, research papers
- **Development Frameworks**: Various ML/AI libraries and tools

## Guidelines and Rules

- Always create news files inside the news folder
- Read and follow the rules specified in `/news/rules.md` when working with news content