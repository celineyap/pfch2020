import csv

crime_count = {}

with open ('NYPD_Complaint_Data_Historic.csv', 'r') as crimedata:

	dictprocessed_csv = csv.DictReader(crimedata)

	for row in dictprocessed_csv:

		if row['OFNS_DESC'] not in crime_count:

			crime_count[row['OFNS_DESC']]=0
		crime_count[row['OFNS_DESC']] = crime_count[row['OFNS_DESC']] +1

sort_ofns = sorted(crime_count.items(), key=lambda x: x[1], reverse=True)
for ofns in sort_ofns:
	print(ofns[0], ofns[1])