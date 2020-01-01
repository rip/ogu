''' OGU AUTOBUMPER PROTOTYPE V.0
may code a fully featured and cross-platform
(run on any device or in the cloud!)
version although this is functional...
just a req l00p'''

from time import sleep
from requests import post

thread_ID_2bump = ''

mybbuser = '' # auth cookie

cookies = {'mybbuser': mybbuser}

my_post_key = '' # found in request // todo: pull from cookie but this is just an example

data = {
'my_post_key': my_post_key,
'subject': '',
'action': 'do_newreply',
'posthash': '',
'quoted_ids': '',
'lastpid': '',
'from_page': '1',
'tid': thread_ID_2bump, 
'method': 'quickreply',
'message': '🦎🦎🦎🦎🦎🦎🦎🦎🦎🦎', # message
'postoptions[signature]': '1' # toggle sig
}

while True:
	post('https://ogusers.com/newreply.php', cookies=cookies, data=data)
	sleep(3600) # bump every x seconds (default: 3600)
