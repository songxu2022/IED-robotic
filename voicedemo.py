#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 00:33:31 2020

@author: kr7
"""
import speech_recognition as sr 
import datetime 
import wikipedia 
import shutil 
from twilio.rest import Client  
import pyttsx3

engine = pyttsx3.init() 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 210)

def speak(output):
    engine.say(output)
    engine.runAndWait()

    print("PerSon : ", output) 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    


def wishMe(): 
	hour = int(datetime.datetime.now().hour) 
	if hour>= 0 and hour<12: 
		speak("Good Morning Sir !") 

	elif hour>= 12 and hour<18: 
		speak("Good Afternoon Sir !") 

	else: 
		speak("Good Evening Sir !") 

	assname =("Jarvis 1 point o") 
	speak("I am your Assistant") 
	speak(assname) 
	

def usrname(): 
	speak("What should i call you sir") 
	uname = takeCommand() 
	speak("Welcome Mister") 
	speak(uname) 
	columns = shutil.get_terminal_size().columns 
	
	print("#####################".center(columns)) 
	print("Welcome Mr.", uname.center(columns)) 
	print("#####################".center(columns)) 
	
	speak("How can i Help you, Sir") 

def takeCommand(): 
	
	r = sr.Recognizer() 
	
	with sr.Microphone() as source: 
		
		print("Listening...") 
		r.pause_threshold = 1
		audio = r.listen(source) 

	try: 
		print("Recognizing...")	 
		query = r.recognize_google(audio, language ='en-in') 
		print(f"User said: {query}\n") 

	except Exception as e: 
		print(e)	 
		print("Unable to Recognizing your voice.") 
		return "None"
	
	return query 

if __name__ == '__main__':  
	
	# This Function will clean any 
	# command before execution of this python file  
	wishMe() 
	usrname() 
	
	while True: 
		
		query = takeCommand().lower() 
		
		# All the commands said by user will be 
		# stored here in 'query' and will be 
		# converted to lower case for easily 
		# recognition of command 
		if 'wikipedia' in query: 
			speak('Searching Wikipedia...') 
			query = query.replace("wikipedia", "") 
			results = wikipedia.summary(query, sentences = 3) 
			speak("According to Wikipedia") 
			print(results) 
			speak(results) 
			
		elif "send message" in query: 
				# You need to create an account on Twilio to use this service 
				account_sid = 'AC76c62d885f1dc49046ab8215ea012e48'
				auth_token = '891087c46ff345f7dd8d3272529b7e4e'
				client = Client(account_sid, auth_token) 

				message = client.messages \
								.create( 
									body = takeCommand(), 
									from_='+12052735226', 
									to =''
								) 

				print(message.sid) 



		# elif "" in query: 
			# Command go here 
			# For adding more commands 
