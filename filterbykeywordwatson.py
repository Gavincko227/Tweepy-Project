'''
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, RelationsOptions, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='18f34dtBi11noHcG4UES1unofJeGWrewAolawgJQudp9',
    url= 'https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-11-16rl'
	)

response = natural_language_understanding.analyze(
    # text='There is a rainstorm tonight in toronto',
    # features=Features(relations=RelationsOptions())).get_result()
    url='www.ryerson.ca',
    features=Features(categories=CategoriesOptions(limit=3))).get_result()

	
	
print(json.dumps(response, indent=2))

'''
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions
import ast
import streamingcollectingtweet as streaming
import collecting_tweet
#import createintent
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='18f34dtBi11noHcG4UES1unofJeGWrewAolawgJQudp9',
    url= 'https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-11-16rl'
	)

def jsonformat(input_json):
	# # Transform json input to python objects
	# input_dict = json.loads(input_json)

	# # Filter python objects with list comprehensions
	# output_dict = [x for x in input_dict if ['keywords'] == '#StCatharines']

	# # Transform python object back into json
	# output_json = json.dumps(output_dict)

	# # Show json
	# print output_json
	print(type(input_json))
	input_json = streaming.json_loads_byteified(input_json)
	print(type(input_json))
	print(input_json.keys())
	for i in range(0, len(input_json["keywords"])):
		#collecting_tweet.filter(input_json["keywords"][i]["text"], "sorteddatacollection.csv")
		collecting_tweet.filter(input_json["keywords"][i]["text"], "sorteddatacollection.csv") #should be the same file as entities
		#createintent.createintent(input_json["entities"][i]["text"])
	for i in range(0, len(input_json["entities"])):	
		#collecting_tweet.filter(input_json["entities"][i]["text"], "sortedall_tweets.csv")
		collecting_tweet.filter(input_json["entities"][i]["text"], "sorteddatacollection.csv")
		#createintent.createintent(input_json["entities"][i]["text"])



def textanalysis(tweet):
	response = natural_language_understanding.analyze(
		text=tweet,
		features=Features(
			entities=EntitiesOptions(emotion=True, sentiment=True, limit=4),
			keywords=KeywordsOptions(emotion=True, sentiment=True,
									 limit=4))).get_result()

	jsonformat(json.dumps(response, indent=2))
	print(json.dumps(response, indent=2))


if __name__ == '__main__':
	textanalysis('COLLISION: #Hwy406 SB at Westchester #StCatharines: All lanes blocked. #OPP, @SC_FireServices & @NiagaraEMS  on scene. ')