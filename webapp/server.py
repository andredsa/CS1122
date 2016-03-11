from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('cs1122_web_test.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
