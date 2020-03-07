import os
import tweepy as tw
from ConfigParser import SafeConfigParser

configParser = SafeConfigParser()

configParser.read('config.ini')

consumer_key=configParser.get('config', 'consumer_key')
consumer_secret = configParser.get('config', 'consumer_secret')
access_token_key = configParser.get('config', 'access_token_key')
access_token_secret = configParser.get('config', 'access_token_secret')

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
api.verify_credentials()

usr_id=api.get_user(screen_name="saradagurl").id
directMessage=api.send_direct_message(usr_id, "Bau")
print("Mesajul a fost trimis")

#try:
 #   api.update_status("bau cica bau bau") ##endpoint statuses/update
#except:
 #   print("Nu se posta un nou tweeet")

#try:
 #   api.destroy_status(1236272019819372544)
  #  print("Tweet-ul a fost sters")
#except:
 #   None

#try:
 #   user=api.get_user(screen_name="Puya999") ##inlocuieste parametrul cu user-ul de twitter dorit  #endpoint users/show.json
  #  print("ID-ul intern al user-ului %s" %user.id)
   # print("Followers %s" % user.followers_count)
    #print("Lista prieteni: ")
    #for friend in user.friends():
     #   print friend.screen_name
#except:
 #   print("User-ul specificat nu poate fi gasit")

# print("Lista tweet-uri care contin cuvantul Python")
# search_results=api.search(q="python", count=10) ##q este cuvantul cautat in tweets,iar count reprezinta numerele de rezulate dorite
# for i in search_results:#iterator printre inregistrarile returnate de interogare
    # print("Text %s" %i.text)
    # print("Location %s" % i.user.location)
    # print("Name %s" % i.user.name)
    # print("Data %s" % i.created_at)
    # print("--------------------------------------------------------------")
# 