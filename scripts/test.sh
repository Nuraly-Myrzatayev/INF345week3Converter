#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../src"

python3 server.py&
#i ran server in background to test it
#then i save it's PID
LASTPID=$!
python3 test.py
kill $LASTPID #And destroy it =)
