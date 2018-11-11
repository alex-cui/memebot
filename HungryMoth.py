import praw
user_agent = ("I am a hungry moth ")
r = praw.Reddit(user_agent=user_agent)
thing_limit = 10
user_name = "HungryMothWantsLamp"
user = r.get_redittor(user_name)

