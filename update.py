import praw

reddit = praw.Reddit(client_id='tVM2iiNWzJ3pdg',
                     client_secret='uRXNcSwJU8-8n2opv29KKO7QPMw',
                     password='',
                     user_agent='Updating Dota 2 Stylesheet',
                     username='VRCkid')

sub = reddit.subreddit('VRCkid')
stylesheet = dota.stylesheet

with open('stylesheet.css.mini', 'r') as m:
	newSheet = m.read()
	stylesheet.update(newSheet)