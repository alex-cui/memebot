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
    if ' lamp ' in text.lower() and comment.author.name != "HungryMothWantsLamp":
        # Generate a message
        message = "https://imgur.com/gallery/pJVKB2f I am hungry." 

        comment.reply(message) # Send message
	time.sleep(1)
