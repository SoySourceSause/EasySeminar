from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)

# <script src="https://www.gstatic.com/firebasejs/5.5.1/firebase.js"></script>
# <script>
#   // Initialize Firebase
#   var config = {
#     apiKey: "AIzaSyDNDOB8eIWBpTMTC-6___j7whWTHNtW0rU",
#     authDomain: "easyseminar5000.firebaseapp.com",
#     databaseURL: "https://easyseminar5000.firebaseio.com",
#     projectId: "easyseminar5000",
#     storageBucket: "easyseminar5000.appspot.com",
#     messagingSenderId: "580693786324"
#   };
#   firebase.initializeApp(config);
# </script>

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
# Use a service account
cred = credentials.Certificate('C:\web\easyseminar2018-80336b25a00f.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# doc_ref = db.collection(u'users').document(u'alovelace-id')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })
  
users_ref = db.collection(u'personal')
docs = users_ref.get()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
  
if __name__ == '__main__':
	app.run(debug=True)
