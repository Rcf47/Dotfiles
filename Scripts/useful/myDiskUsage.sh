#!/bin/bash

echo "Disk usage over 80%:"
df -h | awk '$5+0 > 80 {print}'
