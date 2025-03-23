import json
#import argparse
import requests
import time

def out(model,message,port,max_tokens,temp=0.1):
    # Set up the argument parser
    #parser = argparse.ArgumentParser(description="Chat with vLLM API.")
    #parser.add_argument('--max-tokens', type=int, default=100, help="The maximum number of tokens in the response.")
    #parser.add_argument('--message', type=str, required=True, help="The message to send to the model.")
    # Parse the arguments
    #args = parser.parse_args()
    #print(args.message)
    
    url = str("http://localhost:"+port+"/v1/chat/completions")  # replace with the actual endpoint
    
    payload = {
        "model": model,  # replace with your actual model name
        "messages": [
            {"role": "user", "content": message}
        ],
        "long-prefill-token-threshold": max_tokens,
        "max_tokens":max_tokens,
        #"min_tokens":args.max_tokens-1,
        "temperature":temp
    }
    
    headers = {"Content-Type": "application/json"}
    
    start=time.time()
    response = requests.post(url, json=payload, headers=headers)
    json_string = response.json()  # print the response from the server

    return json_string 
    #return json_string["choices"][0]["message"]["content"]
