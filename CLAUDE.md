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

### **CRITICAL: Rules.md Check Requirement**

**BEFORE writing or creating any content in ANY folder, you MUST:**
1. **Check for rules.md**: Always look for a `rules.md` file in the target folder first
2. **Read and Follow**: If a `rules.md` exists, read it completely and follow ALL formatting, content, and procedural requirements specified
3. **Apply Formatting**: Ensure all output matches the exact formatting requirements (Obsidian callouts, highlights, structure, etc.)
4. **Validate Compliance**: Verify your output meets all rules before finalizing

**This applies to ALL agents and ALL folders including:**
- `/news/` - Follow `/news/rules.md` for formatting, callouts, highlights, and content structure
- `/research/` - Follow `/research/rules.md` for methodology and documentation format  
- `/daily/` - Check for any folder-specific rules
- Any other directories - Always check for local rules before proceeding

### Content Linking and Duplication Prevention

**ALWAYS prioritize linking over duplication:**
1. **Search First**: Before creating new content, search existing vault for related topics using Grep/Glob tools
2. **Link Instead of Duplicate**: Use `[[note-name]]` or `[[folder/note-name]]` to reference existing content rather than rewriting it
3. **Cross-Reference**: When mentioning topics covered elsewhere, always link to the existing detailed coverage
4. **Build Connections**: Use Obsidian's linking system to create knowledge networks rather than isolated content
5. **Reference Existing Research**: Link to existing research files using `[[research/topic-name]]` format when relevant

**Examples of good linking practices:**
- Instead of rewriting transformer details: "For transformer architecture details, see [[research/transformer-architectures]]"
- Reference related daily notes: "Similar developments covered in [[daily/2025-07-30]]"
- Link to comprehensive analyses: "Full analysis available at [[research/multi-agent-systems]]"

### Folder-Specific Rules
- Always create news files inside the news folder
- Read and follow the rules specified in `/news/rules.md` when working with news content
- Use ml-agent-researcher and obsidian-knowledge-curator agents proactively when their capabilities match the task requirements