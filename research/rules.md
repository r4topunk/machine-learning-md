# Research Rules and Methodology

## Purpose
This document establishes standardized rules for conducting research on machine learning topics, discovering similar content, and creating meaningful connections within the Obsidian second brain system.

## Research Workflow

### 1. Topic Discovery Process
Before researching a new topic:
1. **Search Existing Content**: Use Obsidian search to find related topics in daily notes
2. **Check News Archives**: Review `/news/` folder for relevant AI agent developments
3. **Identify Gaps**: Determine what aspects haven't been covered yet
4. **Plan Connections**: Note potential links to existing content

### 2. Research Agent Instructions

#### For ML/AI Topics (General)
```
Research the topic "[TOPIC_NAME]" for second brain reference:
1. Core concept explanation (clear but not overly technical)
2. Why it matters and key applications (3-4 main use cases)
3. Recent developments worth knowing (2024-2025)
4. How it connects to other topics in ML/AI
5. Essential learning resources (3-5 quality sources)

Aim for comprehensive understanding without excessive detail. Focus on practical knowledge and meaningful connections. Avoid deep mathematical derivations or extensive subtopic branching.

IMPORTANT: When creating research files, ALWAYS use Obsidian formatting for better readability:
- Use ==highlights== for key concepts, metrics, dates, and critical information
- Add callouts for important context:
  - > [!warning] for risks and critical challenges
  - > [!danger] for immediate threats or failures
  - > [!info] for important background context
  - > [!note] for key insights and observations
  - > [!tip] for best practices and recommendations
- Highlight specific numbers, percentages, and technical metrics
- Use callouts to break up dense text and emphasize crucial points
```

#### For AI Agents Specifically
Use the existing `/news/rules.md` template for agent-focused research.

### 3. Content Integration Strategy

#### Creating Connections
1. **Backlink Strategy**: Use `[[Topic Name]]` format for connecting related concepts
2. **Tag System**: Apply consistent tags like `#neural-networks`, `#agents`, `#frameworks`
3. **Cross-References**: Add "Related Topics" sections in research notes
4. **Temporal Linking**: Connect concepts that build upon each other chronologically

#### File Organization
- **Research Notes**: Store in `/research/topic-name.md` format
- **Daily Integration**: Reference research in daily notes with links
- **Update Existing**: Enhance previous daily notes with new connections discovered

### 4. Second Brain Connection Framework

#### Discovery Methods
1. **Keyword Search**: Use Obsidian's search for concept overlap
2. **Graph View**: Visualize connections between topics
3. **Tag Exploration**: Find related content through shared tags
4. **Chronological Review**: Identify how topics evolved over time in daily notes

#### Connection Types
- **Foundational**: Basic concepts that support advanced topics
- **Evolutionary**: How topics develop and improve over time
- **Complementary**: Topics that work together or solve similar problems
- **Contrasting**: Different approaches to similar challenges

### 5. Quality Standards

#### Research Depth
- **Primary Sources**: Link to original papers, documentation, official sites
- **Multiple Perspectives**: Include various viewpoints and approaches
- **Current Relevance**: Focus on 2024-2025 developments when possible
- **Educational Value**: Prioritize learning and understanding over news

#### Connection Quality
- **Meaningful Links**: Only connect topics with genuine relationships
- **Bi-directional**: Ensure connections work both ways conceptually
- **Context Explanation**: Briefly explain why topics are connected
- **Progressive Building**: Connect simpler concepts to more complex ones

## Research Templates

### Topic Research Template
```markdown
# [Topic Name]

## Overview
Clear explanation of what this is and why it matters (2-3 sentences). Use ==highlights== for key concepts.

> [!note] Key Insight
> Add important context or insight about the topic here.

## Key Concepts
- **Core concept 1**: brief explanation with ==highlighted== key terms
- **Core concept 2**: brief explanation with ==highlighted== key terms
- **Core concept 3**: brief explanation with ==highlighted== key terms

## Applications & Use Cases
- **Primary application**: context and examples
- **Secondary application**: context and examples
- **Emerging use case**: potential and significance

## Recent Developments
Notable advances or changes in 2024-2025

> [!info] Current State
> Brief callout about the current state or recent developments.

## Related Topics
- [[Foundational Topic]] - how it connects
- [[Related Technology]] - relationship
- [[Advanced Application]] - how it builds

## Learning Resources
- [Primary Documentation](URL) - what it covers
- [Tutorial/Course](URL) - learning approach
- [Research Paper](URL) - key insights

## Tags
#domain #technology #application-area
```

### Connection Discovery Template
```markdown
# Connection Analysis: [Topic A] ↔ [Topic B]

## Relationship Type
[Foundational/Evolutionary/Complementary/Contrasting]

## Connection Points
- Shared concept 1
- Shared concept 2
- Technical overlap

## Learning Sequence
Which should be understood first and why

## Combined Applications
How these topics work together in practice

## Cross-References
- Daily notes mentioning both topics
- Research files covering intersection
```

## Usage Guidelines

### When to Create Research Files
- Complex topics requiring deep exploration
- Subjects spanning multiple daily notes
- Concepts with many interconnections
- Topics needing structured learning paths

### When to Use Daily Notes Only
- Simple resource sharing
- Single video or article discussion
- Brief updates or news items
- Casual learning observations

### Connection Discovery Triggers
- Encountering similar terminology across topics
- Finding repeated authors or researchers
- Noticing shared mathematical foundations
- Identifying common application domains
- Discovering overlapping implementation approaches

## Integration with Existing System

### With Daily Notes
- Reference research files in daily notes using `[[research/topic-name]]`
- Create daily entries that build upon research foundations
- Use research files as "index pages" for scattered daily content

### With News System
- Connect AI agent news to broader ML research topics
- Reference news developments in topic research files
- Use news insights to update and expand research content

### With Obsidian Features
- **Graph View**: Visualize topic relationships and clusters
- **Search**: Find hidden connections across all content
- **Tags**: Create topic hierarchies and category systems
- **Backlinks**: Track which content references each research topic