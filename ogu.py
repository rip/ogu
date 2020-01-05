''' OGU AUTOBUMPER PROTOTYPE version 0.1 
may code a fully featured and cross-platform
(run on any device or in the cloud!)
version although this is functional...
just a req l00p'''

thread_ID_2bump = 'EDITxTHISxWITHxYOURS' # thread id

mybbuser = 'EDITxTHISxWITHxYOURS' # auth cookie

my_post_key = 'EDITxTHISxWITHxYOURS' # found in source html or request
'''
todo: automatically obtain
(along with other input variables other than
thread url to bump, in non-prototype version)
'''

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
from datetime import datetime as clock

while True:
	post('https://ogusers.com/newreply.php', cookies={'mybbuser': mybbuser}, data=data)
	time = clock.now().strftime('%I:%M%p')
	print(f'({time}) bumped https://ogusers.com/showthread.php?tid={thread_ID_2bump}')
	sleep(3600)
	# bumps every 3600 seconds
