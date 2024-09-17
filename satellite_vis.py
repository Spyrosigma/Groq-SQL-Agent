from supabase import create_client, Client
import supabase
import os
import matplotlib.pyplot as plt
import seaborn as sns
import uuid
from collections import Counter


SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def gen_graphs(query):
    pass