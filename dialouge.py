import json
import ibm_watson
import csv_html
import collecting_tweet
from selenium import webdriver
import speech_recognition as sr
import pyaudio
import sys
from Tkinter import *
import ScrolledText as tkst
import csv
import watson_message_dialouge  as message
import collecting_tweet


def messageft(txt, txt1, driver, service):
	print("It should've came")
	r = sr.Recognizer()
	while(True):
		with sr.Microphone() as source: #activating the microphone
			print('Speak anythin')  #checking if the microphone is working
			txt.delete(1.0, END)
			txt.insert(INSERT, 'Say "Hey Compass" to start filteration')  #checking if the microphone is working
			
			try:
				audio = r.listen(source, timeout=2, phrase_time_limit=4)  #2 seconds to say something and then 4 seconds to say a phrase
				input = r.recognize_google(audio) #the voice input from the user 
			except:
				# root1.mainloop()
				continue
			txt1.delete(1.0, END)
			txt1.insert(INSERT, "You said : {}".format(input))#just checks what the out put is on the command prompt 
			
			if input == "hey compass" or input=='a compass' or input=="he compass" or input=="compass" or input=="encompass" or input=="j campus" or input==" compass": #checks if the input someone closley resembles hey compass
				'''
				now into the filtering part
				'''
				txt1.delete(1.0, END)
				txt1.insert(INSERT, "You said : {}".format(input))#just checks what the out put is on the command prompt 
				 
				while (True):  #code below is going to keep running until it is stopped through voice input
		#input = raw_input()
					
					try:	
						print("go ahead I'm listening")
						#txt.delete(1.0, END)
						txt.delete(1.0, END)
						txt.insert(INSERT, "go ahead I'm listening")  #checking if the microphone is working
						audio=r.listen(source, timeout=5, phrase_time_limit=5) #same code as before to econgnize what the user input is
						tointent = r.recognize_google(audio) #the recognized part is labelled tointent - this is the variable that is to be used
						print("You said : {}".format(tointent))
						txt1.delete(1.0, END)
						txt1.insert(INSERT, "You said : {}".format(tointent))
					except:
						print("Sorry could not recognize what you said try again") #if there is an error it would try again
						txt.delete(1.0, END)
						txt.insert(INSERT, "Sorry could not recognize what you said try again")						
						continue   #try again part
					if tointent == "quit":  #if user says quit it will break from the while loop and end the filtration part
						print("You are leaving the filtration program")
						txt.delete(1.0, END)
						txt.insert(INSERT, "You are leaving the filtration program")
						for i in range(0,1000):
							continue
						break  #will end the while loop and go through the intial loop to enable filteration system
						
					elif tointent == "close the program": #if the input is "close the program"
						print("closing")
						txt.delete(1.0, END)
						txt.insert(INSERT, "closing")						
						sys.exit() #Entire program shuts down
						
					#this is part is to get the intent based on the input	
					response = service.message(
						workspace_id='9874ed31-4034-444a-9a9a-f1607c806801',
						input={
							'text': tointent
						}
					).get_result() #this creates a sort of json output which we have to access the intents.
					
					try:
						if (response['intents'][0]['intent'] == 'sortedall_tweets' or response['intents'][0]['intent'] == 'EnvCanada'): #if these return then we can open these files
							csv_html.indexhtml(response['intents'][0]['intent']+".csv") #send these files to be converted to html page
							# root1.mainloop()
							driver.refresh() #refresh the driver so wepage is displayed
							
						elif(response['intents'][0]['intent'] == 'activeweather'):
							firstline = True
							weathertweets = []
							activeweathertweets = []
							with open("sorteddatacollection.csv") as csv_file: 
								csv_reader = csv.reader(csv_file, delimiter=',') #need to remove the entire row!!
								for row in csv_reader:  
									if firstline:
										firstline=False
										print(firstline)
										continue
									if 'EnvCanada' in row[3]: #if cleared is is not in the tweet column then store it
										
										weathertweets.append(row) #stored in cleaned rows
							print(weathertweets)
							activeweathertweets = collecting_tweet.onlyissued(weathertweets)
							print(activeweathertweets)
							with open("activeweather.csv", 'w') as csv_file: #open a new file to store the tweets with only"cleared tweets"
								csv_writer = csv.writer(csv_file)
								csv_writer.writerow(["User Name","tweet_id","created_at","Tweet_text"])
								csv_writer.writerows(activeweathertweets)  #write the tweets without cleared into the file
							csv_html.pandas("activeweather.csv") #format the file using pandas
							csv_html.indexhtml("sortedactiveweather.csv") #convert the formatted file to html
							# root1.mainloop()
							driver.refresh() #refresh the webpage							
							
						elif(response['intents'][0]['intent'] == 'activecollisions'):
							firstline = True
							collisionstweets = []
							activecollisiontweets = []
							with open("sorteddatacollection.csv") as csv_file: 
								csv_reader = csv.reader(csv_file, delimiter=',') #need to remove the entire row!!
								for row in csv_reader:  
									if firstline:
										firstline=False
										print(firstline)
										continue
									if 'EnvCanada' not in row[3]: #if cleared is is not in the tweet column then store it
										
										collisionstweets.append(row) #stored in cleaned rows
							print(collisionstweets)
							activecollisionstweets = collecting_tweet.onlycollisions(collisionstweets)
							print(activecollisionstweets)
							with open("activecollisions.csv", 'w') as csv_file: #open a new file to store the tweets with only"cleared tweets"
								csv_writer = csv.writer(csv_file)
								csv_writer.writerow(["User Name","tweet_id","created_at","Tweet_text"])
								csv_writer.writerows(activecollisionstweets)  #write the tweets without cleared into the file
							csv_html.pandas("activecollisions.csv") #format the file using pandas
							csv_html.indexhtml("sortedactivecollisions.csv") #convert the formatted file to html
							# root1.mainloop()
							driver.refresh() #refresh the webpage							
							
						
						
						#if the user says "cleared" in the input for a certain highway
						elif  " cleared " in tointent or "cleared " in tointent or " cleared" in tointent:
							print("#"+response['intents'][0]['intent']+".csv")
							
							print("ITS IN THE ELIFF")
							#all the intents are with files with hashtags, the hashtag must be added first
							collecting_tweet.filter('CLEARED', "#"+response['intents'][0]['intent']+".csv") #filter all tweets with cleared colllsions to a separate csv file.
							csv_html.indexhtml("CLEARED.csv") #convert that csv file to html page to display
							# root1.mainloop()
							driver.refresh() #refresh the file
						

						#all this is to get only collision tweets
						elif " collisions " in tointent or " collision " in tointent or "Collision " in tointent: #if only collision said for a specfic ighway
							print("This is collisions")
							# collecting_tweet.filter("COLLISION", "#"+response['intents'][0]['intent']+".csv")
							clean_rows=[]
						
							firstline = True
							#opens the file with the intennt, since all the intents are with files with hashtags, the hashtag must be added first
							print("u'#"+response['intents'][0]['intent']+".csv")
							with open("#"+response['intents'][0]['intent']+".csv") as csv_file: #
								csv_reader = csv.reader(csv_file, delimiter=',') #need to remove the entire row!!
								for row in csv_reader:  
									if firstline:
										firstline=False
										print(firstline)
										continue
									if 'CLEARED' not in row[3]: #if cleared is is not in the tweet column then store it
										clean_rows.append(row) #stored in cleaned rows
										print(row)
								# csv_file.truncate()			
							with open("onlycollision.csv", 'w') as csv_file: #open a new file to store the tweets with only"cleared tweets"
								csv_writer = csv.writer(csv_file)
								csv_writer.writerow(["User Name","tweet_id","created_at","Tweet_text"])
								csv_writer.writerows(clean_rows)  #write the tweets without cleared into the file
							csv_html.pandas("onlycollision.csv") #format the file using pandas
							csv_html.indexhtml("sortedonlycollision.csv") #convert the formatted file to html
							# root1.mainloop()
							driver.refresh() #refresh the webpage
							
										
						else:	
							#hashtag is what all the intents that were created
							csv_html.indexhtml("#"+response['intents'][0]['intent']+".csv") #if cleared or collsion is not asked in  input display the file with all the contents 
							print("It prints this")
							# root1.mainloop()
							driver.refresh() #refresh the webpage
					except Exception as e:
						print("No intents created for the verbal input") #if no intents are created for this
						print(e)
						# root1.mainloop()
			elif input == "close the program" or input == "stop the program" or input=="Thats enough": #input to quit the program 
				print "closing"
				txt.delete(1.0, END)
				txt.insert(INSERT, "closing")						
				sys.exit() #Entire program shuts down
			else:
				# root1.mainloop()
				print("continue")
				continue #keeps contninuing
			

if __name__ == "__main__":
	print("This is useless")