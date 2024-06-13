#!/bin/bash
json_file=$(python _scripts/upload_grid.py)
git add .
commit_message="chore: added $json_file"
git commit -m "$commit_message"
git push
