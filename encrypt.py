from flask import Flask, redirect, url_for, request
app = Flask(__name__)

#returning encrypted string
@app.route('/encrypted/<message>')
def encrypted(message):
	return 'encrypted string: %s' % message

#returning flag or 'Wrong password!'
@app.route('/password/<pssw>')
def checkPassword(pssw):
	return '%s' % pssw

#handeling encryption form
@app.route('/encrypt',methods = ['POST'])
def encrypt():
	user = request.form['encryption']
	return redirect(url_for('encrypted',message=encryptMessage(user)))

#handeling password form
@app.route('/enter',methods=['POST'])
def password():
	answer = request.form['password']
	if answer == 't0mat0Soup':
		return redirect(url_for('checkPassword',pssw='flag = nerdlabrules'))
	else:
		return redirect(url_for('checkPassword',pssw='wrong password!'))

#encryption algorithm
def encryptMessage(mess):
	encryptedMess = list()
	for index,letter in enumerate(list(mess), start=1):
		letterToOrd = ord(letter)
		if index % 2 == 0:
			encryptedMess.append(str(chr(letterToOrd + 6)))
		else:
			encryptedMess.append(str(chr(letterToOrd+2)))
	return ''.join(encryptedMess)

if __name__ == '__main__':
	app.run(debug=True)
