# -*- coding: utf-8 -*-

# function for plotting
from matplotlib.colors import ListedColormap
import pandas as pd, numpy as np, matplotlib.pyplot as plt
import csv


#Reading the initial data
df = pd.read_csv('../1-Data/FeaturesClass.csv')

y = targets = labels = df["Class"].values

columns = ['Numero de accidentes por salida',' numero de accidentes por Alcance',' Numero de accidentes por Vuelco',' Numero de accidentes por tijera',' numero de accidentes por atropello',' Numero de accidentes por nivel Amarillo',' Numero de Accidentes por Nivel Blanco',' Numero de accidentes por nivel Negro',' Numero de accidentes por nivel Rojo']
clases = ['High Zone','Low Zone','Mild Zone']
features = df[list(columns)].values



from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
X = imp.fit_transform(features)

from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(X, y)


# 3. Plot the decision tree: 
# http://nbviewer.jupyter.org/github/kittipatkampa/python_dev/blob/master/demo_decision_tree_v1.ipynb
from sklearn.externals.six import StringIO  
import pydot 

# It is necessary to install GraphViz
# http://www.graphviz.org/Download..php
# PATH = C:\Program Files (x86)\Graphviz2.38\bin\:$PATH$


# Extract the decision tree logic from the trained model
dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data
						,feature_names=columns,
						 class_names=clases,    
                         filled=True, rounded=True,  
                         special_characters=True)


# convert the logics into graph
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 

## This will plot decision tree in pdf file
graph.write_pdf(path="Tree.pdf")