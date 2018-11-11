import praw
import time
bot = praw.Reddit(user_agent='HungryMothBot',client_id='Lf1RYS-DToojdQ', client_secret='beINITOxMTltT3hZQubyIS-aclY',username='HungryMothWantsLamp', password='GiveMeThatLamp')

subreddit = bot.subreddit('popular')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    time.sleep(.1);
    if (' lamp' in text.lower()) or ('light source' in text.lower()) or ("glowing" in text.lower()):
        # Generate a message
        message = "https://imgur.com/gallery/pJVKB2f I am hungry." 
	print(text)
        comment.reply(message) # Send message
	time.sleep(1)
    else:
    	print("Nope!")
