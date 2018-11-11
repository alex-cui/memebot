import praw
bot = praw.Reddit(user_agent='HungryMothBot',
		  client_id='Lf1RYS-DToojdQ',
		  client_secret='beINITOxMTltT3hZQubyIS-aclY',
		  username='HungryMothWantsLamp', 
		  password='GiveMeThatLamp')

subreddit = bot.subreddit('popular')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if 'Moth' or 'moth' in text.lower():
        # Generate a message
        message = "".format(author) 

        comment.reply(message) # Send message
