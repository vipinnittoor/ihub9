from flask import Flask,render_template
app=Flask(__name__)
#app.config['SERVER_NAME'] = '127.0.0.1:5001'
 



@app.route('/')
def index():

    return render_template('index.html')

if __name__=="__main__":

    app.run()
