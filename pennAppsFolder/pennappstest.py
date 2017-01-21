# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import SelectField, SubmitField
#from wtforms.validators import Required, Length
import random, json
import plotly.plotly
import plotly.graph_objs as go
#import pandas as pd


import plotly.tools as tls
tls.set_credentials_file(username='nmamadeo', api_key='9eLPzUvSLGlWKczFs2ig')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
bootstrap = Bootstrap(app)

countsDct = {'Alabama': [84.3,23.5,11.8,11.9,18.5],
'Alaska': [92.1,28,8.1,16.4,10.3],
'Arizona': [86,27.5,8.2,12.8,17.4],
'Arkansas': [84.8,21.1,12.3,11.1,19.1],
'California': [81.8,31.4,6.8,9.7,15.3],
'Colorado': [90.7,38.1,7.2,9.2,11.5],
'Connecticut': [89.9,37.6,7.1,6.9,10.5],
'Delaware': [88.4,30,8.5,6.8,12.4],
'Florida': [86.9,27.3,8.5,16.2,15.7],
'Georgia': [85.4,28.8,8.8,15.7,17],
'Hawaii': [91,30.8,6.5,4.7,10.6],
'Idaho': [89.5,25.9,9,12.9,15.1],
'Illinois': [87.9,32.3,7.1,8.1,13.6],
'Indiana': [87.8,24.1,9.7,11.2,14.5],
'Iowa': [91.5,26.7,7.9,5.9,12.2],
'Kansas': [90.2,31,8.6,10.6,13],
'Kentucky': [84.2,22.3,12.9,7,18.5],
'Louisiana': [83.4,22.5,11,13.8,19.6],
'Maine': [91.6,29,11.9,10.3,13.4],
'Maryland': [89.4,37.9,7.1,7.5,9.7],
'Massachusetts': [89.8,40.5,7.9,3.3,11.5],
'Michigan': [89.6,26.9,10.3,7.1,15.8],
'Minnesota': [92.4,33.7,7.1,5.2,10.2],
'Mississippi': [82.3,20.7,11.9,14.8,22],
'Missouri': [88.4,27.1,10.4,11.4,14.8],
'Montana': [92.8,29.5,9.1,14,14.6],
'Nebraska': [90.7,29.3,7.3,9.5,12.6],
'Nevada': [85.1,23,9,14,14.7],
'New Hampshire': [92.3,34.9,8.5,7.5,8.2],
'New Jersey': [88.6,36.8,6.6,10,10.8],
'New Mexico': [84.2,26.3,10.1,12.8,20.4],
'New York': [85.6,34.2,7.4,8.1,15.4],
'North Carolina': [85.8,28.4,9.6,13.1,16.4],
'North Dakota': [91.7,27.7,6.8,8.9,11],
'Ohio': [89.1,26.1,9.9,7.6,14.8],
'Oklahoma': [86.9,24.1,11.3,16.2,16.1],
'Oregon': [89.8,30.8,10.2,8.3,15.4],
'Pennsylvania': [89.2,28.6,9.5,7.5,13.2],
'Rhode Island': [86.2,31.9,8.9,6.7,13.9],
'South Carolina': [85.6,25.8,10.3,12.9,16.6],
'South Dakota': [90.9,27,8.4,12,13.7],
'Tennessee': [85.5,24.9,11.2,12,16.7],
'Texas': [81.9,27.6,8.1,19.1,15.9],
'Utah': [91.2,31.1,6.6,11.5,11.3],
'Vermont': [91.8,36,10,4.6,10.2],
'Virginia': [88.3,36.3,7.7,10.5,11.2],
'Washington': [90.4,32.9,8.9,7.6,12.2],
'West Virginia': [85,19.2,14.4,7.2,17.9],
'Wyoming': [92.3,25.7,8.5,13.4,11.1],
'Wisconsin': [91,27.8,8.2,6.6,12.1]}


def make_bar_chart(choice, state):
    trace1 = go.Bar(
        x=['% over age 25 with HS diploma', '% with Bachelor\'s or higher', '% under 65 with a disability', '% without health insurance', '% in poverty'],
        y=countsDct[choice],
        name= choice
    )
    trace2 = go.Bar(
        x=['% over age 25 with HS diploma', '% with Bachelor\'s or higher', '% under 65 with a disability', '% without health insurance', '% in poverty'],
        y=countsDct[state],
        name= state
    )
    graphs = [ dict (data = [trace1, trace2], layout = go.Layout( barmode = 'group') )]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON)
    return graphJSON

