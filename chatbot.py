import random
from string import punctuation
import utils
import hashlib
import re
import nltk
import dataload
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
BOT_MESSAGE=["Hai ,My Name is PyBot.How can I help you?",
             "Hai",
             "PyBot Online.Ready To Serve You"]
EXCEPTION_MESSAGE=["Sorry You can try another commands",
                   "I am not able to do that",
                   "Sorry the feature is unavailable"]

def hash_text(sent):
    
    return hashlib.md5(str(sent).encode('utf-8')).hexdigest()[:16]




def refine(sent):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(sent)
    filt_sent = [w for w in word_tokens if not w in stop_words]
    result=dataload.result(filt_sent)
    return(result)

    
    



def process(usersent):
    hashid=hash_text(usersent)
    SQL ="SELECT distinct 1 hashid FROM sentences WHERE hashid = %s;"
    count=cursor.execute(SQL,(hashid))
    if(count>0):
        SQL = "SELECT result FROM sentences WHERE hashid = %s ;"
        cursor.execute(SQL,(hashid))
        row=cursor.fetchall()
        for i in row:
            return(i["result"])
        
    else:
        SQL ="INSERT INTO sentences (hashid, sentence) VALUES (%s, %s);"
        cursor.execute(SQL,(hashid,usersent))
        print("BOT>> TRAIN OR SEARCH")
        regexptrain=re.compile(r'train')
        regexpsearch=re.compile(r'search')
        userinput=input(">>> ").strip()
        if  regexptrain.search(userinput.lower()):
            print("BOT>> Please  enter the answer to train me")
            ans=input(">>> ").strip()
            SQL="UPDATE sentences SET result= %s WHERE hashid=%s "
            cursor.execute(SQL,(ans,hashid))
            return("Thankyou For Training Me")
        elif regexpsearch.search(userinput.lower()):
            botsent=refine(usersent)
            SQL="UPDATE sentences SET result= %s WHERE hashid=%s "
            cursor.execute(SQL,(botsent,hashid))
            return(botsent)
            
    




if __name__=="__main__":
    
    conf =utils.get_config()
    
    DBHOST = conf["MySQL"]["server"]
    DBUSER = conf["MySQL"]["dbuser"]
    DBNAME = conf["MySQL"]["dbname"]
    
    print("BOT ONLINE...")
    
    print("Connecting to database...")
    connection=utils.db_connection(DBHOST,DBUSER,DBNAME)
    cursor =connection.cursor()
    connectionID=utils.db_connectionID(cursor)
    print("...connected")
    
    botsentence=random.choice(BOT_MESSAGE)
    while True:
        
        if(botsentence==None):
            print("BOT>> ",random.choice(EXCEPTION_MESSAGE))
        else:
            print("BOT>> ",botsentence)
        
        usersent=input('>>> ').strip()
        if usersent =='' or usersent.strip(punctuation).lower() == 'quit' or usersent.strip(punctuation).lower() == 'exit':
            print("BOT>> Thank You For Using Me")
            break
        
        botsentence=process(usersent)
        connection.commit()