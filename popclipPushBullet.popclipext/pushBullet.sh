#!/bin/bash

#curl -u v1y4FbR0BkrrZCmHglY4ilcTu8drdT06Jaujv5YkwfcyW: https://api.pushbullet.com/api/devices
selectText=$POPCLIP_TEXT
pushbody='drafts://x-callback-url/create?text='`\"$selectText\"`
postdate=`date +%H:%M+"$POPCLIP_TEXT"`
curl https://api.pushbullet.com/api/pushes \
      -u v1y4FbR0BkrrZCmHglY4ilcTu8drdT06Jaujv5YkwfcyW: \
      -d device_iden=ujv5YkwfcyWdjzWIEVDzOK \
      -d type=note \
      -d title=$postdate \
      -d body=$pushbody \
      -X POST
