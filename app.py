from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("ipl_model.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # X_test columns : -
        # ['bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils',
        #  'bat_team_Kings XI Punjab', 'bat_team_Kolkata Knight Riders',
        #  'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',
        #  'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',
        #  'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils',
        #  'bowl_team_Kings XI Punjab', 'bowl_team_Kolkata Knight Riders',
        #  'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',
        #  'bowl_team_Royal Challengers Bangalore',
        #  'bowl_team_Sunrisers Hyderabad', 'overs', 'runs', 'wickets',
        #   'runs_last_5', 'wickets_last_5']

        bat_team_Chennai = 0
        bat_team_Delhi = 0
        bat_team_Kings = 0
        bat_team_Kolkata = 0
        bat_team_Mumbai = 0
        bat_team_Rajasthan = 0
        bat_team_Royal = 0
        bat_team_Sunrisers = 0

        bowl_team_Chennai = 0
        bowl_team_Delhi = 0
        bowl_team_Kings = 0
        bowl_team_Kolkata = 0
        bowl_team_Mumbai = 0
        bowl_team_Rajasthan = 0
        bowl_team_Royal = 0
        bowl_team_Sunrisers = 0


        bat_team=request.form['batting-team']
        if(bat_team=='Mumbai Indians'):
            bat_team_Mumbai = 1

        elif (bat_team == 'Kolkata Knight Riders'):
            bat_team_Kolkata = 1

        elif (bat_team == 'Chennai Super Kings'):
            bat_team_Chennai = 1

        elif (bat_team == 'Rajasthan Royals'):
            bat_team_Rajasthan = 1

        elif (bat_team == 'Kings XI Punjab'):
            bat_team_Kings = 1

        elif (bat_team == 'Royal Challengers Bangalore'):
            bat_team_Royal = 1

        elif (bat_team == 'Delhi Daredevils'):
            bat_team_Delhi = 1

        elif (bat_team == 'Sunrisers Hyderabad'):
            bat_team_Sunrisers = 1

        #bowl_team
        bowl_team = request.form['bowling-team']
        if (bowl_team == 'Mumbai Indians'):
            bowl_team_Mumbai = 1

        elif (bowl_team == 'Kolkata Knight Riders'):
            bowl_team_Kolkata = 1

        elif (bowl_team == 'Chennai Super Kings'):
            bowl_team_Chennai = 1

        elif (bowl_team == 'Rajasthan Royals'):
            bowl_team_Rajasthan = 1

        elif (bowl_team == 'Kings XI Punjab'):
            bowl_team_Kings = 1

        elif (bowl_team == 'Royal Challengers Bangalore'):
            bowl_team_Royal = 1

        elif (bowl_team == 'Delhi Daredevils'):
            bowl_team_Delhi = 1

        elif (bowl_team == 'Sunrisers Hyderabad'):
            bowl_team_Sunrisers = 1


        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])

        runsprev5over = int(request.form['runsprev5over'])
        wicketsprev5over = int(request.form['wicketsprev5over'])


        
        prediction=model.predict([[
            bat_team_Chennai,
            bat_team_Delhi,
            bat_team_Kings,
            bat_team_Kolkata,
            bat_team_Mumbai,
            bat_team_Rajasthan,
            bat_team_Royal,
            bat_team_Sunrisers,
            bowl_team_Chennai,
            bowl_team_Delhi,
            bowl_team_Kings,
            bowl_team_Kolkata,
            bowl_team_Mumbai,
            bowl_team_Rajasthan,
            bowl_team_Royal,
            bowl_team_Sunrisers,
            overs,
            runs,
            wickets,
            runsprev5over,
            wicketsprev5over
        ]])

        if(bat_team ==bowl_team) :
            return render_template('home.html', prediction_text="Plz select bat-team and bowl-team different")

        if (overs<5.0 or overs>20.0):
            return render_template('home.html', prediction_text="Plz enter correct overs value")

        if (wicketsprev5over > wickets):
            return render_template('home.html', prediction_text="current wickets can not be less then prev 5 overs wickets")

        if (runsprev5over > runs):
            return render_template('home.html', prediction_text="current runs can not be less then prev 5 overs runs")

        output=int(prediction[0])

        return render_template('home.html',prediction_text="Predicted score :  {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
