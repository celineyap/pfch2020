import csv

with open ('NYPD_Complaint_Data_Historic.csv', 'r') as datafile:

	processed_csv = csv.reader (datafile)

	line_counter=0

	with open ('crime_data_census.csv','w') as csvout:

		writeable_csv = csv.writer(csvout)

		for row in processed_csv:

			print (line_counter)

			if line_counter==0:

				writeable_csv.writerow(row)

			if row [8] == 'ROBBERY' or row [8] == 'BURGLARY' or row [8] == 'HARRASSMENT 2' or row [8] == 'ASSAULT 3 & RELATED OFFENSES' or row [8] == 'PETIT LARCENY' or row [8] == 'CRIMINAL MISCHIEF & RELATED OF' or row [8] == 'DANGEROUS DRUGS' or row [8] == 'OFF. AGNST PUB ORD SENSBLTY &' or row [8] == 'FELONY ASSAULT' or row [8] == 'GRAND LARCENY' :

				writeable_csv.writerow(row)

			line_counter +=1