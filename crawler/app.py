import os
from battlerite_client.client import Client
from src.crawler import Crawler

client = Client(os.environ['battlerite_key'])
crawler = Crawler(client, "real database", 10)
crawler.start()
