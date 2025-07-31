# TreeQuest Framework

## Overview

TreeQuest is Sakana AI's breakthrough framework that achieves ==collective superintelligence== through coordinated multi-agent collaboration using different language models as coordinated "dream teams." The framework extends Monte Carlo Tree Search (MCTS) with ==Adaptive Branching Multi-LLM coordination== (AB-MCTS), enabling dynamic LLM selection and superior performance compared to single-model approaches.

> [!info] Paradigm Shift
> TreeQuest represents a fundamental shift from scaling individual models to orchestrating collective intelligence through multi-agent coordination, achieving **30% performance improvements** over individual LLM baselines.

## Key Concepts

- **AB-MCTS Algorithm**: Multi-LLM Adaptive Branching Monte Carlo Tree Search extending AlphaGo's MCTS approach
- **Dynamic LLM Selection**: Multi-armed bandit algorithms for adaptive model assignment during search
- **Collective Intelligence**: Leveraging diverse model biases as "precious resources" rather than eliminating them
- **Three-Dimensional Search**: Exploration across depth (refinement), width (generation), and model dimensions
- **Inference-Time Scaling**: Computational resources applied during inference rather than training

## Applications & Use Cases

### **Complex Algorithmic Problem Solving**
- Multi-step programming challenges requiring iterative refinement
- ==ARC-AGI-2 benchmark== showing ==30% improvement== over repeated sampling baselines
- Tasks requiring trial-and-error approaches with adaptive learning

> [!success] Performance Breakthrough
> TreeQuest achieved **>30% success rate** on ARC-AGI-2 benchmark with **19.2% pass@2 metric**, significantly outperforming individual model baselines at **23% success rate**.

### **Enterprise Multi-Provider Strategy**
- Dynamic leverage of multiple frontier models without vendor lock-in
- Task-specific optimization using the right AI for each subtask
- Cost optimization through efficient resource allocation across model capabilities

### **ML Model Optimization**
- Improving accuracy of existing models through collective intelligence
- Software performance optimization with ensemble approaches
- Real-time model selection based on task performance

## Recent Developments

### **2024 Open Source Release**
Released in ==June 2024== under ==Apache 2.0 license== enabling commercial use, with full implementation available on GitHub.

> [!tip] Technical Specifications
> - **Language**: Python 3.11+ required
> - **Installation**: `pip install "treequest[abmcts-m]"`
> - **Algorithms**: AB-MCTS-A (Aggregation) and AB-MCTS-M (Mixed Models)

### **Benchmark Performance Results**
Extensive validation on ==ARC-AGI-2 benchmark== with ==120 test problems==:

| Approach | Success Rate | Key Insight |
|----------|-------------|------------|
| Repeated Sampling Baseline | ==23%== | Individual model limit |
| AB-MCTS with o4-mini | ==27.5%== | Single model with search |
| **Multi-LLM AB-MCTS** | **>30%** | **Collective intelligence advantage** |

> [!note] Experimental Configuration
> Testing used **o4-mini, Gemini 2.5 Pro, DeepSeek-R1** with maximum **250 LLM calls per problem** and reward functions based on correctly solved demonstration cases.

### **Technical Architecture Evolution**
- **Thompson Sampling**: Probabilistic exploration direction decisions
- **Multi-Armed Bandit**: Adaptive LLM selection optimization
- **Checkpointing**: Recovery capabilities for long-running tasks
- **State Aggregation**: Combining insights from multiple model responses

## Related Topics

- [[advanced-event-driven-architecture]] - Asynchronous coordination patterns for multi-agent systems
- [[autogen-framework]] - Microsoft's alternative approach to multi-agent coordination
- [[Multi-Agent Systems]] - Broader context of coordinated AI agent approaches
- [[Monte Carlo Methods]] - Foundational search algorithms extended by TreeQuest
- [[Ensemble Learning]] - Machine learning approach to combining multiple models

> [!info] Framework Comparison
> Unlike **AutoGen** (conversational agents) or **CrewAI** (hierarchical teams), TreeQuest focuses on **dynamic multi-LLM coordination** with adaptive model selection during search processes.

## Learning Resources

### **Official Documentation**
- [Sakana AI TreeQuest GitHub](https://github.com/SakanaAI/treequest) - Complete open-source implementation
- [Research Paper: "Inference-Time Scaling and Collective Intelligence"](https://sakana.ai/ab-mcts/) - Technical foundation and methodology
- [Sakana AI Company Blog](https://sakana.ai/ab-mcts/) - Implementation guidance and use cases

### **Implementation Examples**
```python
# Core TreeQuest API Pattern
from treequest import ABMCTSA, top_k

algo = ABMCTSA()  # Adaptive Branching MCTS with Aggregation
search_tree = algo.init_tree()

# Multi-LLM coordination through flexible generation functions
for iteration in range(max_iterations):
    search_tree = algo.step(search_tree, {'Action': generate_function})
```

### **Integration Patterns**
- **ML Pipeline Integration**: Custom generation functions for domain-specific applications
- **Event-Driven Compatibility**: Checkpointing for fault-tolerant execution
- **Microservices Architecture**: Modular LLM service orchestration

> [!warning] Implementation Considerations
> - **Cost Implications**: Requires access to multiple frontier LLMs
> - **Complexity Fit**: Best suited for complex, multi-step problems requiring iterative refinement
> - **Resource Management**: Maximum 250 LLM calls per problem in benchmark configuration

## Performance Metrics

### **Core Benchmarks**
- **ARC-AGI-2 Success Rate**: ==30%+ improvement== over individual model baselines
- **Search Efficiency**: Maximum ==250 LLM calls per problem== with intelligent resource allocation
- **Model Diversity**: Validated across ==o4-mini, Gemini 2.5 Pro, DeepSeek-R1==

> [!success] Collective Intelligence Evidence
> Ensemble approach solved **over 30% of test problems** - "far ahead of any individual models on their own," demonstrating genuine collective superintelligence emergence.

### **Technical Advantages**
- **Model Agnostic**: Works with any combination of frontier LLMs
- **Adaptive Intelligence**: Real-time optimization of model selection strategies
- **Fault Tolerance**: Checkpointing enables recovery from API errors
- **Scalable Architecture**: Designed for enterprise deployment patterns

## Critical Success Factors

> [!tip] Key Design Principles
> 1. **Diversity as Strength**: Leverages different model biases rather than eliminating them
> 2. **Dynamic Adaptation**: Real-time model selection based on task performance  
> 3. **Inference-Time Intelligence**: Computational scaling during use rather than training

### **Research Significance**
TreeQuest demonstrates that ==coordinated multi-agent systems can achieve superior performance== compared to individual state-of-the-art models, opening new avenues for practical collective superintelligence applications in enterprise environments.

## Tags
#multi-agent-systems #collective-intelligence #sakana-ai #monte-carlo-tree-search #llm-coordination #inference-scaling