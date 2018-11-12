import praw
import time

class Meme:
    #constructor (ignore self its needed for syntax)
    def __init__(self, terms, response, name):
        self.terms = []
        self.response = response
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
lampMoth.addTerm(" moon ")
lampMoth.addTerm(" glowing ")

shrekDonkey = Meme([], "https://66.media.tumblr.com/1e2f561f44d85b1219fd4008ea843578/tumblr_mvc7jbak6Q1sm2yoxo4_250.gif", "Shrek")
shrekDonkey.addTerm(" ogres ")
shrekDonkey.addTerm(" onions ")
shrekDonkey.addTerm(" layers ")
shrekDonkey.addTerm(" parfait ")

pikachuWow = Meme([], "https://www.dailydot.com/wp-content/uploads/2018/10/surprisedpikachu.jpg", "Pikachu/Wow")
pikachuWow.addTerm(" wow ")
pikachuWow.addTerm(" pikachu ")
pikachuWow.addTerm(" ash ")
pikachuWow.addTerm(" ketchup ")

Memes = [lampMoth, shrekDonkey, pikachuWow]

bot = praw.Reddit(user_agent='HungryMothBot',
                  client_id='Lf1RYS-DToojdQ', 
                  client_secret='beINITOxMTltT3hZQubyIS-aclY',
                  username='HungryMothWantsLamp', 
                  password='GiveMeThatLamp')

subreddit = bot.subreddit('popular')

comments = subreddit.stream.comments()

moveOn = False
desired_meme_num = -1

while(not moveOn):
    print("\nMeme List:")
    for x in Memes:
        print("    " + x.name)
        
    print("\nWhat number meme do you want to auto-reply to?")
    desired_meme_num = int(input())
    if desired_meme_num > -1 and desired_meme_num < len(Memes):
	    moveOn = True    

print("\nSearching...")

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author

    for key in Memes[desired_meme_num].terms:
        if key in text.lower():
                print("Success!")
                comment.reply(Memes[desired_meme_num].respond()) # Send message
                time.sleep(1)
