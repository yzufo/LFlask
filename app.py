from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

if __name__ == '__main__':
    app.run()
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login',next='/'))
#     print(url_for('profile',username='John'))
