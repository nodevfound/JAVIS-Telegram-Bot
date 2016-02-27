#!/usr/bin/python

import subprocess
import sys
import time
import telepot
import signal
import datetime

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)
    try:
        if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exit_gracefully)

def log_location(x,y):
    now = datetime.datetime.now()
    with open("javis_location_track.log", "a") as f:
    	f.write(now.strftime("%d/%m/%Y-%H:%M") + "|" + "latitude:" + x + " longitude:" + y + "\n")

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print content_type, chat_type, chat_id

    if chat_id == MASTER_ID:
	if content_type == "text":
		if msg['text'].lower() == "wru": 
    			bot.sendMessage(chat_id, 'JAVIS Here!')
		elif msg['text'].lower() == "backup":
			proc = subprocess.Popen(bkupcmd, stdout=subprocess.PIPE, shell=True)
			(out, err) = proc.communicate()
			bot.sendMessage(chat_id, out)
        	elif msg['text'].lower() == "pubip":
                	proc = subprocess.Popen(ipcmd, stdout=subprocess.PIPE, shell=True)
                	(out, err) = proc.communicate()
                	bot.sendMessage(chat_id, out)
		elif msg['text'].lower() == "help":
			bot.sendMessage(chat_id, '[wru] [backup] [pubip] [help]')
    	elif content_type == "location":
		log_location(str(msg['location']['latitude']), str(msg['location']['longitude']))
		print "Latitude:" + str(msg['location']['latitude']) + " Longitude:" + str(msg['location']['longitude'])
	else:
		bot.sendMessage(chat_id, 'You are not my master')


if __name__ == '__main__':
    TOKEN = [BOT_TOKEN]
    MASTER_ID = [MASTER TOKEN that can talk to this bot]
    THREE_HRS = 10800

    bkupcmd = "cat /home/username/share/rsync_bk.log | grep SGT | tail -n 5"
    ipcmd = "cat wanip.config"

   # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)

    bot = telepot.Bot(TOKEN)
    bot.notifyOnMessage(handle)
    print 'Listening ...'

    # Keep the program running.
    while 1:
    	time.sleep(THREE_HRS)
    	bot.sendMessage(MASTER_ID, 'JAVIS is Alive !')
