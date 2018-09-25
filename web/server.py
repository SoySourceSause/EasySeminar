from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def user():
	return render_template('user.html')

@app.route('/personal')
def personal():
	return render_template('personal.html')

@app.route('/question')
def question():
	return render_template('question.html')

@app.route('/survey')
def survey():
	return render_template('survey.html')

@app.route('/quiz')
def quiz():
	return render_template('quiz.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
