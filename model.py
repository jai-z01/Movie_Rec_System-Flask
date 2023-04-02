import pandas as pd
import numpy as np
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
warnings.filterwarnings("ignore")
df1 = pd.read_csv(r"C:\Users\jai_soorya\OneDrive\Desktop\pypro\Datasets\tmdb_5000_credits.csv")
df = pd.read_csv(r"C:\Users\jai_soorya\OneDrive\Desktop\pypro\Datasets\tmdb_5000_movies.csv")
df = df.merge(df1,on='title')
data = df[['genres','keywords','spoken_languages','overview','tagline','cast','title']]
def func(x):
    x = eval(x)
    s = ''
    for i in x:
        s += i['name'].replace(" ","")+" "
    return s
data['text'] = ''
for i in ['genres','keywords','spoken_languages','cast']:
    data['text'] += data[i].transform(func)
data.fillna('',inplace = True)
data['text'] += data['overview']+data['tagline']
tfidf = TfidfVectorizer(max_features = 2500)
x = tfidf.fit_transform(data['text'])
def recommendor(movie):
    req = x[data[data['title']==movie].index]
    if(req.shape[0] != 0):
        score = cosine_similarity(req,x).flatten()
        ind = (-score).argsort()[1:6]
        recc_movs = []
        for i in np.array(data[['title']].iloc[ind]):
            recc_movs.append(i[0])
        return recc_movs
    else:
        return False
#import pickle
#pickle.dump(recommendor,open('model.pkl','wb'))