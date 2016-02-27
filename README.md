# JAVIS-Telegram-Bot

This is a telegram bot called J.A.V.I.S. It stands for Just A Very Intelligent System. JAVIS helps to monitor and update master of the network status.

If you are using the code, the following need to be modified for the program to run.

1) Fill in JAVIS master telegram ID
- MASTER_ID = [MASTER TELEGRAM ID ]
  
2) Location of rsync  backup file
- bkupcmd = "cat /home/username/share/rsync_bk.log | grep SGT | tail -n 5" 
