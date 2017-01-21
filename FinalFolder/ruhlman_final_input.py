# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
import plotly.graph_objs as go
import pandas as pd
import nltk
#from wtforms.validators import Required, Length
import json, plotly
#import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
bootstrap = Bootstrap(app)

with open('hist.json', 'r') as fp:
    histdict = json.load(fp)

with open('mus.json', 'r') as fp:
    musdict = json.load(fp)
    
with open('wom.json', 'r') as fp:
    womdict = json.load(fp)

with open('wom.json', 'r') as fp:
    womdict = json.load(fp)

with open('pol.json', 'r') as fp:
    poldict = json.load(fp)
    
with open('soc.json', 'r') as fp:
    socdict = json.load(fp)
    
with open('cs.json', 'r') as fp:
    csdict = json.load(fp)
    
with open('psych.json', 'r') as fp:
    psychdict = json.load(fp)
    
with open('econ.json', 'r') as fp:
    econdict = json.load(fp)
    
with open('art.json', 'r') as fp:
    artdict = json.load(fp)
    
with open('eng.json', 'r') as fp:
    engdict = json.load(fp)
    
with open('bio.json', 'r') as fp:
    biodict = json.load(fp)

with open('ruhlbio.json', 'r') as fp:
    biodictruhl = json.load(fp)
    
with open('ruhlhist.json', 'r') as fp:
    histdictruhl = json.load(fp)

with open('ruhlmus.json', 'r') as fp:
    musdictruhl = json.load(fp)
    
with open('ruhlwom.json', 'r') as fp:
    womdictruhl = json.load(fp)

with open('ruhlpol.json', 'r') as fp:
    poldictruhl = json.load(fp)
    
with open('ruhlsoc.json', 'r') as fp:
    socdictruhl = json.load(fp)
    
with open('ruhlcs.json', 'r') as fp:
    csdictruhl = json.load(fp)
    
with open('ruhlpsych.json', 'r') as fp:
    psychdictruhl = json.load(fp)
    
with open('ruhlecon.json', 'r') as fp:
    econdictruhl = json.load(fp)
    
with open('ruhlart.json', 'r') as fp:
    artdictruhl = json.load(fp)
    
with open('ruhleng.json', 'r') as fp:
    engdictruhl = json.load(fp)
    
with open('ruhlbio.json', 'r') as fp:
    biodictruhl = json.load(fp)
    
def construct_query_plotly(worddraw):
    english_stemmer = nltk.stem.SnowballStemmer('english')
    word = english_stemmer.stem(worddraw)
    if word in biodict.keys():
        bioresp = float(biodict[word]) / float(biodict['total_words']) * 100
    else:
        bioresp = 0
    if word in biodictruhl.keys():
        bioruhl = float(biodictruhl[word]) / float(biodictruhl['total_words']) * 100
    else:
        bioruhl = 0
        
    if word in engdict.keys():
        engresp = float(engdict[word]) / float(engdict['total_words']) * 100
    else:
        engresp = 0
    if word in engdictruhl.keys():
        engruhl = float(engdictruhl[word]) / float(engdictruhl['total_words']) * 100
    else:
        engruhl = 0
    
    if word in psychdict.keys():
        psychresp = float(psychdict[word]) / float(psychdict['total_words']) * 100
    else:
        psychresp = 0
    if word in psychdictruhl.keys():
        psychruhl = float(psychdictruhl[word]) / float(psychdictruhl['total_words']) * 100
    else:
        psychruhl = 0
        
    if word in artdict.keys():
        artresp = float(artdict[word]) / float(artdict['total_words']) * 100
    else:
        artresp = 0
    if word in artdictruhl.keys():
        artruhl = float(artdictruhl[word]) / float(artdictruhl['total_words']) * 100
    else:
        artruhl = 0
    
    if word in econdict.keys():
        econresp = float(econdict[word]) / float(econdict['total_words']) * 100
    else:
        econresp = 0
    if word in econdictruhl.keys():
        econruhl = float(econdictruhl[word]) / float(econdictruhl['total_words']) * 100
    else:
        econruhl = 0
        
    if word in socdict.keys():
        socresp = float(socdict[word]) / float(socdict['total_words']) * 100
    else:
        socresp = 0
    if word in socdictruhl.keys():
        socruhl = float(socdictruhl[word]) / float(socdictruhl['total_words']) * 100
    else:
        socruhl = 0
        
    if word in csdict.keys():
        csresp = float(csdict[word]) / float(csdict['total_words']) * 100
    else:
        csresp = 0
    if word in csdictruhl.keys():
        csruhl = float(csdictruhl[word]) / float(csdictruhl['total_words']) * 100
    else:
        csruhl = 0
        
    if word in womdict.keys():
        womresp = float(womdict[word]) / float(womdict['total_words']) * 100
    else:
        womresp = 0
    if word in womdictruhl.keys():
        womruhl = float(womdictruhl[word]) / float(womdictruhl['total_words']) * 100
    else:
        womruhl = 0
    
    if word in poldict.keys():
        polresp = float(poldict[word]) / float(poldict['total_words']) * 100
    else:
        polresp = 0
    if word in poldictruhl.keys():
        polruhl = float(poldictruhl[word]) / float(poldictruhl['total_words']) * 100
    else:
        polruhl = 0
        
    if word in musdict.keys():
        musresp = float(musdict[word]) / float(musdict['total_words']) * 100
    else:
        musresp = 0
    if word in musdictruhl.keys():
        musruhl = float(musdictruhl[word]) / float(musdictruhl['total_words']) * 100
    else:
        musruhl = 0
        
    if word in histdict.keys():
        histresp = float(histdict[word]) / float(histdict['total_words']) * 100
    else:
        histresp = 0
    if word in histdictruhl.keys():
        histruhl = float(histdictruhl[word]) / float(histdictruhl['total_words']) * 100
    else:
        histruhl = 0
        
    animal = pd.DataFrame({'Department': ['Biology','English', 'Psychology', 
                                       'Economics',  'Art', 'Sociology', 
                                       'Computer Science', 'Women and Gender Studies', 
                                       'Political Science', 
                                       'Music', 'History'], 
                        'Responses' : [bioresp,  engresp,  psychresp,  econresp, artresp,
                                    socresp,  csresp,  womresp,  polresp, musresp, 
                                    histresp],
                        'Ruhlman' : [ bioruhl, engruhl,  psychruhl, econruhl, 
                                   artruhl,  socruhl, csruhl,  womruhl,  polruhl, 
                                   musruhl, histruhl]}
                       )
    return animal


