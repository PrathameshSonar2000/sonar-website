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
Project = [{
          'id' : 1,
          'name': 'Airlines reviews',
          'tools': 'Pandas for preprocessing , matplotlib and seaborn for Visual Analysis , Spacy for preprocessing , Spacy for Word Embedding , KNN for ML classification.',
          'description': 'We will analyse reviews of an Airlines and by using NLP we will build a ML model to predict the ratings based on the reviews.',
          'link': 'https://github.com/PrathameshSonar2000/Airlines_reviews.git'
           },
          {
             'id' : 2,
             'name': 'Band gap prediction',
             'tools': 'Pandas for data preprocessing,feature selection, sklearn for feature scaling ,rdkit (use for chemical formulas to get array of equation of polymer)',
             'description': 'A prediction model using Ridge regression machine learning to predict the band gap of polymers.',
             'link': 'https://github.com/PrathameshSonar2000/Band_gap-prediction-using-machine-learning.git'
           },
          {
             'id' : 3,
             'name': 'Indian Covid-19',
             'tools': 'Python, Pandas, Numpy, Matplotlib, Seaborn',
             'description': 'Exploratory Data Analysis on Indian Covid-19 data by using Jupiter Notebook using Python language used libraries such as pandas, matplotlib ,seaborn and A Dashboard using Power bi.',
             'link': 'https://github.com/PrathameshSonar2000/Indian_covid_19_data-exploratory-data-analysis-.git'
          }
          ] 

@app.route("/")
def hello():
    return render_template('home.html',education=Education, project=Project)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)