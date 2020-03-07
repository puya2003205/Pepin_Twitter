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

usr_id=api.get_user(screen_name="Puya999").id
directMessage=api.send_direct_message(usr_id, "Acesta este un mesaj")
print("Mesajul a fost trimis")