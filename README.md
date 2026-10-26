# jo-cli

> **A fast, budget-flexible, terminal-first AI agent for developers.**  
> Built as the foundational CLI execution interface for the **Project Josephine** ecosystem.

---

## ⚡ What is jo-cli?

`jo-cli` is a terminal-first coding assistant and workflow runner designed as a lightweight, cost-controlled alternative to Claude Code. 

Instead of locking you into a single proprietary ecosystem or recurring monthly seat subscription, `jo-cli` gives you complete autonomy over your models and inference costs. Bring your own Hugging Face or OpenAI-compatible provider token, choose the exact model suited for your workload (from Qwen 2.5 Coder to DeepSeek V3), and execute code edits, bash commands, and system diagnostics right inside your repository.

Under the hood, `jo-cli` shares the same core engine that powers the **jo-cloud** desktop tray and the offline **josephine** runtime.

---

## 🚀 Key Features

* **Bring-Your-Own-Key (BYOK):** Seamless integration with Hugging Face Serverless / Dedicated Inference, OpenRouter, and standard OpenAI-compatible endpoints.
* **Deterministic Tool Execution:** Built on Josephine's Phase 1 execution architecture. Code editing, process inspection, shell dispatching, and hardware telemetry execute deterministically without runtime lockups.
* **Granular Diff & Patching:** Inspect, read, and write multi-line targeted file diffs directly inside git repositories.
* **Zero UI Overhead:** Pure terminal interface powered by `rich` streaming. Sub-millisecond startup, zero GUI thread lag, and clean standard I/O streaming.
* **Dual Execution Modes:** Interactive REPL mode for conversational iterative development, and single-shot execution mode for fast shell piping.

---
## 🛠️ Usage

### 1. Interactive REPL (Default)
Launch an interactive agent session directly inside your project repository:

```bash
cd my-web-app/
jo
```

Inside the interactive session, prompt the agent to inspect files, edit functions, run tests, or debug errors:

```text
╭─ jo-cli v0.1.0 ─────────────────────────────────────────────────────────────╮
│ Model: Qwen/Qwen2.5-Coder-32B-Instruct                                      │
│ Workspace: /home/user/projects/my-web-app                                   │
╰─────────────────────────────────────────────────────────────────────────────╯

jo > inspect src/server.ts and fix the uncaught exception on route /api/checkout
```

### 2. Single-Shot Command Execution
Pipe shell commands or run quick direct fixes without entering the interactive shell:

```bash
# One-shot instruction
jo "run git status and explain why the build failed in tests/"

# Pipe logs or errors straight to jo-cli
npm test 2>&1 | jo "diagnose this stack trace and propose a diff"
```

---

## 🧩 Architectural Position

`jo-cli` is Part 1 of the 3-tier **Project Josephine** ecosystem:

```text
┌──────────────────────────────────────────────────────────┐
│              Josephine Core Engine Layer                 │
│    (Deterministic Tools, Event Streaming, Context)      │
└──────────────┬──────────────────┬─────────────────┬──────┘
               ▼                  ▼                 ▼
          [ jo-cli ]         [ jo-cloud ]      [ josephine ]
      Terminal-First CLI     System Tray HUD   Fully Offline
      (Hugging Face / BYOK)  (Cloud / Voice)   (Local llama.cpp)
```

1. **`jo-cli`**: The terminal-first workbench for developers and feature testing.
2. **`jo-cloud`**: The persistent background desktop assistant with system tray integration and voice communication.
3. **`josephine`**: The sovereign, fully local desktop assistant powered by an embedded local LLM.

---

## 📄 License

Distributed under the Apache 2.0 / MIT License. See `LICENSE` for details.