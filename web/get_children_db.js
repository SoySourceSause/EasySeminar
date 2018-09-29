// JavaScript Document
(function() {
	
	const config = {
	apiKey: "AIzaSyBvF6B8TvDp43PJgpDMKsSYlDDq9vPJUwE",
	authDomain: "webquickgo.firebaseapp.com",
	databaseURL: "https://webquickgo.firebaseio.com",
	storageBucket: "webquickgo.appspot.com",
	// apiKey: "AIzaSyDQQqY-iNLB8rEUVjIVbalJOXj9RJYrFB8",
 //    authDomain: "easyseminardb.firebaseapp.com",
 //    databaseURL: "https://easyseminardb.firebaseio.com",
 //    projectId: "easyseminardb",
 //    storageBucket: "easyseminardb.appspot.com",
	};
	
	firebase.initializeApp(config);
	//Get elements
	//label에다가 저장한 것이 부모노드.
	label = 'object'
	const prelabel = document.getElementById(label);
	const ulList = document.getElementById('list');
	const test = document.getElementById('test');
	const howmany = document.getElementById('num');
	//Create references
	const dbReflabel = firebase.database().ref().child(label);
	const dbRefList = dbReflabel.child('hehe');

	//Sync object changes
	dbReflabel.on('value', snap => {
		prelabel.innerText = JSON.stringify(snap.val(),null, 3);
	});
	
	//Sync object changes
	dbRefList.on('child_added', snap => {
		const li = document.createElement('li');
		li.innerText = snap.val();
		li.id = snap.key;
		//부모노드를 골라받음
		const pa = document.createElement('li');
		pa.innerText = snap.key;

		//test.appendChild(pa);
		document.getElementById('test').appendChild(pa);
		
		ulList.appendChild(li);
		
	}); 
	dbRefList.on('child_changed', snap => {
		const liChanged = document.getElementById(snap.key);
		liChanged.innerText = snap.val();
	});
	dbRefList.on('child_removed', snap => {
		const liToRemove = document.getElementById(snap.key);
		liToRemove.remove();
	});
	 
	// var numperson = document.getElementById('test')
	// .getElementsByTagName.length;
	// //여기 안된다 ㅠㅠ
	// var subjectListCount = document.getElementId( 'test' ).childen.length;
 //  	document.getElementById('noticenum').innerHTML = subjectListCount


}());
