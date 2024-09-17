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
    if query == 'Plot the uptime of the system over the month of December 2016.':
        response = supabase.table("telemetry_data").select("timestamp","calibrated_value").eq("name", "eps_power").execute()

        print(response.data)
        values = response.data

        timestamps = [value['timestamp'] for value in values]
        calibrated_values = [value['calibrated_value'] for value in values]

        plt.plot(timestamps, calibrated_values)
        plt.xlabel('Timestamp')
        plt.ylabel('EPS Power')
        plt.title('EPS_Power vs Timestamp')
        a = uuid.uuid4()
        plt.savefig(f'{a}.jpg')
        unique_filename = f'{a}.jpg'
        plt.savefig(f'/charts/{unique_filename}')
        plt.close()
        
        return unique_filename

        # UPLOAD AND SEND BACK PUBLIC URL LINK HERE
        '''
        with open(unique_filename, 'rb') as f:
                    supabase.storage.from_("Gig1 - Graphs").upload(
                        file=f,
                        path=f"{unique_filename}", 
                        file_options={"content-type": "image/*"}
                    )

        # Get public URL for the uploaded file
        file_url = supabase.storage.from_("Gig1 - Graphs").get_public_url(
            f"{unique_filename}"
        )
        
        '''
        # emit('bot-response', {'data': file_url} ,room=user_id)
    
    elif query == 'Generate a box plot of battery levels throughout December.':
        response = supabase.table("telemetry_data").select("timestamp", "calibrated_value").eq("name", "eps_battery").execute()

        values = response.data
        battery_levels = [float(value['calibrated_value']) for value in values]

        plt.figure(figsize=(10, 6))
        plt.boxplot(battery_levels)
        plt.title('Battery Levels Throughout December')
        plt.ylabel('Battery Level')
        plt.xlabel('December')

        unique_filename = f'{uuid.uuid4()}.jpg'

        plt.savefig(f'/charts/{unique_filename}')
        plt.close()
        return unique_filename
        
        # emit('bot-response', {'data': file_url} ,room=user_id)

    elif query == "Create a pie chart of the most common system messages in December.":
        response = supabase.table("telemetry_data").select("name").execute()

        messages = [item['name'] for item in response.data]

        message_counts = Counter(messages)

        top_messages = dict(message_counts.most_common(10))


        labels = list(top_messages.keys())
        sizes = list(top_messages.values())

        plt.figure(figsize=(12, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal') 
        plt.title('Top 10 Most Common System Messages in December')

        unique_filename = f'{uuid.uuid4()}.jpg'

        plt.savefig('charts/'f'{unique_filename}', bbox_inches='tight')
        plt.close()

        return unique_filename
        


query = 'Plot the uptime of the system over the month of December 2016.'
# query = 'Generate a box plot of battery levels throughout December.'
# query = 'Create a pie chart of the most common system messages in December.'
gen_graphs(query)