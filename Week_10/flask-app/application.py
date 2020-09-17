from flask import Flask, render_template
from flask import request
import recom #import all objects from recom.py

app = Flask(__name__) #tell Flask to make THIS script the center of the application

@app.route('/index') #whenever the user visits HOSTNAME:PORT/index, this function is triggered
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations') #python decorater modifies the function that is defined on the next line.
def recommender():
    #ratings = dict(request.args)
    #recommentations = rec.calculate_best_movies(ratings)
    #build this ML function...

    result = recom.random_recommend(4)
    return render_template('recommendations.html', result_html=result)
    #passing the backend python variable to the frontend(html). i.e. the response

if __name__ == '__main__':
    #whatever occurs after this line is executed when we run "python application.py"
    #however, whatever occurs afters this line is NOT executed when we IMPORT application.py

    app.run(debug=True) #this will start an infinite process, i.e. serving our web page.
    #debug mode displays backend errors to the browser
    #Also automatically restarts server upon chanfes to code.
