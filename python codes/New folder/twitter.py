class TwitterAPI(object):
    """
    TwitterAPI class allows the Connection to Twitter Via oAuth
    once you have registered with Twitter and receive the 
    necessary credentials
    """
    def __init__(self):
        consumer_key = 'get_your_credentials'
        consumer_secret = 'get_your_credentials'
        acess_token = 'get_your_credentials'
        acess_secret = 'get_your_credentials'
        self.consumer_key = consumer_key
        self.consumer_secret=consumer_secret
        self.acess_token=acess_token
        self.acess_secret=acess_secret
        self.ratries=3
        self.auth = twitter.oauth.OAuth(acess_token,acess_secret,
        consumer_key,consumer_secret)
        self.api=twitter.Twitter(auth=self.auth)
        
