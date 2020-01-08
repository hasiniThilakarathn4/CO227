from unidecode import unidecode
from textblob import TextBlob
import matplotlib.pyplot as plt

file=open("japuratext.txt");
t=file.read();
bobo = TextBlob(unidecode(t))
print(format(bobo.sentiment.polarity))

pos = 0
neg = 0

if bobo.sentiment.polarity>0:
    print("positive")
    pos = bobo.sentiment.polarity +1
    neg = 2-pos
elif bobo.sentiment.polarity<0:
    print("negative")
    neg = (bobo.sentiment.polarity * -1) + 1
    pos = 2 - neg
else:
    print("neutral")

labels = 'Positive', 'Negative'
sizes = [pos, neg]
colors = ['yellowgreen', 'lightskyblue']
explode = (0, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
