import speech_recognition
import pyttsx3
import pyaudio
import os
import time
from tkinter import *
import threading
import sys
from datetime import datetime
from datetime import date
import turtle
import wikipedia
import ctypes
import random
from googletrans import Translator
import subprocess
import requests
from bs4 import BeautifulSoup
import webbrowser

#********** CLASA DE GLUME ***************

class Jokes():
	def __init__(self,joke1,joke2,joke3):
		self.joke1 = joke1
		self.joke2 = joke2
		self.joke3 = joke3

jokes = Jokes("De ce nu pot elefanții să foloseasca calculatorul \n\n pentru că le este frică de maus","Pe ce raft a pus Mihai cărțile de matematică \n\n pe raftul de cărți horor","Urăsc violența dar îmi place când mă lovește norocul")

#------------- Declararea Variabilelor ----------------

recognizer = speech_recognition.Recognizer()
translator = Translator()
shape_size_1 = 9
test = False
shape_size_2 = 9
stop_talking = True
stop_thread = False
stop_program = False
tasks = []
jokes1 = [jokes.joke1,jokes.joke2,jokes.joke3]
schedule1 = "LUNI: \n\n Engleza \n Matematica \n Franceza \n Româna \n Chimia \n Istoria \n Dezvoltarea Personală \n"
schedule2 = "MARȚI: \n\n Româna \n Biologia \n Matematica \n Engleza \n Chimia \n Programare în C plus plus \n"
schedule3 = "MIERCURI: \n\n Educația Fizică \n Geografia \n Franceza \n Matematica \n Româna \n Chimia \n"
schedule4 = "JOI: \n\n Istoria \n Matematica \n Engleza \n Biologia \n Informatica \n Franceza \n"
schedule5 = "VINERI: \n\n Educatia Fizica \n Informatica \n Româna \n Matematica \n Geografia \n Engleza \n"


#********************** FUNCTIA CARE AFISEAZA ORARUL ************************

def show_school_schedule():
	global schedule1
	global schedule2
	global schedule3
	global schedule4
	global schedule5

	wn = Tk()
	wn.geometry("300x700")
	wn.title("Orarul Lecțiilor")
	table1 = Label(wn,text = "Orarul: \n\n" + schedule1,font = ("Consolas Bold",9))
	table1.place(x=0,y=0)
	table1.pack()
	table2 = Label(wn,text = schedule2,font = ("Consolas Bold",9))
	table2.place(x=0,y=100)
	table2.pack()
	table3 = Label(wn,text = schedule3,font = ("Consolas Bold",9))
	table3.place(x=0,y=200)
	table3.pack()
	table4 = Label(wn,text = schedule4,font = ("Consolas Bold",9))
	table4.place(x=0,y=300)
	table4.pack()
	table5 = Label(wn,text = schedule5,font = ("Consolas Bold",9))
	table5.place(x=0,y=300)
	table5.pack()
	wn.mainloop()

# THREADUL CARE AFISEZA ORARUL

schedule = threading.Thread(target = show_school_schedule)

#********************** FUNCTIA CARE OPRESTE PROGRAMUL ***************************

def stop_app():
	global stop_program
	stop_program = True

#*************************** FUNCTIA SECUNDARA ******************************

def app():
	global stop_program
	window = turtle.Screen()
	window.setup(600,600)
	window.title("Andrei Assistant")
	try:
		img = Image("photo",file = "icon.png")
		window.bgcolor("#01001E")
		turtle._Screen._root.iconphoto(True,img)
	except:
		test = True
	window.tracer(0)
	try:
		window.bgpic("back.gif")
	except:
		window.bgcolor("#01001E")
	pen = turtle.Turtle()
	pen.color("black")
	pen.width(3)
	pen.penup()
	pen.setposition(-280,230)
	pen.pendown()
	pen.color("white")
	pen.write("Spune 'stop' sau 'La revedere' daca vrei să ieși \n      sau apasă tasta 's' sau 'q'.",font = ("Consolas Bold",15))
	pen.penup()
	pen.setposition(-200,-285)
	pen.pendown()
	pen.write("Copyright © 2023 AndreiAssistant-All Rights Reserved \n   	 	 CEO - Arseni Andrei ",font = ("Consolas Bold",10))
	pen.hideturtle()
	turtle.listen()
	turtle.onkeypress(stop_app,"s")
	turtle.onkeypress(stop_app,"q")
	while True:
		window.update()
		if stop_program == True:
			break

	window.bye()

#********************** FUNCTIA PRINCIPALA ************************	

def main_loop():
	global jokes1
	global schedule1
	global schedule2
	global schedule3
	global schedule4
	global schedule5
	global stop_program
	global tasks
	add_task = False
	tell_schedule_day = False
	os.system('cls')
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	rate = engine.getProperty('rate')
	engine.setProperty('voice',voices[1].id)
	engine.setProperty('rate',125)
