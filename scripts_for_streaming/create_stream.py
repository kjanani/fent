# Janani Kalyanam
# August 25, 2016

# Script to collect tweets from the TwitterStreaming API

import os,sys
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


consumer_key = open('keys.csv','r').readlines()[0].strip().split(',')[1];
consumer_secret =  open('keys.csv','r').readlines()[1].strip().split(',')[1];
access_key =  open('keys.csv','r').readlines()[2].strip().split(',')[1];
access_secret =  open('keys.csv','r').readlines()[3].strip().split(',')[1];


class listener(StreamListener):
    
    def __init__(self): # constructor: set counter to 0, and open a file for writing tweets
        self.counter = 0;
        self.output = open('../data/fentanyl' + time.strftime('%Y%m%d-%H%M%S') + '.json','w');

    def on_data(self, data):
        print(data)
        self.output.write(data+'\n');
        self.counter += 1;

        if(self.counter > 20000):
            self.output.close(); # close the previous file
            self.output = open('fentanyl' + time.strftime('%Y%m%d-%H%M%S') + '.json','w'); # open a new one with current timestamp
            self.counter = 0; # reset counter
        return True

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + '\n')
        time.sleep(60)
        return False
    
if __name__ == '__main__':

    l = listener();
    auth = OAuthHandler(consumer_key, consumer_secret);
    auth.set_access_token(access_key, access_secret);
    stream = Stream(auth,l);
    while(1):
        try:
            stream.filter(track=['fentanyl','actiq','duragesic','sublimaze','kill pill'], languages=['en']);
        except:
            continue;
