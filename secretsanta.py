##############################################################
#
####     Secret Friend: 
# "Christmas tradition in which members of a group or community are randomly 
# assigned a person to whom they anonymously give a gift" by wikipedia
#
# Copyright 2013 Margarida Carvalho
#
# Licensed under the terms of GNU GENERAL PUBLIC LICENSE.
# http://www.gnu.org/licenses/gpl.html
#
##############################################################

# random function that we will use
from random import sample

# Import smtplib for the actual sending function
import smtplib

# Import the email modules
from email.mime.text import MIMEText

def SecretFriend(emails):
	n = len(emails)
	if n ==1:
		print("No SecretFriend is possible")
		return 0
	else:
		friends = sample(range(n),n)
		for i in range(n):
			if friends[i]==i:
				friends[i] = friends[(i+1)%n]
				friends[(i+1)%n] = i
		# start sending emails
		for i in range(n):
			msg = MIMEText("Your secret friend is "+emails[friends[i]])
			msg['Subject'] = 'Secret Friend'
			me = 'referee@decision' # fixed email
			you = emails[i]
			msg['From'] = me
			msg['To'] = you
			s = smtplib.SMTP('localhost')
			s.sendmail(me, [you], msg.as_string())
			s.quit()
		# end sending emails
		return 0

# example
emails = ["friend1@com","friend2@net","friend3@org"]
SecretFriend(emails)
