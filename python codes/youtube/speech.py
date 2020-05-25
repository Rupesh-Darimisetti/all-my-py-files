import speechRecognisation as sr

r=sr.Recogniser()

with sr.Microphone() as source:
         print('speak  anything: ')
         audio=r.listen(source)
         try:
                   text=r.redcognise_google(audio)
                   print ('you said:{}'.format(text))
                  
         except e:
                  print("i didnt understand what u said")
