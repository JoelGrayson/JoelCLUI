#!/bin/bash

rm -rf dist
rm -rf src/joelclui.egg-info
python3 -m build
twine upload dist/*
