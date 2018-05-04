#!/bin/bash
while true; do
  echo "killing proscess and re-starting..."
  killall python3
  git pull
  python3 main.py >> log.log
  sleep 30m
done