#=========== Mesajul de introducere ===========
	time.sleep(1)
	engine.say("Salut, mă numesc Andrei, cu ce tepot ajuta")
	engine.runAndWait()


# MAIN LOOP

	while not stop_program:

		try:
			with speech_recognition.Microphone() as mic:

				recognizer.adjust_for_ambient_noise(mic,duration = 0.2)
				audio = recognizer.listen(mic)
				text = recognizer.recognize_google(audio,language = "ro")
				text = text.lower()
				#print("[Alta incercare]||||||||")

				#print(text)

				for letter in text:
					
#//////////////////////////// SPUNE O GLUMA ///////////////////////////////////

					if ("glumă" in text) or ("glume" in text):
						joke = random.choice(jokes1)
						engine.say(joke)
						engine.runAndWait()
						break

#/////////////////////// SPUNE NUMELE /////////////////////////

					elif ("numești" in text) or ("cheamă" in text):
						engine.say("Mă numesc Andrei, la fel ca creatorul meu.")
						engine.runAndWait()
						break

#//////////////////////////// SPUNE VARSTA ////////////////////

					elif (("ani" in text) and ("câți" in text)) or ("vârsta" in text):
						engine.say("Nu am o vârstă, sistemul meu este încă în dezvoltare")
						engine.runAndWait()
						break

#//////////////////////////// VREMEA IN ORAS /////////////////////////////

					elif ("vreme" in text or "temperat" in text):
						engine.say("Ce oraș")
						engine.runAndWait()
						with speech_recognition.Microphone() as mic:

							recognizer.adjust_for_ambient_noise(mic,duration = 0.2)
							audio = recognizer.listen(mic)
							city = recognizer.recognize_google(audio,language = "ro")
							city = city.lower()
						webbrowser.open_new(f"https://google.com/search?q='vremea {city}")
						break

#///////////////////////// TRADUCE O FRAZA ///////////////////////////////

					elif ("tradu" in text) or ("traduci" in text):
						engine.say("Traduci din românăăăăăă?")
						engine.runAndWait()
						with speech_recognition.Microphone() as mic:

							recognizer.adjust_for_ambient_noise(mic,duration = 0.2)
							audio = recognizer.listen(mic)
							confirmation = recognizer.recognize_google(audio,language = "ro")
							confirmation = confirmation.lower()
							if ("nu" in confirmation):
								engine.say("Spune fraza")
								engine.runAndWait()
								with speech_recognition.Microphone() as mic:

									recognizer.adjust_for_ambient_noise(mic,duration = 0.2)
									audio = recognizer.listen(mic)
									phrase = recognizer.recognize_google(audio,language = "en")
									phrase = phrase.lower()
									translated_phrase = translator.translate(phrase,dest = "ro")
									#print(translated_phrase.text)
									engine.setProperty('voice',voices[1].id)
									engine.say(translated_phrase.text)
							else:
								engine.say("Spune fraza")
								engine.runAndWait()
								with speech_recognition.Microphone() as mic:

									recognizer.adjust_for_ambient_noise(mic,duration = 0.2)
									audio = recognizer.listen(mic)
									phrase = recognizer.recognize_google(audio,language = "ro")
									phrase = phrase.lower()
									translated_phrase = translator.translate(phrase,dest = "en")
									#print(translated_phrase.text)
									engine.setProperty('voice',voices[0].id)
									engine.say(translated_phrase.text)
							engine.runAndWait()
							engine.setProperty('voice',voices[1].id)
							break


#//////////////////////// DESCHIDE O APLICATIE //////////////////////////////////

					elif ("deschide" in text or "aplicație" in text or "pornește" in text):
						engine.say("Spune numele aplicației pe care vrei să o deschid")
						engine.runAndWait()
						with speech_recognition.Microphone() as mic:

							recognizer.adjust_for_ambient_noise(mic,duration = 0.2)
							audio = recognizer.listen(mic)
							app = recognizer.recognize_google(audio,language = "ro")
							app = app.lower()
							not_found = False
							
							if ("linia de comandă" in app or "comandă" in app):
								subprocess.call("cmd.exe")
							elif ("you tube" in app or "youtube" in app or "iutub" in app or "youtub" in app):
								webbrowser.open_new("https://www.youtube.com")
							elif ('calculator' in app):
								subprocess.call("calc.exe")
							elif (("browser" in app) or ("google" in app) or ("chrome" in app)):
								webbrowser.open_new("https://www.google.com")
							elif ("code" in app) or ("block" in app):
								subprocess.call("C:\\Program Files\\CodeBlocks\\codeblocks.exe")
							elif (("sublime" in app) or ("text" in app)):
								subprocess.call("C:\\Program Files\\Sublime Text\\sublime_text.exe")
							else:
								webbrowser.open_new(f"https://google.com/search?q='{app}")

						break

