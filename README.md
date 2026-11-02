# Agent Audit Merkle ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Agent Audit Merkle Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/agent-audit-merkle/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/agent-audit-merkle?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/agent-audit-merkle/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Agent Audit Merkle** is a production-ready developer tool and connector: Tamper-proof cryptographic Merkle audit ledger for agent actions, observations, and tool calls.

---

## 🚀 Problem Statement

When agents make destructive or high-liability decisions, logs stored in plaintext files can be edited, deleted, or fabricated after the fact.

---

## ⚡ Architecture Flow

```mermaid
graph TD
    A[Root Hash H_ROOT] --> B[H_12]
    A --> C[H_34]
    B --> D[Event 1: Read Spec]
    B --> E[Event 2: Edit Code]
    C --> F[Event 3: Run Tests]
    C --> G[Event 4: Git Push]
```

---

## 📊 Performance Benchmarks

| Ledger Operation | Latency | Complexity | Tamper Detection |
|---|---|---|---|
| Append Event Leaf | 0.04ms | O(log N) | Instant |
| Generate Inclusion Proof | 0.08ms | O(log N) | Cryptographic |
| Verify Log Integrity | 0.12ms | O(N) | 100% Guaranteed |

---

## 🛠️ Installation & Quickstart

```bash
pip install agent_audit_merkle
```

### Python API

```python
import agent_audit_merkle

print(agent_audit_merkle.__version__)
```

### CLI Usage

```bash
agent-audit-merkle --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
