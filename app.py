from flask import Flask, render_template, request
from res import out

app = Flask(__name__)

@app.route('/')
def index():
    models = ["meta-llama/Meta-Llama-3.1-70B-Instruct","GPT-3", "GPT-4", "GPT-4 Turbo", "Codex"]
    selected_model = models[0]  # Default model (could be set to the first model)
    return render_template('index.html', models=models, selected_model=selected_model)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message', '')
    selected_model = request.form.get('model', 'meta-llama/Meta-Llama-3.1-70B-Instruct')  # Default to GPT-3 if no model is selected

    # Simulating a response (Replace with actual model interaction)
    bot_message= out(selected_model,user_message,1024)["choices"][0]["message"]["content"]
    #bot_message = f"Response from {selected_model} for: {user_message}"

    return render_template(
        'index.html',
        models=["meta-llama/Meta-Llama-3.1-70B-Instruct", "GPT-3", "GPT-4", "GPT-4 Turbo", "Codex"],
        user_message=user_message,
        bot_message=bot_message,
        selected_model=selected_model
    )

if __name__ == '__main__':
    app.run(debug=True)

