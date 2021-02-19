# IPL-First-Inning-Score-Predictor-App

This application tell us about the predicted score for first inning by giving last 5 over details (runs made in last 5 overs and wickets taken in last 5 overs).

The App Link :    https://ipl-score-prediction-akd-app.herokuapp.com/

Application Video link : https://drive.google.com/file/d/1wGnJ5B0Rv1TKD8BIKmWgwf-inlVjM7Jc/view?usp=sharing

Some Glimpses of Application : 

![rcd1](https://user-images.githubusercontent.com/61588604/108326757-a3da1400-71f0-11eb-8c59-7f3afb6d550b.png)


![rcd2](https://user-images.githubusercontent.com/61588604/108327460-73df4080-71f1-11eb-9d0d-cf0c6e7c5ac2.png)

![rcd3](https://user-images.githubusercontent.com/61588604/108327518-848fb680-71f1-11eb-8a70-0baec5c1d487.png)




Journey : 

**1) Data Collection** :  Data collected from the Kaggle . 

    -->about data : Data Columns are : mid(match number) ,date, venue, bat_team, bowl_team , batsman, bowler, runs, wickets, overs, run_last_5(runs made in last 5      overs),wickets_last_5(wickets taken in last 5 overs), non_striker and total score of that match .
    
    --> As a data scientist, we will predict the total predicted score for first inning when user give some input .(input : select teams for batting and bowling and current runs , wickets and overs  and runs & wickets in last 5 overs .)
    
    Assumption : all batsman and bowlers have same capability and  there is no effect of venue)
    
**2) Data Preprocessing** : 

    -first of all , deleted all unused columns(mid,date,venue,batsman ,bowler) from dataset. and cleaned from null values.
    
    -then I used one-hot-encoding for "bat_team" and "bowl_team" columns.
    
**3) Model building** : 

    a) split the dataset into X(independent features) and y(dependent features) .
    
    b) perform train_test_split
    
    c) try linear regression , lasso regression, ridge regression, RandomForestRegressor with hyperparameter tuning. 
    
    d) obsered that linear regression has highest score and lowest error . so save this model using pickle.

**4) Model deployment** : 
    a) using flask framework , we deployed this model on HEROKU platform .
    
App link : https://ipl-score-prediction-akd-app.herokuapp.com/
    
    
