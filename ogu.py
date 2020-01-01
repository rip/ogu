''' OGU AUTOBUMPER PROTOTYPE V.0
may code a fully featured and cross-platform
(run on any device or in the cloud!)
version although this is functional...
just a req l00p'''

thread_ID_2bump = 'Edit This' # thread id

mybbuser = 'Edit This' # auth cookie

my_post_key = 'Edit This' # found in request // todo: pull from cookie above but this is just an example

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

from requests import post
from time import sleep

while True:
	post('https://ogusers.com/newreply.php', cookies={'mybbuser': mybbuser}, data=data)
	sleep(3600) # bump every x seconds (default: 3600)
