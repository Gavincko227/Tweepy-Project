from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from selenium import webdriver
import time
import urllib
import urllib2
import csv
import json
import ast
import csv_html
import tweepy, datetime, time
from datetime import datetime
from pytz import timezone    
import filterbykeywordwatson as watson
#import watson_message_dialouge as watsonmessage
import threading
import collecting_tweet
toronto = timezone('Canada/Eastern')
tor_time = datetime.now(toronto)
print tor_time.strftime('%Y-%m-%d_%H-%M-%S')
#Variables that contain the user credentials to access Twitter API
import ibm_watson


consumer_key = "Cr23jDeibBZXbEbw5gWcjGBlM"
consumer_secret = "wprCArOI7HqgiB49U2byOYyTl6O3anKvZHhFFpXMIPbl6ozWJb"
access_token = "209015814-OT8ivQSDLxapOO6htCRT46ipZWVJowjL6BaVoFjE"
access_token_secret = "16QE6QmZkMxv682647PZEOfzV2sqaxOZoelzySJzUfuG3"

function = False
# def watsonmessage():
	# service=ibm_watson.AssistantV1(
    # version='2019-02-28',
    # iam_apikey='rHPoGMbSy7JGmQh3-nMKSSY7AbTeQ6PMh8i18DPaQdZb',
    # url='https://gateway.watsonplatform.net/assistant/api'
	# )

	# input = raw_input()
	# response = service.message(
		# workspace_id='9874ed31-4034-444a-9a9a-f1607c806801',
		# input={
			# 'text': input
		# }
	# ).get_result()
	# csv_html("#"+response['intents'][0]['intent']+".csv")

def datetime_from_utc_to_local(utc_datetime):
	now_timestamp = time.time()
	offset = datetime.datetime.fromtimestamp(now_timestamp) - datetime.datetime.utcfromtimestamp(now_timestamp)
	return utc_datetime + offset






def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data
### TWITTER CLIENT ###
class TwitterClient():
	def __init__(self, twitter_user=None): # None defaults to user timeline if nothing is given 
		self.auth = TwitterAuthenticator(). authenticate_twitter_app()
		self.twitter_client = API(self.auth)
		self.twitter_user = twitter_user
	def get_tweets(self, num_tweets):
		tweets = []
		for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
			tweets.append(tweet)
		return tweets
		
	# def get_friend_list(self, num_friends):
		# friend_list = []
		# fpr friend in Cursor(self.twitt
 
	

### TWITTER AUTHENTICATOR ###
class TwitterAuthenticator():
	def authenticate_twitter_app(self):
		# Creating the authentication object
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		# Setting your access token and secret
		auth.set_access_token(access_token, access_token_secret)
		return(auth)
		
	
class TwitterStreamer():
	'''
	Class fpr streaming and processing live tweets
	'''
	def _init_(self):
		self.twitter_autenticator = TwitterAuthenticator() #the authenticator
	def stream_tweets(self, fetched_tweets_filename, datacollectionfile, hash_tag_list, driver, handles_list):
		self.twitter_autenticator = TwitterAuthenticator() #the authenticator for stream 
		#This handles Twitter authentication and the connection to the Twitter Streaming API
		listener = TwitterListener(fetched_tweets_filename, datacollectionfile,driver,handles_list) #creates the listener method in class TwitterListener
		auth = self.twitter_autenticator.authenticate_twitter_app() #gets the necessary authenication
		# # Creating the API object while passing in auth information
		# api = tweepy.API(auth) 
		stream = Stream(auth, listener) #streames to the listerner class
		# while(function==False):
			# # watsonmessage.watsoninput()
			# # self.driver.refresh()
			
			# print("This is the beginnning")
			# if (function==True):
				# break
		# This line filter Twitter Streams to capture data by the keywords
		#stream.filter(follow= hash_tag_list, location=)
		stream.filter(follow=hash_tag_list)
		# watsonmessage.watsoninput()
				# #hash_tag_list is the array of user_id that were passed and therefore follow those users
		# #watsonmessage()
		# # import watson_message_dialouge as watsonmessage
		# driver.refresh()
		
		
