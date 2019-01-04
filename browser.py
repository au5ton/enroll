#!/usr/bin/env python

import mechanize
br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
#br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]

response = br.open("https://howdy.tamu.edu")

print( response.read())
