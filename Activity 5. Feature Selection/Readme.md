ABOUT THIS FILES:

incidentsarabaporaccidente.csv: Archive containing the information of the accidents of the province of ARABA.

SacarLabels.py: Script which runs the DBSCAN algorithm and pulls out which clusters each crash belongs to. Later this information is entered in a csv file.

incidentsarabaporaccidenteC.csv: File containing the csv incidentsarabaporaccidente.csv information and includes the label of the cluster to which it belongs.

ScriptBD.py: Script that inserts the information of the file CSV, in a data base sqlite3 to realize consultations later.

BD.db: Database sqlite3 with the information of the accidents of the province of ARABA.

Caracterisitcas.py: Script that transforms the information of the BD into another series of characteristics according to the label of the cluster to which belongs. The result is the file Caracteristicas.csv.

Caracteristicas.csv: Resulting from the previous Script.

PCA.py: Script that executes the PCA algorithm on file Characteristics.csv. Then show a graph with the results.

Makefile: Script to run the activity.


EXECUTION:

To execute the file you must write on the terminal the command "make all".




