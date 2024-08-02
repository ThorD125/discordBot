#!/bin/bash

pipreqs --encoding utf-8 --force
git status
git add .
git commit -m "update"
git push
