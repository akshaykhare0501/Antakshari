# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 22:48:43 2021

@author: Admin
"""
from gtts import gTTS
from playsound import  playsound
import os
import speech_recognition as sr
global Query
global letter
global mytext
global Status

def antakshari():
    global Status
    global Query
    Status = 1
    if ('खेल' in Query or 'अंताक्षरी' in Query) and ('रोको' in Query or 'रोक' in Query or 'रुक' in Query or 'बंद' in Query):
        Status = 0
    
    if Status == 1:
        last_letter()
        song()
        win_check()
    if Status == 0: 
        mytext="अंताक्षरी खेलने के लिए आपका धन्यवाद "
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    
     

def last_letter():
    global letter
    global Status

    if Query[-1] == ' ' or ' ा'  or ' ि '  or 'ूू ू '  or ' ृ'  or ' े'  or ' ै'  or ' ो'  or ' ौ':
        letter = Query[-2]
        mytex=f"आपका आखिरी अक्षर था ......{ Query[-2]}..., मुझे .....{ Query[-2]} अक्षर से गाना होगा   "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    else:
        letter = Query[-1]
        mytex=f"आपका आखिरी अक्षर था ......{ Query[-1]}..., मुझे .....{ Query[-1]} अक्षर से गाना होगा   "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
def song():
    global letter
    global mytext
    if letter == 'क':
        mytext="क्यों इतने में तुझको ही, चुनता हूँ हर पल, क्यों तेरे ही ख्वाब अब, बुनता हूँ हर पल"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....ल...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'ख':
        mytext="ख्वाबों में भी यह सोचा नहीं था, की धुप भी मिलेगी छाँव में, कभी रास्तों में सोचा नहीं था, की काँटे भी चुभेंगे पाऊँ मे"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....म...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'ग':
        mytext="गम को ऐ यार उल्लू बना दे, खुल के तू मुस्कुराना, छोड़ फिकरों की घंटी बजाना, दिल की ढोलक बजाना"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....न...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'घ':
        mytext="घूमर रमवाने आप पधारो सा, आवो जी आवो जी घूमार्दी खेलबा ने, पधारो सा घूमार्दी खेलबा ने, बालम थारो गुरर गुरर गुरावे, आज म्हारो जिवड़ो घनो हिच्कावे"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....व...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'च':
        mytext="चुरा के दिल मेरा....., गोरिया चली.....,चुरा के दिल मेरा...,हा हा .. गोरिया चली,......पागल हुआ... दीवाना हुआ... पागल हुआ... दीवाना हुआ... तेरी गली में चली....हां..चुरा के दिल मेरा....., गोरिया चली"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....ल...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'छ':
        mytext="छूकर.. मेरे मन को, किया तूने.. क्या इशारा, बदला यह मौसम, लगे प्यारा जग सारा, छूकर.. मेरे मन को, किया तूने.. क्या इशारा"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....र...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'ज':
        mytext="जनम जनम जनम.. साथ चलना यूँही, कसम तुम्हे कसम.. आके मिलना यही, एक जान है भले दो बदन हो जुदा"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....द...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'झ':
        mytext="झटका ज़रा सा.. महसूस हुआ एक, लाइफ की गाडी.. ने कस्स के मारे ब्रेक, हो रहा है क्यों कंफ्यूज मेरे दिल, मश्वरा मेरा तू आज़मा के देख. यही उमर है करले, गलती से मिस्टेक. यही उमर है करले, गलती से मिस्टेक"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....क...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'त':
        mytext="तेरी उम्मीद,  तेरा इंतज़ार करते हैं, तेरी उम्मीद, तेरा इंतज़ार करते हैं,  ऐ सनम, हम तो सिर्फ तुमसे प्यार करते है"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....ह...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'थ':
        mytext="थम सा गया है ये समा, आये जो सामने हो तुम, बस इक निगाह में मुझे, अपना बना गए हो तुम"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....म...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'द':
        mytext="दे दे प्यार दे , प्यार दे, प्यार दे रे हमें प्यार दे, दे दे प्यार दे प्यार दे, प्यार दे रे हमें प्यार दे"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....द...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'ध':
        mytext="धरती धोरां री, आ तो सुरगां नै सरमावै, ईं पर देव रमण नै आवै, ईं रो जस नर नारी गावै, धरती धोरां री"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....र...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'न':
        mytext="नमो-नमो जी, शंकरा, भोलेनाथ, शंकरा,जय त्रिलोकनाथ, शंभु, हे शिवाय, शंकरा"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....र...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'प':
        mytext="पहला नशा, पहला खुमार..., नया प्यार है.. नया इंतज़ार,.. कर लूं मैं क्या अपना हाल, ए ए दिल-इ-बेकरार"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....र...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'फ':
        mytext="फूलों का तारों का सबका कहना है, एक हज़ारों में मेरी बहना है, सारी उम्र हमें संग रहना है, फूलों का तारों का सबका कहना है"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....ह...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'ब':
        mytext="बोले चूड़ियाँ, बोले कंगना, हाय मैं हो गया.. तेरा साजणा, तेरे बिनजियो नईयो लगदा, मैं ते मर जावा"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....व...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'भ':
        mytext="भीगी भीगी सड़कों पे मैं, तेरा इंतज़ार करो, धीरे धीरे दिल की ज़मीं... को, तेरे ही नाम करू"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....र...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'म':
        mytext="मेरे देश की धरती, सोना उगले, उगले हीरे मोती, मेरे देश की धरती"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....त...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'य':
        mytext="यह जो हल्का हल्का सुरूर है, यह तेरी नजर का कुसूर है, तेरा इश्क है या फितूर है, मेरा इश्क है या फितूर है, मैंने खुद को तुझ पर लुटा दिया"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....य...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'र':
        mytext="रंग बरसे, भीगे चुनरवाली रंग बरसे,हो रंग बरसे,  भीगे चुनरवाली रंग बरसे"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....स...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'ल':
        mytext="लाल दुपट्टा उड़ गया,  रे बैरी, हवा के झोंके से, मुझको पिया ने देख लिया,  है रे धोके से"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....स...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'व':
        mytext="वोह लम्हे, वह बातें, कोई न जाने, थी कैसी रातें, होऊ, बरसातें, वह भीगी भीगी यादें, वह भीगी भीगी यादे"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....द...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'श':
        mytext="शक्तिमान.. शक्तिमान.. शक्तिमान.. शक्ति शक्ति शक्तिमान शक्ति शक्ति शक्तिमान शक्ति शक्ति शक्तिमान शक्ति शक्ति शक्तिमान अदभुत अदम्य साहस की परिभाषा है ये मिटती मानवता की आशा है ये श्रृष्टि की शक्ति का वरदान है ये अवतार नहीं है ये इंसान है शक्तिमान.. शक्तिमान.. शक्तिमान"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....न...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'स':
        mytext="सुन साथिया माहिया, बरस दे इश्क़या की इंक़यान, रंग जाओ, रंग जाओ, खो जाओ, मेन"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ....न...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif letter == 'ह':
        mytext="हम सब मर्द मावले बड़े खुद्दार है, अब हर एक दिन स्वराज का त्योहार है, अब यह शीश ना झुके, तेरी लाज हम रखें, तेरे चरणों की शपथ  मां जगदंबे,.. हे माय भवानी"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        mytex="आपको ... न...अक्षर से गाना होगा  "
        myobj=gTTS(text=mytex,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    #print(mytext)
    takeCommandHindi()
    
def win_check():
    global mytext

    print(mytext[-1], mytext[-2])
    print(Query[0], Query[1], Query[2])
    if Query[0] == mytext[-2] or Query[0] == mytext[-1]:
        mytext="आपने सही गाना  गाया"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
        antakshari()
        #break
    elif Query[0] != mytext[-2] or Query[0] != mytext[-1]:
        mytext="आपने गलत अक्षर से गाना गाया, में जीत गई"
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    elif len(Query) > 1 and len(Query) < 20:
        mytext="आपने बहुत कम गाना गाया, में जीत गई" 
        myobj=gTTS(text=mytext,lang='hi',slow=False)
        myobj.save('audio_1.mp3')
        playsound('audio_1.mp3')
        os.remove('audio_1.mp3')
    
    
    
        
        
    
    
def takeCommandHindi():
	global Query	
	r = sr.Recognizer()
	with sr.Microphone() as source:
		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		print('Listening')
		r.pause_threshold = 0.7
		audio = r.listen(source)
		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language='hi')
			
			# for listening the command in indian english
			print("the query is printed='", Query, "'")
        
		# handling the exception, so that assistant can
		# ask for telling again the command
		except Exception as e:
			print(e)
			print("Firse kahiye")
			return "None"
		return Query
        
       
mytext="अंताक्षरी में आपका स्वागत है,... चलिए आपसे शुरुवात  करते है, पहले आप किसीभी शब्द से गाना शुरु कीजिए"
myobj=gTTS(text=mytext,lang='hi',slow=False)
myobj.save('audio_1.mp3')
playsound('audio_1.mp3')
os.remove('audio_1.mp3')
takeCommandHindi()
Status = 1
antakshari()


    
        
            