class ChoiceForm(Form):
    
    choice = SelectField(u'Your state', choices=[("blank", "Make a choice"), ('Alabama','Alabama'),
('Alaska','Alaska'),
('Arizona','Arizona'),
('Arkansas','Arkansas'),
('California','California'),
('Colorado','Colorado'),
('Connecticut','Connecticut'),
('Delaware','Delaware'),
('Florida','Florida'),
('Georgia','Georgia'),
('Hawaii','Hawaii'),
('Idaho','Idaho'),
('Illinois','Illinois'),
('Indiana','Indiana'),
('Iowa','Iowa'),
('Kansas','Kansas'),
('Kentucky','Kentucky'),
('Louisiana','Louisiana'),
('Maine','Maine'),
('Maryland','Maryland'),
('Massachusetts','Massachusetts'),
('Michigan','Michigan'),
('Minnesota','Minnesota'),
('Mississippi','Mississippi'),
('Missouri','Missouri'),
('Montana','Montana'),
('Nebraska','Nebraska'),
('Nevada','Nevada'),
('New Hampshire', 'New Hampshire'),
('New Jersey', 'New Jersey'),
('New Mexico', 'New Mexico'),
('New York', 'New York'),
('North Carolina', 'North Carolina'),
('North Dakota', 'North Dakota'),
('Ohio','Ohio'),
('Oklahoma','Oklahoma'),
('Oregon','Oregon'),
('Pennsylvania','Pennsylvania'),
('Rhode Island', 'Rhode Island'),
('South Carolina', 'South Carolina'),
('South Dakota', 'South Dakota'),
('Tennessee','Tennessee'),
('Texas','Texas'),
('Utah','Utah'),
('Vermont','Vermont'),
('Virginia','Virginia'),
('Washington','Washington'),
('West Virginia','West Virginia'),
('Wyoming','Wyoming'),
('Wisconsin','Wisconsin')])
    
    state = SelectField(u'States', choices=[("blank", "Make a choice"), ('Alabama','Alabama'),
('Alaska','Alaska'),
('Arizona','Arizona'),
('Arkansas','Arkansas'),
('California','California'),
('Colorado','Colorado'),
('Connecticut','Connecticut'),
('Delaware','Delaware'),
('Florida','Florida'),
('Georgia','Georgia'),
('Hawaii','Hawaii'),
('Idaho','Idaho'),
('Illinois','Illinois'),
('Indiana','Indiana'),
('Iowa','Iowa'),
('Kansas','Kansas'),
('Kentucky','Kentucky'),
('Louisiana','Louisiana'),
('Maine','Maine'),
('Maryland','Maryland'),
('Massachusetts','Massachusetts'),
('Michigan','Michigan'),
('Minnesota','Minnesota'),
('Mississippi','Mississippi'),
('Missouri','Missouri'),
('Montana','Montana'),
('Nebraska','Nebraska'),
('Nevada','Nevada'),
('New Hampshire', 'New Hampshire'),
('New Jersey', 'New Jersey'),
('New Mexico', 'New Mexico'),
('New York', 'New York'),
('North Carolina', 'North Carolina'),
('North Dakota', 'North Dakota'),
('Ohio','Ohio'),
('Oklahoma','Oklahoma'),
('Oregon','Oregon'),
('Pennsylvania','Pennsylvania'),
('Rhode Island', 'Rhode Island'),
('South Carolina', 'South Carolina'),
('South Dakota', 'South Dakota'),
('Tennessee','Tennessee'),
('Texas','Texas'),
('Utah','Utah'),
('Vermont','Vermont'),
('Virginia','Virginia'),
('Washington','Washington'),
('West Virginia','West Virginia'),
('Wyoming','Wyoming'),
('Wisconsin','Wisconsin')])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    
    choice = None
    state = None
    ids = []
    graphJSON = []
    #ruhlman_data = pd.read_excel('test.xlsx')
    form = ChoiceForm()
    if form.validate_on_submit():
        choice = form.choice.data
        state = form.state.data
        if choice != "blank":
            graphJSON = make_bar_chart(choice, state)
            ids = ["Bar Chart for x"]
        form.choice.data = ''
    return render_template('index.html', form=form, choice=choice, state = state,
                           graphJSON=graphJSON,
                           ids=ids)

if __name__ == '__main__':
    app.run(debug=True, port = 7000)
    #app.run(host='0.0.0.0', port = 1561, debug=True)