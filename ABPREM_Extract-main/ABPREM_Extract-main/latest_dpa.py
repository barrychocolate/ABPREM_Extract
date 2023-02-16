# Imported modules
import csv
import os
from datetime import datetime

# This code extracts the latest DPA records
directorypath = os.getcwd()
headings28 = ["RECORD_IDENTIFIER","CHANGE_TYPE","PRO_ORDER","UPRN","UDPRN","ORGANISATION_NAME","DEPARTMENT_NAME","SUB_BUILDING_NAME","BUILDING_NAME","BUILDING_NUMBER","DEPENDENT_THOROUGHFARE","THOROUGHFARE","DOUBLE_DEPENDENT_LOCALITY","DEPENDENT_LOCALITY","POST_TOWN","POSTCODE","POSTCODE_TYPE","DELIVERY_POINT_SUFFIX","WELSH_DEPENDENT_THOROUGHFARE","WELSH_THOROUGHFARE","WELSH_DOUBLE_DEPENDENT_LOCALITY","WELSH_DEPENDENT_LOCALITY","WELSH_POST_TOWN","PO_BOX_NUMBER","PROCESS_DATE","START_DATE","END_DATE","LAST_UPDATE_DATE","ENTRY_DATE"]

readfile = 'ID28_DPA_Records.csv'
writefile = 'DPA_latest.csv'
rowcount = 1
writecount = 0
# Update this to change how recent a record has to be to be included
earliest_date = datetime(2021, 1, 1).date()

if os.path.isfile(writefile):
    os.remove(writefile)

dp_28 = open(writefile, 'a', encoding='utf-8')
write28 = csv.writer(dp_28, delimiter=',', quotechar='"', lineterminator='\n')
# write28.writerow(headings28)

csvfileList = ['ID28_DPA_Records.csv']

for filepath in csvfileList:
    with open(filepath, encoding='utf-8') as f:
        csvreader = csv.reader(f, delimiter=',', doublequote=False, lineterminator='\n', quotechar='"', quoting=0, skipinitialspace=True)
        try:
            for row in csvreader:
                if rowcount == 1:
                    write28.writerow(row)
                    writecount += 1
                else:
                    process_date = datetime.strptime(row[24], '%Y-%m-%d').date()
                    start_date = datetime.strptime(row[25], '%Y-%m-%d').date()
                    update_date = datetime.strptime(row[27], '%Y-%m-%d').date()
                    entry_date = datetime.strptime(row[28], '%Y-%m-%d').date()
                    if (process_date >= earliest_date) or (start_date >= earliest_date) or (update_date >= earliest_date) or (entry_date >= earliest_date):
                        write28.writerow(row)
                        writecount += 1

                rowcount += 1

                # if rowcount > 5:
                #     break
                if rowcount % 100000 == 0:
                    print(f'row {rowcount:,} processed')

        except KeyError as e:
            print(f'error at row {rowcount}')
            pass

dp_28.close()
print(f'{rowcount:,} rows read and {writecount:,} rows written')
