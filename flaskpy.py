from flask import Flask
app= Flask(__name__) #creating the Flask object

@app.route('/home')
def home():
    return "hello,welcome to KL"

@app.route('/home/about')
def about():
    return 'Location: Hyderabad'

if __name__=="__main__":
    app.run()