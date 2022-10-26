import boto3
from botocore.client import Config
import json
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from sqlalchemy import create_engine
from sqlalchemy import inspect
import time
import urllib.request


class Loader():
    def __init__(self):
        self.link_list = []
        self.product_list =[]
    def create_directory(self):
        '''Creates directory'''
        os.chdir("C:\\Users\\awoye\\OneDrive\\Documents\\GitHub\\data-collection-pipeline782")
        try:
            os.mkdir('raw_data')
        except:
            pass


    def load_data_to_json(self):
        '''Saves dictionary of product text data as a json file'''   
        os.chdir('C:\\Users\\awoye\\OneDrive\Documents\\GitHub\\data-collection-pipeline782\\raw_data')
        with open('C:\\Users\\awoye\\OneDrive\\Documents\\GitHub\\data-collection-pipeline782\\raw_data\\data.json','w') as f:
            json.dump(self.product_list,f) 


    def upload_raw_data(self):
        '''
        Uploads raw data to S3
        '''
        ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
        ACCESS_SECRET_KEY =os.environ['ACCESS_SECRET_KEY']
        BUCKET_NAME = 'waterstones-data'

        data=open('data.json','rb')

        s3 = boto3.resource(
            's3',
            aws_access_key_id = ACCESS_KEY_ID,
            aws_secret_access_key = ACCESS_SECRET_KEY,
            config = Config(signature_version = 's3v4'))
        s3.Bucket(BUCKET_NAME).put_object(Key = 'data.json', Body = data)
        print("Data sent to S3!")
    

    def make_pandas_dataframe(self):
        self.df = pd.DataFrame(self.product_list)
    

    def load_to_sql(self):
        '''
        Loads dataframe into PostgresSQl
        '''
        print("Connecting to database")
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'database-1.czkh6nyqipgc.eu-west-2.rds.amazonaws.com'
        USER = 'postgres'
        PASSWORD = PASSWORD
        DATABASE = 'postgres'
        PORT = 5432
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        engine.connect()
        try:
            old_info = pd.read_sql_table('waterstones_data',con = engine)
            merged_data = pd.concat([old_info, self.df])
            new_data = merged_data.drop_duplicates(keep=False)
            new_data.to_sql('waterstones_data',engine,if_exists ='append', index = False)
        except Exception:
            self.df.to_sql('waterstones_data',engine,if_exists ='append', index = False)
        finally:
            old_info = pd.read_sql_table('waterstones_data',con = engine)
            merged_data = pd.concat([old_info, self.df])
            new_data = merged_data.drop_duplicates(keep=False)
            new_data.to_sql('waterstones_data',engine,if_exists ='append', index = False)