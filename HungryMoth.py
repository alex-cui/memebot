import praw
import time

#define class Meme
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

#create and define Meme objects
lampMoth = Meme([],"https://imgur.com/gallery/pJVKB2f I am hungry.", "Lamp/Moth")
lampMoth.addTerm(" lightbulb ")
lampMoth.addTerm(" bright ")
lampMoth.addTerm(" lamp ")
lampMoth.addTerm(" light source ")
lampMoth.addTerm(" glowing ")

shrekDonkey = Meme([], "https://66.media.tumblr.com/1e2f561f44d85b1219fd4008ea843578/tumblr_mvc7jbak6Q1sm2yoxo4_250.gif Donkey!!!", "Shrek/Donkey")
shrekDonkey.addTerm(" ogres ")
shrekDonkey.addTerm(" onions ")
shrekDonkey.addTerm(" layers ")
shrekDonkey.addTerm(" parfait ")
shrekDonkey.addTerm(" donkey ")

Memes = [lampMoth, shrekDonkey]

bot = praw.Reddit(user_agent='HungryMothBot',client_id='Lf1RYS-DToojdQ', client_secret='beINITOxMTltT3hZQubyIS-aclY',username='HungryMothWantsLamp', password='GiveMeThatLamp')

subreddit = bot.subreddit('popular')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    time.sleep(.01)
    for i in Memes:
        for j in i.terms:
            if j in text.lower() and author != "HungryMothWantsLamp":
                print(i.name, ' was found')
                time.sleep(1) #set to 600 for 10 min
                #comment.reply(i.respond()) # Send message
