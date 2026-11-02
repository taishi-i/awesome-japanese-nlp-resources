# Security Policy

## Supported Versions

This repository is a curated list plus the `awesome-japanese-nlp-resources` plugin for Claude Code and Codex. Only the latest version on the `main` branch (and the latest released plugin version) receives security fixes.

| Version | Supported |
| --- | --- |
| `main` / latest plugin version | :white_check_mark: |
| Older plugin versions | :x: |

If you use the plugin, update it to the latest version before reporting:

```shell
/plugin update awesome-japanese-nlp-resources@awesome-japanese-nlp-resources
```

## Scope

**In scope**

- The plugin under [`plugins/awesome-japanese-nlp-resources/`](plugins/awesome-japanese-nlp-resources/): skills (`SKILL.md`), Python scripts, bundled data, and plugin manifests (`.claude-plugin/`, `.codex-plugin/`), plus the marketplace manifests at the repository root (`.claude-plugin/`, `.agents/`)
  - e.g. a script that can be made to read or write files outside its intended scope, execute arbitrary commands, or leak data
  - e.g. skill instructions or bundled data that could cause an agent to perform unintended actions (prompt injection)
- Links in this list that point to malicious content, such as a repository, model, or dataset that has been hijacked, taken over after a rename, or replaced with malware

**Out of scope**

- Vulnerabilities in third-party projects listed here. Please report those directly to the maintainers of the project concerned.
- Vulnerabilities in Claude Code, Codex, GitHub, or Hugging Face themselves. Please report those to the respective vendors.

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues, pull requests, or discussions.**

Instead, report them privately via GitHub's [private vulnerability reporting](https://github.com/taishi-i/awesome-japanese-nlp-resources/security/advisories/new) ("Security" tab → "Report a vulnerability").

Please include as much of the following as you can:

- A description of the issue and its potential impact
- The affected file(s), skill, or list entry
- Steps to reproduce (agent used — Claude Code or Codex — plugin version, and the prompt or command)
- Any suggested fix, if you have one

For a listed link that is merely broken or outdated (not malicious), a regular issue or pull request is fine.

## What to Expect

- We aim to acknowledge your report within 24 hours.
- We will keep you informed of our progress and let you know when the issue is fixed.
- Malicious links will be removed from the list as soon as they are confirmed.
- With your permission, we will credit you in the fix or advisory.

Thank you for helping keep this project and its users safe.
