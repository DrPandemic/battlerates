from dotenv import load_dotenv, find_dotenv
import os
from battlerite_client.client import Client
from src.crawler import Crawler

load_dotenv(find_dotenv())

client = Client(os.environ['battlerite_key'])
crawler = Crawler(client, "real database", 10)
crawler.start()
