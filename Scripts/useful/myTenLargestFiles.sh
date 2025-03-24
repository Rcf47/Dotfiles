#!/bin/bash

echo "Ten largest files please wait:"
find / -type f -exec du -h {} + 2> /dev/null | sort -rh | head -10
