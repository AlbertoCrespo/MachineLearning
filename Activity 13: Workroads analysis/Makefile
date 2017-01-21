all : borrar ejecutar

borrar:
	rm '../1-Data/incidentsWorks2007.csv'
	rm '../1-Data/incidentsWorks2007C.csv'
	rm '../1-Data/BD1.db'
	rm '../1-Data/Works2007Features.csv'
	rm '../1-Data/Works2007FeaturesC.csv'
	rm '../1-Data/DecisionTree.csv'

ejecutar: 
	python ScriptFilterProvincieandWorks2007.py
	python KNN.py
	python ScriptBD.py
	python Caracteristicas.py
	python kmeans.py
	python Juntartodo.py
	python DecisionTree.py