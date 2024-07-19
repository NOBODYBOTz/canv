#!/bin/sh

# Run health check server in the background
python health_check.py &

# Start the bot
exec python -m Assistant.__main__
