from flask import Flask, jsonify, request
app = Flask(__name__)



@app.route('/todos', methods=['GET'])
def todo():
  json_text = jsonify(todo)
  return json_text

todos = [
  { "label": "My first task", "done": False }
]

todos = todos.json

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

# request_body ={
#    "done": true,
#    "label": "Sample Todo 1"
#    }

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)