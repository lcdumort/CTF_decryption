from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/encrypted/<message>')
def encrypted(message):
	return 'welcome %s' % message

@app.route('/encrypt',methods = ['POST'])
def test():
	print('this is a test')
	#else:
	#	user = request.args.get('encryption')
	#	return redirect(url_for('encrypted',message=user))
def encrypt():
	if request.method == 'POST':
		user = request.form['encryption']
		print(user)
		return redirect(url_for('encrypted',message=user))

if __name__ == '__main__':
	app.run(debug=True)
