
import os
import aiml
from subprocess import call
from datetime import date, timedelta
import webbrowser as wb

#BRAIN_FILE="brain.dump"

k = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml fileswhat was t
# and saves the brain dump.
#if os.path.exists(BRAIN_FILE):
 #   print "Loading from brain file: " + BRAIN_FILE
   # print "wait for few seconds"
    #k.loadBrain(BRAIN_FILE)
#else:
#print "Parsing aiml files"

k.bootstrap(learnFiles="std-startupt.aiml", commands="load aiml b")

    #print "Saving brain file: " + BRAIN_FILE
   # k.saveBrain(BRAIN_FILE)

# Endless loop which passes the input to the bot and prints
# its response
count=0
user_name=input("unga peru enna:>")
print ("NiKu:> Vada {}".format(user_name))
#call(["espeak",("hello {}".format(user_name))])

while True:  
	  #count +=1
	    #if count is 1:

    about = ["who are you", "who created you", "what is your name", "name", "about you"]
    what_can_i_do = "hey iam chatbot \n and i can draw(just say:Draw) \n i do math(just say:calculate) " \
                    "\n i play youtube(just say youtube) \n i can search (just say:search) \n you can talk with 	me by entering your message "
    #ssk = ["do you know ssk", "who is ssk", "who is SSK", " do you know  sanjay", "do you know  sanjaykhanssk",
          # "do you know sanjaykhan", "who is sanjay"]
    empty= []

    user_input = input("{}> ".format(user_name))


    more_than_chat = user_input.split(" ")
        #more_than_chat = user_input
    if user_input is "what can you do":
        print("NiKu:>" + what_can_i_do)
        #call(["espeak",(what_can_i_do)])
        continue
    if user_input in empty:
        print("NiKu:>" +"He created me")
        #call(["espeak",(what_can_i_do)])
        continue


    elif user_input in about:
        answers = "thanks for asking,\n iam ssk's brain power N project chatbot \n My Name is NiKu ;)"
        print("NiKu:>" + answers)
        #call(["espeak",(answers)])
        continue
    elif "youtube" in more_than_chat[0]:

        more_than_chat.remove(more_than_chat[0])
        query = '+'.join(more_than_chat)
        link = ("https://www.youtube.com/results?search_query={}".format(query))
        #call(["espeak",("opening web browser")])
        wb.open(link)
        continue
    elif "search" in more_than_chat[0]:
        more_than_chat.remove(more_than_chat[0])
        query = '+'.join(more_than_chat)
        link = (
            "https://www.google.co.in/search?dcr=0&source=hp&ei=r0CBWtjaOYPlvgSnpIuQCw&q={}".format(query))
        #call(["espeak",("opening web browser")])
        wb.open(link)
        continue

    else:
            ai_output = k.respond(user_input)
            print("NiKu:>" + ai_output)
            #call(["espeak",(ai_output)])




