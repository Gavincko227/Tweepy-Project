import tkinter as tk
import tkinter.messagebox
import sys
from tkinter import scrolledtext
import collecting_tweet
import tweepy, datetime, time
TorontoList = ['OPP_GTATraffic', 'Gavincko', 'ECAlertON143']
BarrieList = ['opp4', 'opp5','opp6', 'opp7']
accounts=[]
global account
account=[]
follow = []


consumer_key = "7tnMEONXpqg6SBDW4eec62GI0"
consumer_secret = "pDwKxefBmxUW2AGrdzhprkAiDt8BhOTmmiqMd9BIZAoAbkGvEz"
access_key = "925003211425107968-hAdW9BmUd3L71cJevI3J6Wr9CbgD7AH"
access_secret = "yWpysA00PYcBgCgqdtTgqcrA7HR9A1YFSWjCvjePjUYiD"

#shandles_list = []
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)			
#handles_list = ["Gavincko","ECAlertON143", "ECAlertON128", "ECAlertON12"]	
#x = PrettyTable()
class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.dict = {'Central Region': ['Toronto', 'Barrie', 'Brampton'],
                     'West Region': ['Windsor', 'London', 'sarnia'],
                     'East Region': ['Nigeria', 'Kenya', 'Ethiopia'],
                     'Other Regions': ['Windsor', 'London', 'sarnia']
                     }
        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)
        self.variable_a.trace('w', self.updateoptions)
        self.optionmenu_a = tk.OptionMenu(
            self, self.variable_a, *self.dict.keys())
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, '')
        self.variable_a.set('Central Region')
        self.optionmenu_a.pack(pady=20, padx=10, side=tk.TOP, expand=1)
        self.optionmenu_b.pack( padx=5, pady=20, side=tk.LEFT)
        self.btn = tk.Button(self, text="Add", width=8, command=self.add)
        self.btn.pack(padx=10, pady=10, side=tk.LEFT)
        self.btn1 = tk.Button(self, text="Submit",
                              width=8, command=self.submit)
        self.btn1.pack(padx=5, pady=20, side=tk.LEFT)
        self.btn2 = tk.Button(self, text="delete",
                              width=8, command=self.delete)
        self.btn2.pack(padx=5, pady=20, side=tk.LEFT)
        self.pack()
        global txt2
        txt2 = scrolledtext.ScrolledText(self,state='disabled', width=40, height=10)
        txt2.pack(side="left", fill="both", expand=1, pady=20, padx=20)

    def updateoptions(self, *args):
        countries = self.dict[self.variable_a.get()]
        self.variable_b.set(countries[0])
        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')
        for country in countries:
            menu.add_command(
                label=country, command=lambda country=country: self.variable_b.set(country))
				
    def remove(self,accounts):
        final_list=[]
        for acc in accounts:
            if acc not in final_list:
                 final_list.append(acc)
        # print(accounts)
        # print(final_list)
        return final_list
		
		
    def add(self, *args):
        var1 = self.variable_a.get()
        var2 = self.variable_b.get()
        # txt3 = scrolledtext.ScrolledText(self, width=40, height=10)
        # txt3.pack(side="top", fill="both", expand=True)
        # print(account)
        if tkinter.messagebox.askokcancel("Selection", "Confirm selection: " + var1 + ' ' + var2):
		
		
            if var2 == "Toronto":
                if(len(TorontoList) > 0):
                    txt2.configure(state='normal')
                    # txt2.delete(1.0, tk.END)
                txt2.configure(state='normal')
                for i in range(len(TorontoList)):
                    if (TorontoList[i] in accounts):
                        continue
                    txt2.insert(tk.INSERT, TorontoList[i] + "\n")
                    accounts.append(TorontoList[i])
                txt2.configure(state='disabled')
				
				
				
            if var2 == "Barrie":
                if(len(TorontoList) > 0):
                    txt2.configure(state='normal')
                    # txt2.delete(1.0, tk.END)
                for i in range(len(BarrieList)):
                    if (BarrieList[i] in accounts):
                        continue
                    txt2.insert(tk.INSERT, BarrieList[i] + "\n")
                    accounts.append(BarrieList[i])
                txt2.configure(state='disabled')
                
				
            
            
            
    def delete(self,*args):
        del accounts[:]
        txt2.configure(state='normal')
        txt2.delete(1.0, tk.END)
        txt2.configure(state='disabled')
        open('UserInput.txt', 'w').close()
		
		
    def submit(self, *args):
		account=self.remove(accounts)
		print(account)
        # with open('UserInput.txt', 'w') as fh:
            # for j in range(len(account)):
                # fh.write(account[j]+"\n")
		for acc in account:
			userid = api.get_user(acc)
			follow.append(userid.id)
			
		collecting_tweet.done(account, follow)
		
		exit()
		
   
root = tk.Tk()
app = App(root)
app.mainloop()