#///////////////////////////////// SPUNE ORARUL LECTIILOR //////////////////////////////////////////

					elif ("orar" in text) or ("școlar" in text):
						tell_schedule_day = False
						engine.say("Orarul tău este aici")
						engine.runAndWait()
						schedule.start()
						engine.say("Vrei să îți spun orarul ")
						engine.runAndWait()
						listener = speech_recognition.Recognizer()
						with speech_recognition.Microphone() as micr:
							listener.adjust_for_ambient_noise(micr,duration = 0.2)
							voice = listener.listen(micr)
							confirm = listener.recognize_google(voice,language = "ro")
							confirm = confirm.lower()
							if ("da" or "dap" or "yes") in confirm:
								engine.say("Care zi")
								engine.runAndWait()
								tell_schedule_day = True
							else:
								engine.say("Bine")
								engine.runAndWait()
								tell_schedule_day = False
								break

#//////////////////////////// CAUTA O PERSONALITATE //////////////////////////////////


					elif (("caută" in text) or ("google" in text) or ("cauți" in text) or ("search" in text)):
						engine.say("Spune ce vrei să cauți")
						engine.runAndWait()
						listener = speech_recognition.Recognizer()
						with speech_recognition.Microphone() as micr:
							listener.adjust_for_ambient_noise(micr,duration = 0.2)
							voice = listener.listen(micr)
							word = listener.recognize_google(voice,language = "ro")
							word = word.lower()
							word = translator.translate(word,dest = "en")
						#	print(word.text)
							try:
								informatia = ""
								info = wikipedia.summary(word.text,sentences = 5)
								#print("Wikipedia")
								info_ro = translator.translate(info,dest = "ro")
								#print(info_ro.text)
								engine.say(info_ro.text)
							except:
								engine.say("Nu sa găsit un rezultat,dar am deschis o pagină google cu aceast subiect")
								webbrowser.open_new(f"https://google.com/search?q='{word.text}'")
							engine.runAndWait()
							break

#////////////////////////////////// SPUNE SARCINILE /////////////////////////////////

					elif (("sarcină" in text) or ("sarcina" in text) or ("sarcini" in text) or ("dusk" in text) or ("ask" in text) or ("desk" in text) or ("treabă" in text) or ("treburi" in text)):
						if len(tasks) != 0:
							engine.say("Sarcinile tale sunt")
							for task in tasks:
								engine.say(task)
						else:
							engine.say("Tu nu ai sarcini de făcut")
						engine.runAndWait()
						engine.say("Vrei să introduci o sarcină in lista ta de sarcini")
						engine.runAndWait()
						listener = speech_recognition.Recognizer()
						with speech_recognition.Microphone() as micr:

							listener.adjust_for_ambient_noise(micr,duration = 0.2)
							voice = listener.listen(micr)
							confirm = listener.recognize_google(voice,language = "ro")
							confirm = confirm.lower()
							#print(confirm + " confirmat!!!!!!!!!!!!!!!!!!!!!!!!")
							if ("da" in confirm or "yeah" in confirm or "yep" in confirm):
								engine.runAndWait()
								add_task = True
							else:
								add_task = False
								engine.say("Bine")
								engine.runAndWait()
								break

#////////////////////////////////// SALUTA UTILIZATORUL /////////////////////////////////

					elif ("bună" in text) or ('salut' in text) or ("noroc" in text) or ("sheila" in text) or ("halo" in text):
						engine.say("Bună")
						time.sleep(0.1)
						engine.say("Cu ce te pot ajuta")
						engine.runAndWait()
						break

#/////////////////////////// SPUNE CREATORUL TAU /////////////////////////////////						

					elif ("creat" in text):
						engine.say("Creatorul meu este Andrei Arseni")
						engine.runAndWait()
						break

#//////////////////////////// OPRESTE PROGRAMUL /////////////////////////////////						

					elif ("stop" in text) or ("stop stop" in text) or ("la revedere" in text) or ("ieși" in text):
						engine.say("La revedere")
						engine.runAndWait()
						stop_program =  True
						break

#//////////////////////  TIMPUL CURENT  /////////////////////////////						

					elif (("timp" in text) or ("ora" in text) or ("oră" in text)):
						engine.say("Timpul curent este")
						time.sleep(0.1)
						week_day = time.strftime("%A")
						week_day2 = ""
						if (week_day == "Monday"):
							week_day2 = "Luni"
						elif (week_day == "Tuesday"):
							week_day2 = "Marți"
						elif (week_day == "Wednesday"):
							week_day2 = "Miercuri"
						elif (week_day == "Thursday"):
							week_day2 = "Joi"
						elif (week_day == "Friday"):
							week_day2 = "Vineri"
						elif (week_day == "Saturday"):
							week_day2 = "Sîmbată"
						elif (week_day == "Sunday"):
							week_day2 = "Duminică"
						current_time = time.strftime("ziua de " + week_day2 + " ora %H  %M minute %S secunde",time.localtime())
						engine.say(current_time)
						engine.runAndWait()
						break

