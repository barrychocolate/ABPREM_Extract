# Project Aim
The aim of this project is to be able to extract all the Delivery Point Addressess that have been created or updated recently.  These are extracted into a csv file.

# Step 1
Download AddressBase Premium or Addressbase Premium Islands from the OS Data Hub.

# Step 2
Run AddressBasePremium_RecordSplitter_v3_7.py.  This will extract all of the data into a single file for each of the related tables.

**Note**: This script is a direct copy from Ordnance Survey's repo which can be found here https://github.com/OrdnanceSurvey/AddressBase)

# Step 3
Run latest_dpa.py.  This reads the 'ID28_DPA_Records.csv' file produced by step 2 and copies any records that meet the criteria below to a new file called 'DPA_latest.csv'.

Selection criteria: 
process_date >= '01/01/2021' OR
start_date >= '01/01/2021' OR
update_date >= '01/01/2021' OR
entry_date >= '01/01/2021'

Details on the AddressBasde Premium scehma can be found here https://www.ordnancesurvey.co.uk/documents/product-support/tech-spec/addressbase-premium-technical-specification.pdf
