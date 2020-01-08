# load data
filename = 'colombotext.txt'
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

###################################################################
#import csv

#w = csv.writer(open("ColomboWordFreq.csv", "w"))
#for key, val in all.items():
 # w.writerow([key, val])

##################################################################

del all["https"]
del all["http"]
del all["sri"]
del all["lanka"]
del all["vs"]
del all["gçª"]
del all["gçô"]

#print(all)
# finding 20 highest values in a Dictionary

from collections import Counter

keys_X=[]
values_Y=[]


k = Counter(all)

# Finding 3 highest values
high = k.most_common(50)

for i in high:
     keys_X.append(i[0])
     values_Y.append(i[1])


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
                'title': 'University of Colombo - words with highest fequency'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

