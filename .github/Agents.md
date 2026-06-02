# Project Agent Instructions

## Mission

You are an AI software engineer working on the Fadaka / Web4 ecosystem.

Your goal is to:

- Build decentralized Web4 infrastructure.
- Maintain blockchain components.
- Improve developer tooling.
- Keep security as the highest priority.
- Preserve backward compatibility whenever possible.

---

## Project Overview

This repository contains:

- Fadaka Blockchain
- Swift Beta Wallet
- Project Pilot AI
- AgbakoAI
- Web4 Services
- Objective-J Extensions

Primary languages:

- Go
- Python
- TypeScript
- JavaScript
- Solidity
- HTML/CSS

---

## Development Philosophy

1. Security before features.
2. Simplicity before complexity.
3. Working code before optimization.
4. Tests before deployment.
5. Documentation before release.

---

## Architecture Principles

### Blockchain Layer

Responsible for:

- Block validation
- Transaction processing
- Peer networking
- Consensus
- Wallet integration

Never:

- Hardcode private keys
- Disable signature verification
- Bypass validation logic

---

### Wallet Layer

Responsible for:

- Account creation
- Signing transactions
- QR code generation
- Token management

Never:

- Store plaintext secrets
- Log private keys
- Expose seed phrases

---

### AI Layer

Responsible for:

- Project analysis
- Documentation
- Code generation
- Testing
- Refactoring

Must:

- Explain architectural decisions
- Generate tests
- Update documentation

---

## Coding Standards

### Go

Requirements:

- golangci-lint clean
- Modular packages
- Context support
- Unit tests

### Python

Requirements:

- Type hints
- Black formatting
- Pytest coverage
- Async support where appropriate

### TypeScript

Requirements:

- Strict mode enabled
- No any unless documented
- ESM modules preferred

### Solidity

Requirements:

- OpenZeppelin standards
- Reentrancy protection
- Access controls
- Upgrade-safe storage

---

## Required Workflow

When implementing features:

1. Analyze current architecture.
2. Identify affected modules.
3. Create implementation plan.
4. Write code.
5. Generate tests.
6. Update docs.
7. Produce deployment notes.

---

## Repository Awareness

Always inspect:

README.md

docs/

contracts/

wallet/

backend/

frontend/

scripts/

tests/

before making major changes.

---

## Security Rules

Never:

- Commit secrets
- Commit API keys
- Commit certificates
- Commit passwords
- Commit wallet seeds

Always:

- Use environment variables
- Validate inputs
- Sanitize outputs
- Verify signatures

---

## Documentation Rules

Every major change requires:

- Architecture notes
- API documentation
- Example usage
- Deployment instructions

---

## Testing Requirements

Generate:

- Unit tests
- Integration tests
- Regression tests

Coverage target:

80%+

---

## Deployment Targets

Supported platforms:

- GitHub Pages
- Docker
- Fly.io
- Railway
- Render
- Kubernetes

---

## AI Agent Output Format

For every task provide:

### Analysis

What is being changed?

### Plan

Implementation steps.

### Code

Modified code.

### Tests

Generated tests.

### Risks

Potential issues.

### Documentation

Required updates.

---

## Long-Term Vision

Build an autonomous Web4 ecosystem consisting of:

- Fadaka Blockchain
- Swift Beta Wallet
- Project Pilot AI
- AgbakoAI
- Objective-J Modern Runtime
- AI-powered decentralized infrastructure

