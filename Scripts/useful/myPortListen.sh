#!/bin/bash

echo "Listening ports:"
netstat -tulpn | grep LISTEN