# One can create more than one plot and store them in a list, which will be
# turned into JSON to be passed to the client.
def make_bar_chart(inputText): 
    animal = construct_query_plotly(inputText)
    animal.sort_values(['Responses','Ruhlman'], ascending = True, inplace = True)
    graphs = [
            dict(
                data = [
                        dict(
                            x=animal['Responses'],
                            y=animal['Department'],
                            mode='markers',
                            name='Responses',
                            marker=dict(
                            color='rgba(156, 165, 196, 0.95)',
                            line=dict(
                            color='rgba(156, 165, 196, 1.0)',
                            width=1,
                            ),
                            symbol='circle',
                            size=16,
                            )
                           ,),
                           dict(
                            x=animal['Ruhlman'],
                                                y=animal['Department'],
                                                mode='markers',
                                                name='Ruhlman',
                                                marker=dict(
                                                    color='rgba(204, 204, 204, 0.95)',
                                                    line=dict(
                                                        color='rgba(217, 217, 217, 1.0)',
                                                        width=1,
                                                    ),
                                                    symbol='circle',
                                                    size=16,
                                                    )
                                                ),
                        
                        ],
                layout =
                    go.Layout(
                        title="Word Frequency based on Responses and Ruhlman Abstracts",
                        xaxis=dict(
                            showgrid=False,
                            showline=True,
                            linecolor='rgb(102, 102, 102)',
                            titlefont=dict(
                                color='rgb(204, 204, 204)'
                            ),
                            tickfont=dict(
                                color='rgb(102, 102, 102)',
                            ),
                            autotick=False,
                            dtick=10,
                            ticks='outside',
                            tickcolor='rgb(102, 102, 102)',
                        ),
                        margin=dict(
                            l=200,
                            r=40,
                            b=50,
                            t=80
                        ),
                        legend=dict(
                            font=dict(
                                size=10,
                            ),
                            yanchor='middle',
                            xanchor='right',
                        ),
                        width=800,
                        height=600,
                        paper_bgcolor='rgb(238,232,170)',
                        plot_bgcolor='rgb(255,255,240)',
                        hovermode='closest',
                        )
                )
        ]
              # Convert the figures to JSON
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON)
    return graphJSON


@app.route('/', methods=['GET', 'POST'])
def index():
    #inputText = request.form['inputText']
    ids = []
    graphJSON = []
    graphJSON = make_bar_chart('test')
    ids = ["Department Work vs. Perceptions"]
    if request.method == 'POST':
            inputText = request.form['inputText']
            graphJSON = make_bar_chart(inputText)
    return render_template('index.html',
                           graphJSON=graphJSON,
                           ids=ids) #data = ruhlman_data.to_html())
                           
@app.route('/inputText', methods=['GET', 'POST'])
def indexInput():
    #inputText = request.form['inputText']
    ids = []
    graphJSON = []
    graphJSON = make_bar_chart('test')
    ids = ["Department Work vs. Perceptions"]
    if request.method == 'POST':
            inputText = request.form['inputText']
            graphJSON = make_bar_chart(inputText)
    return render_template('index.html',
                           graphJSON=graphJSON,
                           ids=ids) #data = ruhlman_data.to_html())


if __name__ == '__main__':
    app.run(debug=True, port = 7000)
    #app.run(host='0.0.0.0', port = 1561, debug=True)