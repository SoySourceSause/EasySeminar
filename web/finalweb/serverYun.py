from flask import Flask, render_template, request, url_for
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

app = Flask(__name__)

# cred = credentials.Certificate('C:\web\easyseminar2018-80336b25a00f.json')
# firebase_admin.initialize_app(cred)

# db = firestore.client()

# doc_ref = db.collection(u'users').document(u'alovelace-id')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })

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
@app.route('/test')
def test():
	return render_template('test.html')
# Use a service account
# @app.route('/submit', methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['name']
#       return redirect(url_for('success', name = user))
#    else:
#       user = request.args.get('name')
#       return redirect(url_for('success', name = user))
@app.route('/submit', methods = ['POST'])
def submit():
	name = request.form['name']
	return render_template('submit.ejs', name=name)
  
# users_ref = db.collection(u'personal')
# docs = users_ref.get()

# for doc in docs:
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))
  
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
