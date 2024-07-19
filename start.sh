#!/bin/sh

# Run health check server in the background
python web.py &

# Start the bot
exec python -m Assistant.__main__
