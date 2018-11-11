import praw
import time

class Meme:
    
    def __init__(self, terms, response, name):
    	self.response = response
	self.terms = []
	self.name = name

    def addTerm(self, term):
    	self.terms.append(term)

    def setResponse(self, res):
    	self.response = res
	
    def respond(self):
    	return self.response
    
lampMoth = Meme([],"https://imgur.com/gallery/pJVKB2f I am hungry.", "Lamp/Moth")
lampMoth.addTerm(" lightbulb ")
lampMoth.addTerm(" bright ")
lampMoth.addTerm(" lamp ")
lampMoth.addTerm("light source")
lampMoth.addTerm(" glowing ")
#lampMoth.setResponse("https://imgur.com/gallery/pJVKB2f I am hungry.")

shrekDonkey = Meme([], "https://66.media.tumblr.com/1e2f561f44d85b1219fd4008ea843578/tumblr_mvc7jbak6Q1sm2yoxo4_250.gif", "Shrek/Donkey")
#shrekDonkey.setResponse("https://66.media.tumblr.com/1e2f561f44d85b1219fd4008ea843578/tumblr_mvc7jbak6Q1sm2yoxo4_250.gif")
shrekDonkey.addTerm(" ogres ")
shrekDonkey.addTerm(" onions ")
shrekDonkey.addTerm(" layers ")
shrekDonkey.addTerm(" parfait ")

Memes = [lampMoth, shrekDonkey]


bot = praw.Reddit(user_agent='HungryMothBot',client_id='Lf1RYS-DToojdQ', client_secret='beINITOxMTltT3hZQubyIS-aclY',username='HungryMothWantsLamp', password='GiveMeThatLamp')

subreddit = bot.subreddit('popular')

comments = subreddit.stream.comments()

moveOn = False
desired_meme_num = -1
while( not moveOn):
	print("Meme List:")
	for meme in Memes:
		print(meme.name)

	print("What number meme do you want to auto-reply to? ")
	desired_meme_num = input();
	if desired_meme_num > -1 and desired_meme_num < len(Memes):
	    moveOn = True    

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    time.sleep(.01)
    for key in Memes[desired_meme_num].terms: 
	if key in text.lower():
           #comment.reply(Memes[desired_meme_num].respond()) # Send message
	    time.sleep(1)
    else:
    	print("Nope!")

