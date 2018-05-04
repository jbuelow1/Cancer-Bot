#!/bin/bash
while true; do
  killall python3
  git pull
  python3 main.py >> log.log
  sleep 30m
done
