---
allowed-tools: Task, Glob, Grep, Read, Write, TodoWrite
description: Research any topic using specialized agents and create structured documentation
argument-hint: <topic> [type]
---

# Research Command

Research any topic using specialized agents and create structured documentation following the vault's research methodology.

## Arguments
- `topic` (required): The topic to research
- `type` (optional): Research type - "ml" (default), "agents", or "general"

## Context
- Vault structure: @research/rules.md
- Research template: @research/template.md  
- Connection map: @research/connection-map.md

## Your task

Research the topic "$ARGUMENTS" following this methodology:

### Step 1: Discovery Phase
1. Search existing vault content using Grep/Glob for related topics and connections
2. Check daily notes for previous coverage of this topic
3. Review news archives in `/news/` for relevant developments
4. Identify existing research files for potential connections

### Step 2: Research Phase
Based on the topic type, use appropriate agent:

**For ML/AI Topics (default):**
Use ml-agent-researcher with this prompt:
```
Research the topic "$ARGUMENTS" with focus on:
1. Core concepts and technical foundations
2. Recent developments and breakthroughs (2024-2025)
3. Practical applications and use cases
4. Key researchers, papers, and resources
5. Connections to other ML/AI domains
6. Learning resources (videos, tutorials, documentation)

Provide findings in format suitable for Obsidian vault integration with:
- Clear explanations for learning purposes
- Source links for further exploration
- Connections to related topics already covered
- Practical implementation examples where relevant
```

**For AI Agents:**
Use ml-agent-researcher with agent-specific focus on architectures, frameworks, multi-agent patterns, and industry implementations.

**For General Topics:**
Use general-purpose agent for comprehensive research outside ML/AI domain.

### Step 3: Documentation Phase
1. Create research file at `/research/[topic-name].md` using the template format
2. Include overview, key concepts, recent developments, applications
3. Add related topics with connection explanations
4. Provide resources and learning paths
5. Include implementation examples where relevant

### Step 4: Integration Phase
1. Update `/research/connection-map.md` with new topic relationships
2. Suggest relevant daily note references using `[[research/topic-name]]` format
3. Identify gaps for future research
4. Map learning progression pathways

## Quality Standards
- Use primary sources, multiple perspectives, current relevance (2024-2025)
- Create meaningful connections with context explanations
- Focus on educational value and learning progression
- Link to papers, documentation, and official resources
- Build from simple to complex concepts

## Output Requirements
1. **Research File**: Comprehensive `/research/[topic-name].md` analysis
2. **Connection Updates**: Modified connection map with relationships
3. **Integration Suggestions**: Daily note linking recommendations
4. **Learning Path**: Structured understanding approach