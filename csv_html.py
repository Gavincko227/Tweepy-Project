from prettytable import PrettyTable
from selenium import webdriver
import time
import urllib
import urllib2
import pandas as pd
import os
import re

x = PrettyTable()

def html_code(line):
		line = line.split(',') #splits the csv line into different objects.
		#x.add_row([line[0], line[1], line[2], line[3], line[4], line[5]])
		try:
			x.add_row([line[0], line[1], line[2], line[3]])# that split line is added to the different columns.
		except:
			print("line did not work")
		#x.add_row([line[0], line[1], line[2])
		#        for i in range (0, len(line)):
#               x.add_row([line[i]])
     





def indexhtml(file):

	#os.remove('table.html')
	re.sub("<.*?>:", " ", "table.html") # subs any obsscure characters with a space.
	csv_file = open(file, 'r') #opens the sorted file  
	csv_file = csv_file.readlines()# reads the sorted.csv file

	row_count =  sum(1 for row in csv_file) #counts the number of rows 
	print(row_count, "\n\n\n\n") #just a check
	print(sum)
	
	x.clear_rows() #clear the rows that were previously in x ( prettutable 
	fieldnames = csv_file[0].split(',') #spliting the csv file by the comma or else one straight line
	
	x.field_names = [fieldnames[0], fieldnames[1], fieldnames[2], fieldnames[3]] #number of columns that is to be views
	
	for i in range (1, row_count): #iterates through every row
			
			line = csv_file[i] #assings each row to variable line
			print(line)
			line.split(',')
			# print(line[0], line[1], line[2], line[3])
			html_code(line)
			
			# try:
				# html_code(line) #calls the html_code funtion and passes the csv file to add it to x which
			# except IndexError:
				# continue
			
	html_string = x.get_html_string() #gets the html string method from the library for the rows in x (the table)
	html_file = open('/Tweepy-Project/htmltemplates/htmltable.html', 'w') #table.html is opened to write
	html_file = html_file.write(html_string) # and the html string is written to the html file
	#tabs = []
	'''
	driver = webdriver.Chrome()
	driver.get("file:///C:/Users/Gavincko/Documents/Tweepy%20Project/python/templates/table.html")
	while True:
		time.sleep(5)
		driver.refresh()
	'''	
	

def pandas(file):
	df = pd.read_csv(file, delimiter=',') #reads the file "all_tweets.csv" that was passed and splits it by the comma, making a dataframe
	
	df = df.sort_values(['tweet_id'], ascending=[False])#sorts the values from highest tweet_id to lowest.
	
	df.drop_duplicates(subset=None, inplace=True)
	df.to_csv('sorted' + file, index=False, encoding='utf-8')#puts that dataframe into a csv file called sorted, more organized


if __name__ == '__main__':
	print ("hello")
















'''
import pandas as pd

columns = ['age', 'week', 'opp', 'ACscr', 'OPPscr', 'location']
df = pd.read_csv('all_tweets.csv', names=columns)

# This you can change it to whatever you want to get
age_15 = df[df['age'] == 'U15']
# Other examples:
bye = df[df['opp'] == 'Bye']
crushed_team = df[df['ACscr'] == '0']
crushed_visitor = df[df['OPPscr'] == '0']
# Play with this

# Use the .to_html() to get your table in html
print(crushed_visitor.to_html())
'''




















'''

from prettytable import PrettyTable

csv_file = open('/Users/Gavincko/Documents/Tweepy Project/python/all_tweets.csv', 'r')
csv_file = csv_file.readlines()
print csv_file[1]
x = PrettyTable()
#x.field_names = csv_file[0]

seperate = []
print len(csv_file)

for i in range(0, len(csv_file[0])):
    line = csv_file[i].split(',')
    for a in range(0,len(line)):
        x.addrow()
    







for i in range(0, len(csv_file)):
    line = csv_file[i].split(',')
    for a in range(0, len(line)):
        print line[a]

line_1 = csv_file[0]
line_1 = line_1.split(',')
#line_2 = csv_file[1]
#line_2 = line_2.split(',')
print line_1, #line_2
x = PrettyTable([line_1[0]])
for a in range(1, len(line_1)):
    x.add_column([line_1[a]])
html_code = x.get_html_string()
html_file = open('/Users/Gavincko/Documents/Tweepy Project/python/table.html', 'w')
html_file = html_file.write(html_code)

'''