### TWITTER STREAM LISTENER ###		
class TwitterListener(StreamListener): #inherit from stream listener class which methods that we can override
	'''
	Basic listener class that just prints received tweets to stdout.
	'''
	

	def __init__(self, fetched_tweets_filename, datacollectionfile,driver, handles_list):
		self.fetched_tweets_filename = fetched_tweets_filename
		self.datacollectionfile = datacollectionfile
		self.driver = driver
		self.handles_list = handles_list
		function=False
		# while(function==False):
			# # watsonmessage.watsoninput()
			# # self.driver.refresh()
			# print("This is the beginnning")
	def on_data(self, data):
		#pass
		# if 'screen_name' in data:
			# print("it went in the loop")
			# status = Status.parse(self.api, json.loads(data))
			# if self.on_status(status) is False:
				# return False
		function=True
		print("True")
		try:
			#below is the checks to see which type of data
			print(data) #the entire tweet
			print(dir(data)) #the tweet directores like user name or time
			print(type(data)) # the type is unicode 
			print("\n")
			data1 = json_loads_byteified(data) #convert normal tweet to json format (unicode to dict)
			
			print(data1)     # do the same process
			print(type(data1)) #the json format is type of dict
			print("\n")
			print(data1.keys()) # the keys are the different conetents tweet has to 
			print("\n")
	
			# for key, value in data1.iteritems():
				# print key, value
			#data2 = json.loads(data1)
			# data1 = json.dumps(data, sort_keys=True, separators=(',', ':'))
			# print(type(data1))
			# print("\n")
			# print(data1)
			#print(type(data2))
			# json1_data = json_loads_byteified(data)
			# print(json1_data)
			# print("\n")
			# print(type(json1_data))
			# print(json1_data.keys())
			# dictdata = ast.literal_eval(repr(data))
			
			# print(dictdata)
			# print(type(dictdata))
			
			# dictdatadump = json_loads_byteified(json.dumps(data, sort_keys=True, separators=(',', ':')))
			# print("\n")
			# print(dictdatadump)
			# print(type(dictdatadump))
		# printta2 = json_loads_byteified(data1)
		# pri(json1_data.keys())
		#print(data2.keys())
		# print("\n")
		
		#print (data2.keys())
		
			toronto = timezone('Canada/Eastern') #establish timezone
			data1["created_at"] = datetime.now(toronto) #get the current date time in toronto since it can be twitter uses GMT time
			print tor_time.strftime('%Y-%m-%d_%H-%M-%S') #check to see if the time and date is formatted correctly
				
			with open(self.fetched_tweets_filename, 'w') as tf, open(self.datacollectionfile, 'a') as dcf:  #open all_tweet.csv to append
				writertf = csv.writer(tf)
				writerdcf = csv.writer(dcf)
				#created_date_local = datetime_from_utc_to_local(data1["created_at"])
				'''
				this is how the tweet is split into its different contents to write into the file
				'''
				writedata = [data1["user"]["name"], data1["id_str"], data1["created_at"].strftime('%Y-%m-%d %H:%M:%S'), data1["text"]]
				#writedata = [dictdatadump["user"], dictdatadump["id_str"], dictdatadump["created_at"], dictdatadump["text"]]
				
				#writertf.writerows([writedata])
				writertf.writerow(["User Name","tweet_id","created_at","Tweet_text"]) #writes the first row as four colums using writer method	
				writerdcf.writerows([writedata])
				
				for handles in self.handles_list:
					collecting_tweet.get_all_tweets(handles, writertf)
				
			csv_html.pandas(self.fetched_tweets_filename)
			csv_html.pandas(self.datacollectionfile)
			csv_html.indexhtml('sortedall_tweets.csv')
			#driver = webdriver.Chrome()
			#driver.get("file:///C:/Users/Gavincko/Documents/Tweepy%20Project/python/templates/table.html")
			# while True:
				# time.sleep(5)
			self.driver.refresh()
			
			# watsonmessage.watsoninput()
			# self.driver.refresh()
			'''
			driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
			driver.get("/Users/Gavincko/Documents/Tweepy Project/python/table.html")
			while True:
				time.sleep(5)
				driver.refresh()
		'''
			watson.textanalysis(data1["text"])
		except BaseException as e:
			print("Error on data: %s" % str(e))
		
		return(True)
			
	def on_error(self, status):
		#pass
		if status == 420:
			# Returning False on_data method in case rate limit occurs
			return False
		print(status)

	
		
	#def watsonmessage(self):
		# service=ibm_watson.AssistantV1(
		# version='2019-02-28',
		# iam_apikey='rHPoGMbSy7JGmQh3-nMKSSY7AbTeQ6PMh8i18DPaQdZb',
		# url='https://gateway.watsonplatform.net/assistant/api'
		# )

		# input = raw_input()
		# response = service.message(
			# workspace_id='9874ed31-4034-444a-9a9a-f1607c806801',
			# input={
				# 'text': input
			# }
		# ).get_result()

		# print(json.dumps(response, indent=2))
		# print(type(response))
		# print(response.keys())
		# #print(len(response['intents'][0]))
		# csv_html(response['intents'][0]['intent']+".csv")
		# self.driver.refresh()
		

if __name__ == "__main__":
	print('hello')