import urllib
import json
import csv
import http
import io
from urllib.request import urlopen
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import pandas as pd
import time
import arrow
from datetime import datetime,date,timedelta 
import requests
import logging
import time

log_file_name = "logger" + ".log"
logger = logging.getLogger(log_file_name)
hdlr = logging.FileHandler(log_file_name)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)
bucket_name = "sumedhprithvijsss"
initial_file = "TX_170617_WBAN_13910.csv"
initial_local = "initial.csv"
file_name = ""
name_list = []
with open('config.json') as data_file:    
        data1 = json.load(data_file)
links = data1['links']['array']

present_link = data1['presentDataLinkToBeAdded'] 
conn = S3Connection(data1['AWSAccess'], data1['AWSSecret'])
print("Established connection to S3")
logger.info("Established connection to S3")
seq =  (data1['state'],arrow.now().format('DDMMYY'),data1['stationID'])
file_name = "_".join(seq)
file_name = file_name + '.csv'
df = []
nonexistent = conn.lookup(bucket_name)


def initialize_bucket():
    if nonexistent is None:
        logger.info("creating new bucket with name " + bucket_name)
        conn.create_bucket(bucket_name)
        existingbucket = conn.get_bucket(bucket_name)
        initial_data = Key(existingbucket)
        initial_data.key = initial_file
        for url in links:
            response = urlopen(url)        
            html = response.read()
            with open(initial_local, 'ab') as f:
                f.write(html)    
        initial_data.set_contents_from_filename(initial_local)
        responsenew = urlopen(present_link)  
        htmlnew = responsenew.read()
        with open(file_name, 'ab') as f:
            f.write(htmlnew)
        print("Read new file from "+present_link+" and copied to local")    
        logger.info("Read new file from "+present_link+" and copied to local")   
        df3 = pd.read_csv(initial_local,low_memory=False,header = 0)
        df4 = pd.read_csv(file_name,low_memory=False,header = 0)
        frames2 = [df3, df4]
        result2 = pd.concat(frames2,join='outer')
        result2.to_csv(file_name)
        new_link_data = Key(existingbucket)
        new_link_data.key = file_name    
        new_link_data.set_contents_from_filename(file_name)
    else:
        existingbucket = conn.get_bucket(bucket_name)
        print("Bucket exists with name " + bucket_name)
        logger.info("Bucket exists with name " + bucket_name)
    return  existingbucket


existingbucket = initialize_bucket()
file_exists = False            
for key in existingbucket.list():
    if key.name == file_name:
        file_exists = True
        print("Todays File is created or already present ")
        logger.info("Todays File is created or already present")
    name_list.append((key.name)[3:9])


now = datetime.now()
youngest = max(dt for dt in name_list if dt < str(now))

def get_new_file(new_file_link):
    responsenew = urlopen(new_file_link)  
    htmlnew = responsenew.read()
    with open(file_name, 'ab') as f:
        f.write(htmlnew)
    print("Read new file from "+new_file_link+" and copied to local")    
    logger.info("Read new file from "+new_file_link+" and copied to local")    
    return 

def create_and_append_file():
    for key in existingbucket.list():
        if (key.name)[3:9] == youngest:
            print(key.name)
            print(file_name)
            new_data = Key(existingbucket)
            new_data.key = key.name    
            new_data.set_contents_from_filename(key.name)  
            df1 = pd.read_csv(new_data,low_memory=False,header = 0)
            df2 = pd.read_csv(file_name,low_memory=False,header = 0)
            frames1 = [df1, df2]
            result1 = pd.concat(frames1,join='outer')
            result1.to_csv(file_name)
            print("Appended data from file -" + key.name + " to create new file with name - " + file_name)
            logger.info("Appended data from file -" + key.name + " to create new file with name - " + file_name)
            subsequent_data = Key(existingbucket)
            subsequent_data.key = file_name        
            subsequent_data.set_contents_from_filename(file_name)
            print("Pushed file to S3")
            logger.info("Pushed file to S3")            
    return

   


if not file_exists:
    get_new_file(present_link)
    create_and_append_file()