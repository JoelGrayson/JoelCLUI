#!/bin/bash

echo "-----Update pyproject.toml's version-----"
echo -n "Old version: "
grep version < ./pyproject.toml | sed -E 's/^version ?= ?\"(.*)\"$/\1/'
echo -n "New version: "
read -r new_version
sed "s/^version = .*$/version = \"$new_version\"/" pyproject.toml > temp
cat temp > pyproject.toml
rm temp

echo "-----Build-----"
rm -rf dist
rm -rf src/joelclui.egg-info
python3 -m build
twine upload dist/*
