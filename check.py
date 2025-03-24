from flask import Flask, render_template, request, session, jsonify
from res import out
import os
import math

global initial_name

initial_name = ""
max_tokens=0

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session to work

# Initialize models in session
@app.before_request
def initialize_models():
    if 'models' not in session:
        session['models'] = ["meta-llama/Meta-Llama-3.1-70B-Instruct", 
                             "meta-llama/Llama-3.1-8B-Instruct"
                             ]
    if 'chat_history' not in session:
        session['chat_history'] = []

# Finding the model parameters
base_para = 20

#ports
ports=[8079]
used_ports=set()
used_models={}

def para(model, start='b', end='-'):
    out = ''
    flag = 0
    for i in model[::-1]:
        if i == end and flag == 1:
            try:
                return math.ceil(float(out))
            except:
                flag=0
        if flag == 1:
            out = i + out
        if i.upper() == start.upper():
            flag = 1 
    return 0

@app.route('/')
def index():
    global initial_name
    if initial_name=="":
        selected_model = session['models'][0]  # Default model
        
    selected_model=initial_name

    # Pass the current chat history and models to the template
    return render_template('check.html', 
                           models=session['models'], 
                           selected_model=selected_model, 
                           chat_history=session['chat_history'])

@app.route('/chat', methods=['POST'])
def chat():
    global initial_name

    user_message = request.form.get('message', '')
    selected_model = request.form.get('model', session['models'][0])  # Default model

    initial_name = selected_model
    if initial_name not in used_models:
        # initial_name = selected_model
        #os.system('kill -9 $(lsof -t -i:8080)')
        # Simulate model serving (replace with actual model interaction)
        # if initial_name not in used_models:
        used_models[initial_name]=str(ports[-1]+1)
        ports.append(ports[-1]+1)
            
        n_gpus= math.ceil(para(initial_name)/base_para)
        if n_gpus==0:
            n_gpus=1
        elif n_gpus!=1 and n_gpus%2!=0:
            n_gpus+=1
            
        os.system("VLLM_SKIP_WARMUP=true vllm serve " + initial_name + " --disable_log_requests --trust-remote-code --port "+used_models[initial_name]+" --tensor-parallel-size "+str(n_gpus))
    
    
    # Simulating a response (Replace with actual model interaction)
    try:
        print("max_tokens: ", session['max_tokens'],session['temp'])
        out_put = out(selected_model, user_message,used_models[initial_name],session['max_tokens'],session['temp'])
    except:
        out_put = out(selected_model, user_message,used_models[initial_name],50,0.1)
    
    # print(out_put)
    bot_message=out_put["choices"][0]["message"]["content"]
    # bot_message = out(selected_model, user_message,used_models[initial_name],256)
    
    # Store user and bot messages in session chat history
    session['chat_history'].append(('You', user_message))
    session['chat_history'].append((selected_model, bot_message))

    session.modified = True

    return render_template('check.html', 
                           models=session['models'], 
                           selected_model=selected_model, 
                           chat_history=session['chat_history'], 
                           user_message=user_message, 
                           bot_message=bot_message)

@app.route('/add_model', methods=['POST'])
def add_model():
    model_name = request.json.get('model')
    if model_name and model_name not in session['models']:
        session['models'].append(model_name)
        session.modified = True
        return jsonify({'status': 'success', 'models': session['models']})
    return jsonify({'status': 'error', 'message': 'Model name is invalid or already exists.'})

@app.route('/delete_model', methods=['POST'])
def delete_model():
    model_name = request.json.get('model')
    if model_name in session['models']:
        session['models'].remove(model_name)
        session.modified = True
        return jsonify({'status': 'success', 'models': session['models']})
    return jsonify({'status': 'error', 'message': 'Model not found.'})

@app.route('/max_tokens',methods=['POST'])
def tokens():
    max_tokens = request.form.get('max_tokens',type=int)
    # Modify the session (assuming you're storing max_tokens in the session)
    session['max_tokens'] = max_tokens
    session.modified = True
    return '', 204

@app.route('/update_slider', methods=['POST'])
def update_slider():
    data = request.get_json()
    try:
        session['temp'] = data.get('temp', session['temp'])
    except:
        session['temp'] = data.get('temp', 0.1)
        
    session.modified = True
    # Optionally, you can process the slider value here (e.g., update in a database, etc.)
    return '', 204
    
if __name__ == '__main__':
    app.run(debug=True)
