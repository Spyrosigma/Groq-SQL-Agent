# Groq-SQL-Agent


### How to run locally ?

1. Clone the repo
  ```bash
  https://github.com/Spyrosigma/Groq-SQL-Agent.git
  ```

2. Install necessary modules
  ```bash
  pip install -r requirements.txt
  ```

3. Create a .env file and fill in the creds:
  - GROQ_API_KEY
  - Your Database URL and API key (You've to set it up)

4. There are 2 Agents:
   - Satellite Image Agent
   - Housekeeping Satellite Agent

5. 2 separate python files are there, run them :
  - For houskeeping Agent
    ```bash
    python telementry.py  
    ```
  - For Satellite Image Agent
    ```bash
    python satellite.py
    ```

5. Run the index.html file for Chatbot Interaction.

  
