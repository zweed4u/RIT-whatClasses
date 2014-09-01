#Zachary Weeden
#@zweed4u  display for RIT MyCourses 
#Tested on Python 2.6.6 

import mechanize
import urllib
import cookielib
from bs4 import BeautifulSoup
import html2text
import re
import sys
import StringIO
import getpass
from easygui import passwordbox

try:
    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)


    br.set_handle_gzip(False)


    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Chrome')]

    # The site we will navigate into, handling it's session
    br.open('https://mycourses.rit.edu/')

    # Inspect name of the form
    '''
    for f in br.forms():
        print f
    '''
    # Select the second (index one) form - the first form is a search query box
    br.select_form(nr=0)





    # User credentials
    #####HANDLE LOGIN CHECKING#####



    print "               ___  __             __   __   ___  __  __ "
    print "|  | |__|  /\   |  /  ` |     /\  /__` /__` |__  /__`  _|"
    print "|/\| |  | /~~\  |  \__, |___ /~~\ .__/ .__/ |___ .__/  . "

    print "                 __          __       ___  ___  __   / |     " 
    print "                |__) \ / .    / |  | |__  |__  |  \ /__| |  |"
    print "                |__)  |  .   /_ |/\| |___ |___ |__/    | \__/"
    print "\n"                                                                                                                                     




    username = raw_input("Username: ")
    print "Password: "
    password = passwordbox("Password: ")

    #password = getpass.getpass() #-> echos pass with IDLE
    #password = raw_input("Password: ") -> echos pass


    br.form['username'] = username
    br.form['password'] = password


    # Login
    br.submit()









    #Prints html of main page after login
    #print(br.open('https://mycourses.rit.edu/d2l/lp/ouHome/defaultHome.d2l').read()) 


    regex = '<a class="vui-link vui-outline d2l-link d2l-left" href="(.+?)" title="(.+?)">(.+?)</a>'
    pattern = re.compile(regex)





    ###USE IN WHILE LOOP TO PRINT OUT STR
    ###PROMPT USER FOR HOW MANY CLASSES&&LABS ARE TAKEN AND USE THAT AS COUNTER VAR RATHER THAN i

    htmltext = br.open('https://mycourses.rit.edu/d2l/lp/ouHome/defaultHome.d2l').read()
    classes = re.findall(pattern,htmltext)

    noClass = int(input("How Many Classes/Labs/Recitations are taken? "))
    print "\n"


    i=0
    while i < noClass:   # 9 classes/labs
        className = str(classes[i]).split("', '")[2]
        className = str(className).split("')")[0]
        print "Class " + str(i+1) + ": " + className + "\n"
        i+=1

    '''
    print str(classes[1]).split(', ')[2]
    print "\n"
    print str(classes[2]).split(', ')[2]
    print "\n"
    print str(classes[3]).split(', ')[2]
    print "\n"

    print str(classes[4]).split(', ')[2]
    print "\n"
    print str(classes[5]).split(', ')[2]
    print "\n"
    print str(classes[6]).split(', ')[2]
    print "\n"
    print str(classes[7]).split(', ')[2]
    print "\n"
    print str(classes[8]).split(', ')[2]
    print "\n"
    '''
except:
    print "~~~Exception Thrown! Most likely incorrect login credentials.~~~"

