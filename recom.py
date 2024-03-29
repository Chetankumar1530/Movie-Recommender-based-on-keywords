import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import ast
import warnings
warnings.filterwarnings("ignore")
vec = TfidfVectorizer()
data = pd.read_csv("Nlp with images.csv")
data.fillna("sorry",inplace=True)
vector = vec.fit_transform(data["ggg"])
indexed = pd.Series(data = data.index,index=data.lower)

def search(n, top = 10,rate = 3):
    if n.lower() in indexed:
        rec = pd.DataFrame(list(linear_kernel(vector[indexed[n.lower()]],vector)))
        rec = rec.transpose()
        rec.columns = ["name"]
        rec = rec.sort_values(by="name" ,ascending=False)
        x = pd.DataFrame()
        for i in range(0,min(top,800)):
            x = x.append(data.loc[rec.index[i]:rec.index[i]])
        x = x[(x["Ratinng"] > rate) & (x["img"] != "sorry") ]
        x = x.sort_values(by="Ratinng",ascending=False)
        
#         display(x)
    else:
        return ("Not Found")
    return list(x["Movie Title"]), list(x.ggg), list(x.Ratinng),list(x["Release Date"]),list(x["Positive reviews"]),list(x["Negative reviews"]),list(x["Nuteral  reviews"]),list(x["img"])


def search_by_keyword(n, top = 10,rate = 3):
    data.Plot.loc[810] = n
    vector = vec.fit_transform(data["Plot"])
    indexed = pd.Series(data = data.index,index=data.title)

    rec = pd.DataFrame(list(linear_kernel(vector[indexed[810]],vector)))
    rec = rec.transpose()
    rec.columns = ["name"]
    rec = rec.sort_values(by="name" ,ascending=False)
    x = pd.DataFrame()
    for i in range(1,min(top,800)):
        x = x.append(data.loc[rec.index[i]:rec.index[i]])
    x = x[x["Ratinng"] > rate]
    return list(x["Movie Title"]), list(x.ggg), list(x.Ratinng),list(x["Plot"]),list(x["Positive reviews"]),list(x["Negative reviews"]),list(x["Nuteral  reviews"]),list(x["img"])

def listt():
    data = pd.read_csv("Nlp with images.csv")
    data = data[ data["img"] != "sorry" ]
    data = data.sort_values(by="Ratinng",ascending=False)
    return list(data["Movie Title"]), list(data.ggg), list(data.Ratinng),list(data["Release Date"]),list(data["Positive reviews"]),list(data["Negative reviews"]),list(data["Nuteral  reviews"]),list(data["img"])
