---
author: Andrew Hoyt
date: December 14th, 2025
paging: Slide %d / %d
---

# Direnv

## Andrew Hoyt

Direnv is a environment variable manager for your shell. Automatically load
your environment when you enter a directory.

---

## What does it do

Direnv allows you to automatically load environemnt variables when you enter
a directory. It works with by executing bash commands and exporting environment
varaibles. It uses an `.envrc` file to define the environment.

---

## Example Direnv

```bash
# .envrc

export FOO=bar

# Any arbitrary bash can be executed in your .envrc file. In this example I am
# loading a secret value from the pass password manager tool.
SECRET=$(pass secret)
export SECRET

# Direnv also includes a bash standard library. For example you can add a directory
# dynamically to your path with PATH_add
# For example, you can preprend a python virtual environment, overriding the system
# version of python on your path
export VIRTUAL_ENV="$PWD/.venv"
PATH_add "$VIRTUAL_ENV/bin"
```

---

## Code example

In addition to this presentation there is a simple echo web server written
in FastAPI in `main.py` and a client in `client.py`. The environemnt
is already loaded so no need to use `uv run` or `source .venv/bin/activate`.
This is all handled automatically by direnv.
