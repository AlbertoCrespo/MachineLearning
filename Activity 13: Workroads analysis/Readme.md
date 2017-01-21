ABOUT THIS FILES:

The process performed in this activity is as follows:

1) First runs the script ScriptFilterProvincieandWorks2007.py that is in charge of extracting the types of accidents caused by works in 2007. This information is stored in the file incidentsWorks2007.

2) In the second place, the KNN.py script that uses the KNN algorithm, using the accidents of type 2006 as a training set, is assigned a zone to the set of incidents of type works of 2007 calculated in point 1, obtaining As a result the file incidentsWorks2007C.csv.

3) Thirdly, we launched ScriptBD.py, which is to enter the information of the previous point in a database of type sqlite3.

4) At this point, the script Caracteristicas.py is launched that allows to make a series of queries to the database of the previous point, and thus to obtain a file csv, that contains the information of the number of works that are by zone, this one Resolver file is named Works2007Features.csv.

5) At this point the script kmenas.py that executes a kmeans algorithm with 3 cluster to the previous information, perimitiendo thus to assign three type of label to the previous information. As a result we get the file Works2007FeaturesC.csv.

6) At this point, the Juntartodo.py script is executed, which joins the csv file, the characteristics of the 2006 incidents, obtained in activity 5, with the kmeans zone obtained in the previous point. The resulting file is a csv file called DeccisionTree.csv.

7) Finally, a decision tree algorithm is applied to the file obtained from the previous point using the DecisionTree.py script, with a maximum depth of 3 and an entropy selection criterion. The results that the generated pdf offers us is that the accidents that were later turned into works are Accidents by level Black and by reach.


EXECUTION:

To execute the file you must write on the terminal the command "make all".




