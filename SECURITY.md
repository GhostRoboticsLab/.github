# Security policy

This is the default security policy for every GhostLabs (`GhostRoboticsLab`) repository that does not ship its own `SECURITY.md`. A repository's own policy (for example Hackagotchi or Hermes) takes precedence over this one.

## Reporting a vulnerability

Please do not open a public issue for a security problem.

- **Public repositories:** use GitHub's private vulnerability reporting (**Security → Report a vulnerability** on the repository) where it is enabled.
- **Otherwise, and for private repositories you have access to:** email **ghostlabsoftware@gmail.com** with `[security]` in the subject.

A useful report names the repository and commit, the affected files, what an attacker can do, and how to reproduce it. A proof of concept helps; please avoid destructive tests against live services or other people's data.

We will acknowledge your report and keep you informed while it is being fixed. GhostLabs does not run a bug bounty program.

## Scope

Anything shipped from a GhostLabs repository: application code, firmware images, build tooling, GitHub Actions workflows, and infrastructure configuration published here. Issues in third-party dependencies belong upstream; tell us as well if a GhostLabs project is affected.

## Supported versions

Only the default branch and the latest release of each repository receive security fixes.
