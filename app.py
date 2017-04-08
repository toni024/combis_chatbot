from flask import Flask, render_template, send_from_directory
import json

witToken = XGCQNQXGXO6DMGQGPNMYJ2C4HZNKBF5Z

#app = Flask(__name__, static_url_path='/build')
app = Flask(__name__)
debug = True


@app.route("/fetch_api", methods=['POST'])
def api():
    resp_data = {}
    resp_data['name'] = "mihili"
    resp_data['id'] = "2"
    return json.dumps(resp_data)


@app.route('/')
def index():
  return send_from_directory('build/', 'index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)




if __name__ == '__main__':
  app.debug = debug
  app.run()
