#!/usr/bin/env bash
set -euo pipefail
#i've been encountering error about python not seeing /<projectFolder>/../src/server.py
#this made me realise the file could try and run from anywhere, so while this cd is really not necessary,
#i think it is not pedantic for me if i add this anyway
#btw $0 is the current filename so run.sh, so this line
#is forcing anything to get redirected where we can run server.py
cd "$(dirname "$0")/../src"

python3 server.py
