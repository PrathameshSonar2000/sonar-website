from flask import Flask, render_template 

app = Flask(__name__)

Education = [  {
                'id':1,
                'name': 'Bachelors of Engineering',
                'branch': 'Electronics and Telecommunication',
                'Honours': 'Data Science',
                'year': '2019-2023',
                'mark': '8.1 CGPA',
                'university': 'SPPU'
              },
             {
               'id':2,
               'name': 'Higher Secondary School Certificate (12th)',
               'branch': 'Science',
               'year': '2017-2019',
               'mark': '60%',
               'university': 'Marathwada, Aurangabad'
             },
             {
               'id':3,
               'name': 'Secondary School Certificate (10th)',
               'year': '2006-2016',
               'mark': '9.8 CGPA',
               'university': 'CBSE'
             }
            ]

@app.route("/")
def hello():
    return render_template('home.html',education=Education)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)