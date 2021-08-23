'''
@Author: Swapnil Bhoyar
@Date: 2021-08-22
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-08-22
@Title : Program to count receive socket from socket and analyze twitter data.
'''
import socket
from  textblob import TextBlob
import csv

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',9998))
pos=0
neg=0
tweet_count=0
opinion = ["pos","neg","tweet_count"]
while True:
    full_msg = ''
    new_msg = True
    with open('twitter_data.csv', 'w') as csv_file:
      csv_writer = csv.DictWriter(csv_file, fieldnames=opinion)
      csv_writer.writeheader()
    while True:
        with open('twitter_data.csv', 'a') as csv_file:
            msg = s.recv(1000)
            msg=msg.decode("utf-8")
            analysis=TextBlob(msg) # here it will apply NLP\
            print(analysis.sentiment)
            tweet_count=tweet_count+1
            # now checking polarity only
            if analysis.sentiment.polarity > 0:
                pos=pos+1
            if analysis.sentiment.polarity < 0:
                neg =neg+1
            csv_writer = csv.DictWriter(csv_file, fieldnames=opinion)
            info = {
                    "pos": pos,
                    "neg": neg,
                    "tweet_count":tweet_count
                    }
            csv_writer.writerow(info)
            print(pos, neg)
            
        new_msg = True
        full_msg = ""
        