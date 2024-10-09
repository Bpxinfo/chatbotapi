
from flask import Flask,session, request, Response,jsonify
from flask_cors import CORS
import time
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'working'
    
@app.route('/chat', methods=['POST'])   
def sample_chat_completions():
    import os

    try:
        endpoint ="https://Phi-3-small-128k-instruct-zqhas.eastus2.models.ai.azure.com"
        key =os.getenv("PHI3_API_KEY")
    except KeyError:
        print("Missing environment variable 'AZURE_AI_CHAT_ENDPOINT' or 'AZURE_AI_CHAT_KEY'")
        print("Set them before running this sample.")
        exit()

    # [START chat_completions]
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential

    client = ChatCompletionsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    response = client.complete(
        messages=[
            SystemMessage(content="You are a helpful assistant."),
            UserMessage(content="How many feet are in a mile?"),
        ]
    )

    #print(response.choices[0].message.content)
    return jsonify({'response': response.choices[0].message.content})
    # [END chat_completions]



if __name__ == '__main__':
    app.run(debug=True)
