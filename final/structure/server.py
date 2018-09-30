from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def user():
	return render_template('index.html')

@app.route('/personal')
def personal():
	return render_template('personal.html')

@app.route('/personal_submit', methods = ['POST'])
def personal_submit():
	name = request.form['name']
	school = request.form['school']
	department = request.form['department']
	age = request.form['age']
	contact = request.form['contact']
	email = request.form['email']
	return render_template('personal_submit.ejs', name=name, school=school, department=department, age=age, contact=contact, email=email)

@app.route('/question')
def question():
	return render_template('question.html')

@app.route('/question_submit', methods = ['POST'])
def question_submit():
	nameq = request.form['nameq']
	content = request.form['content']
	return render_template('question_submit.ejs', nameq=nameq, content=content)

@app.route('/survey')
def survey():
	return render_template('survey.html')

@app.route('/survey_submit', methods = ['POST'])
def survey_submit():
	understand = request.form['understand']
	helping = request.form['helping']
	hard = request.form['hard']
	environment = request.form['environment']
	satisfy = request.form['satisfy']
	suggestion = request.form['suggestion']
	return render_template('survey_submit.ejs', understand=understand, helping=helping, hard=hard, environment=environment, satisfy=satisfy, suggestion=suggestion)


@app.route('/quiz')
def quiz():
	return render_template('quiz.html')

@app.route('/quiz_submit', methods = ['POST'])
def quiz_submit():
	name = request.form['name']
	quiz = request.form['quiz']
	return render_template('quiz_submit.ejs', name=name, quiz=quiz)
  
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
