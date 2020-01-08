# load data
filename = 'all.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
#print(words[:100])


wordfreq=[words.count(p) for p in words]

all=dict(zip(words,wordfreq))

keys_X=['uop','uom','uoc','usjp','uok']
values_Y=[]

#values_Y[0] = all.get("uop", "")
#values_Y[1] = all.get("uom", "")
#values_Y[2] = all.get("uoc", "")
#values_Y[3] = all.get("usjp", "")
#values_Y[4] = all.get("uok", "")

values_Y.insert(0, all.get("uop", ""))
values_Y.insert(1, all.get("uom", ""))
values_Y.insert(2, all.get("uoc", ""))
values_Y.insert(3, all.get("usjp", ""))
values_Y.insert(4, all.get("uok", ""))

print(keys_X)
print(values_Y)



###################################   WORD FREQUENCY  ###########################################################

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Searchversity'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': keys_X, 'y': values_Y, 'type': 'line', 'name': 'SF'},

            ],
            'layout': {
                'title': 'Popularity distribution of universities in Sri Lanka'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

