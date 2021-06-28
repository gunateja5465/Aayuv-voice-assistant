import speech_recognition as sr
from time import ctime
import time
import webbrowser
import os
import pyttsx3
import screen_brightness_control as sbc
import subprocess
import smtplib
import pyautogui
import pywhatkit as pwk

pc=pyttsx3.init()
voices = pc.getProperty('voices')
r=sr.Recognizer()

def sendgmail(to,content):
    serv=smtplib.SMTP_SSL('smtp.gmail.com',465)
    serv.login('gunatejapattoori1@gmail.com','afsan5465')
    serv.sendmail('gunatejapattoori1@gmail.com',to,content)
    serv.quit()

def record_audio():
    
    with sr.Microphone() as source:
        
        pc.runAndWait()
        voice_data=''
        try:
            print("Listening")
            r.pause_threshold = 0.8
            r.adjust_for_ambient_noise(source,duration=1)
            audio=r.listen(source)
            print("recognizing")
            voice_data=r.recognize_google(audio,language='en-in')
        
        except Exception:
            print('say again')
            pc.say('say that again')
    return voice_data
    
def respond(x):
    while (x):
        voice_data=record_audio()
        print(voice_data)
        if 'stop' in voice_data:
            pc.say('Thankyou sir!')
            print('thanku')
            x=False
        elif 'I love you' in voice_data:
            pc.say('I love you too ')
        elif 'what is your name' in voice_data:
            pc.say('My name is aayuv.')
        elif 'what time is it' in voice_data:
            pc.say(ctime())
            
        else:
            if 'change brightness' in voice_data or 'set brightness' in voice_data:
                b=int(voice_data.replace('change brightness to',''))
                b=int(voice_data.replace('set brightness to',''))
                sbc.fade_brightness(b)
            if 'search' in voice_data:
                pc.say('what do you want to search for?')
                search=record_audio()
                url='https://google.com/search?q='+search
                webbrowser.get().open(url)
            elif 'increase brightness' in voice_data:
                b=sbc.get_brightness()
                sbc.fade_brightness(b+25,b)
            elif 'decrease brightness' in voice_data:
                b=sbc.get_brightness()
                sbc.fade_brightness(b-25,b)
            elif 'find location' in voice_data:
                pc.say('plese say the name of the location')
                loc=record_audio()
                url='https://google.nl/maps/place/'+loc+'/&amp;'
                webbrowser.get().open(url)
            elif 'results' in voice_data:
                pc.say('what should i search for')
                song=record_audio()
                url='https://www.youtube.com/results?search_query='+song
                webbrowser.get().open(url)
            elif 'open' in voice_data:
                pc.say('what should i open for u')
                app=record_audio()
                app=app.lower()
                print(app)
                if 'vlc' in app:
                    subprocess.Popen('C://Program Files//VideoLAN//VLC//vlc.exe')
                elif 'torrent' in app:
                    subprocess.Popen('C://Program Files//tixati//tixati.exe')
                elif 'chrome' in app:
                    subprocess.Popen('C://Program Files (x86)//Google//Chrome//Application//chrome.exe')
                elif 'not' in app:
                    subprocess.call('notepad')
            elif 'show' in voice_data:
                f=open('notes.txt','r')
                print(f.read())
                print('notes opened')

            elif 'write a note' in voice_data:
                pc.say('what should write boss')
                note=record_audio()
                file=open('notes.txt','a')
                file.write(ctime())
                file.write(' -- ')
                file.write(note)
            elif 'mail' in voice_data:
                try:
                    pc.say('whom should i send')
                    print('give the mail id to send')
                    to=input()
                    pc.say('what should i send')
                    content=record_audio()
                    print('done')
                    sendgmail(to,content)
                    pc.say('done boss')
                except Exception as e:
                    pc.say('unable to send mail')
                    print(e)
            elif 'screenshot' in voice_data:
                ss=pyautogui.screenshot()
                pc.say('how should i save it')
                sc=record_audio()
                loca='C://voice//screenshots//'+sc+'.png'
                ss.save(loca)
                print('ss taken')
            elif 'scroll down' in voice_data:
                pyautogui.scroll(200)
            elif 'scroll up' in voice_data:
                pyautogui.scroll(-200)
            elif 'pp' in voice_data:
                try:
                    pc.say('to whom should i send ')
                    pc.say('give me the number')
                    print('give the number to send whatsapp mesage')
                    num=input()
                    num='+91'+num
                    pc.say('what should i send')
                    msg=record_audio()
                    cth=int(time.strftime('%H'))
                    print(cth)
                    ctm=int(time.strftime('%M'))
                    ctm+=1
                    print(ctm)
                    pwk.sendwhatmsg(num,msg,cth,ctm)
                    print('sent')
                except:
                    print('unable to send')

    
currentTime = int(time.strftime('%H'))
if currentTime < 12 :
    pc.say('Good morning boss')
if currentTime >= 12 and currentTime <18:
    pc.say('Good afternoon boss')
if currentTime >= 18 :
    pc.say('Good evening boss')
pc.say('what can i do for you')
x=True
respond(x)