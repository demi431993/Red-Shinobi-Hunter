# Red-Shinobi-Hunter

Red-Shinobi-Hunter is an authorized defensive security assessment toolkit focused on controlled reconnaissance, exposure validation, and detection-engineering workflows.

## Current capabilities

- HTTP/HTTPS target normalization and validation
- Controlled HEAD probing with timeout handling
- Structured JSON or human-readable results
- Configurable request pacing
- Optional pacing jitter behind an explicit `--stealth` switch
- Target-count limits to reduce accidental scope expansion
- Automated pytest CI

## Install

```bash
python -m pip install -e ".[test]"
```

## Example

```bash
red-shinobi-hunter https://example.com --json
```

For controlled pacing during an authorized assessment:

```bash
red-shinobi-hunter https://example.com --stealth --jitter-min 0.2 --jitter-max 0.8
```

## Scope and safety

Use this project only against systems you own or have explicit authorization to assess. The stealth switch controls assessment pacing/jitter; it is not a security-control bypass and does not provide persistence, credential theft, payload delivery, rootkit installation, or malware evasion.

## Roadmap

The repository is intentionally starting with a small, testable core. Planned defensive modules can be added incrementally for asset inventory, HTTP security-header analysis, TLS posture checks, evidence collection, reporting, and detection-oriented telemetry.
