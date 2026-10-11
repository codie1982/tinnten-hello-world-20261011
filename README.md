# Tinnten Hello World

A small public project for testing Tinnten's Git import, OpenCode development,
live progress, clean verification, and review flow.

## Python

```sh
python3 hello.py Ada
python3 -m unittest discover -v
```

## Node.js

```sh
node hello.mjs Ada
npm ci --ignore-scripts
npm test
```

Both implementations print `Hello, Ada!`. The project has no third-party
dependencies. Python uses its standard library; Node.js uses its built-in test
runner. Dependency versions and system tools are provided by the worker profile.

Changes made by a Tinnten coding task are reviewed separately from this repository's
initial publication. A coding task does not automatically push changes to GitHub.
