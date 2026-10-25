#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../src"

#kill the server before starting in case our server is already running in the background
pkill -f server240107075.py || true

python3 server240107075.py&
#i ran server in background to test it
#then i save it's PID
LASTPID=$!
python3 test.py
kill $LASTPID #And destroy it =)
