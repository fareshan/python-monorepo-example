#!/usr/bin/env bash
#
# Builds (or rebuilds) the sandbox of a library. Run as:
#
# ./$(git rev-parse --show-toplevel)/scripts/rebuilds-sandbox.sh
#
# in any library directory. You likely want to source the sandbox in your
# shell after having called this script. Do it with:
#
# source .venv/bin/activate

set -x # This will print each command to the standard error before executing it, which is useful for debugging scripts.

rm -Rf ".venv"
python3 -m venv .venv
source .venv/bin/activate
pip install -r $(git rev-parse --show-toplevel)/pip-requirements.txt
pip install -r $(git rev-parse --show-toplevel)/dev-requirements.txt -r requirements.txt
