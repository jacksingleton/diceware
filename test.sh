#!/usr/bin/env bash

set -euo pipefail

wordlist=$(cat 20k-most-common-google.list)
diceware=$(echo "$wordlist" | ./wordlist-to-diceware.py)
num_uniq_words=$(echo "$diceware" | cut -d' ' -f2 | sort | uniq | wc -l)

if [ $num_uniq_words -eq "7776" ]; then
  printf "\e[32m" # green
  echo 'Pass!'
  printf "\e[0m" # end green
  exit 0
else
  printf "\e[31m" # red
  echo 'Fail!' >&2
  printf "\e[0m" # end red
  echo 'Did not generate 7776 unique words!' >&2
  echo "Got $num_uniq_words" >&2
  exit 1
fi
