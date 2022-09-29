#!/bin/bash

# Note: Update pyproject.toml's version before running build

rm -rf dist
rm -rf src/joelclui.egg-info
python3 -m build
twine upload dist/*
