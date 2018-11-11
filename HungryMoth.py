import praw # simple interface to the reddit API, also handles rate limiting of requests

bot = praw.Reddit(user_agent='I am a hungry moth',
                  client_id='MothBot',
                  client_secret='',
                  username='HungryMothWantsLamp',
                  password='')

subreddit = bot.subreddit('popular')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if 'Moth' or 'moth' in text.lower():
        # Generate a message
        message = "".format(author) 

        comment.reply(message) # Send message
