#!/bin/bash

python3 shitgut.py words.txt  mailysaily.txt
cat mailysaily.txt


OUTPUT_FILE="mailysaily.txt"
SALAD=$(cat "$OUTPUT_FILE")
USER=$( ./pairer.sh)
str="$USER"
MAIL="${str%%:*}"
echo "$MAIL"   


curl --ssl-reqd \
  --url 'smtps://smtp.gmail.com:465' \
  --user "$USER" \
  --mail-from "$MAIL" \
  --mail-rcpt 'youraddress@gmail.com' \
  -T <(printf "Subject: SALADIN\n\n%s" "$SALAD")