#///////////////////////////  DATA CURENTA /////////////////////////////


					elif (("data" in text) or ("dată" in text)):
						engine.say("Data curentă este ")
						time.sleep(0.1)
						todays_date = date.today()
						month = ""
						if (todays_date.month == 10):
							month = "octombrie"
						if (todays_date.month == 11):
							month = "noiembrie"
						if (todays_date.month == 12):
							month = "decembrie"
						if (todays_date.month == 1):
							month = "ianuarie"
						if (todays_date.month == 2):
							month = "februarie"
						if (todays_date.month == 3):
							month = "martie"
						if (todays_date.month == 4):
							month = "aprilie"
						if (todays_date.month == 5):
							month = "mai"
						if (todays_date.month == 6):
							month = "iunie"
						if (todays_date.month == 7):
							month = "iulie"
						if (todays_date.month == 8):
							month = "august"
						if (todays_date.month == 9):
							month = "septembrie"

						engine.say("Luna" + month)
						engine.runAndWait()
						engine.say("Ziua" + str(todays_date.day))
						#print(todays_date.day)
						engine.runAndWait()
						engine.say("Anul" + str(todays_date.year))
						engine.runAndWait()
						day = todays_date.day

						#Verifica daca este o zi speciala
						
						if (day == 31 and month == "decembrie"):
							engine.say("Astăzi este Anul Nou")

						elif (day == 25 and month == "decembrie"):
							engine.say("Astăzi este Crăciunul")

						elif (day == 20 and month == "octombrie"):
							engine.say("Astăzi este ziua de naștere a creatorului meu \n Arseni Andrei")

						elif (day == 1 and month == "iunie"):
							engine.say("Astăzi este începutul verii")

						engine.runAndWait()
						break


#////////////////////////// VERIFICA DACA SA ADAUGE O SARCINA IN LSTA DE SARCINI ///////////////////

					if add_task == True:
						engine.say("Spune sarcina")
						engine.runAndWait()
						listener2 = speech_recognition.Recognizer()
						with speech_recognition.Microphone() as micro:
							listener2.adjust_for_ambient_noise(micro,duration = 0.2)
							voice = listener2.listen(micro)
							task = listener2.recognize_google(voice,language = "ro")
							task = task.lower()
							tasks.append(task)
							engine.say("Sarcina a fost adăugată cu succes")
							engine.runAndWait()
						#	print("Sarcina_________________" + task)
							add_task = False
							break	

#//////////////////////////// VERIFICA DACA SA SPUNA ORARUL //////////////////////////

					if tell_schedule_day == True:
						#print("[Intrat in ziua de orar]")
						listener = speech_recognition.Recognizer()
						with speech_recognition.Microphone() as micr:
							listener.adjust_for_ambient_noise(micr,duration = 0.2)
							voice = listener.listen(micr)
							day = listener.recognize_google(voice,language = "ro")
							day = day.lower()
							if "luni" in day:
								engine.say("Orarul pe luni este")
								engine.say(schedule1)
								engine.runAndWait()
								engine.say("asta e tot")
								engine.runAndWait()
								
							if "marți" in day:
								engine.say("Orarul pe marți este")
								engine.say(schedule2)
								engine.runAndWait()
								engine.say("asta e tot")
								engine.runAndWait()
								
							if "miercuri" in day:
								engine.say("Orarul pe miercuri este")
								engine.say(schedule3)
								engine.runAndWait()
								engine.say("asta e tot")
								engine.runAndWait()
								
							if "joi" in day:
								engine.say("Orarul pe joi este")
								engine.say(schedule4)
								engine.runAndWait()
								engine.say("asta e tot")
								engine.runAndWait()
								
							if "vineri" in day:
								engine.say("Orarul pe vineri este")
								engine.say(schedule5)
								engine.runAndWait()
								engine.say("asta e tot")
								engine.runAndWait()
								
							tell_schedule_day = False
							break

					else:
						engine.say("Nu înțeleg ce vrei să spui")
						engine.runAndWait()
						break
				
				if stop_program == True:
					break

		except:
			#print("error")
			recognizer = speech_recognition.Recognizer()
			continue

	sys.exit(0)

# THREADUL PRINCIPAL

main_thread = threading.Thread(target = main_loop)
main_thread.start()

# THREADUL SECUNDAR

second_thread = threading.Thread(target = app)
second_thread.start()
