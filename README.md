# check_oclc_uniqueness
A short script to determine the unique titles that our library holds per the Worldcat Metadata API

1. Generate a CSV report in the Evergreen reporter that includes the content of the 035$a.
2. Fix the variables in this script.  `oclc_number_header`'s value should be the same as what you called the column in the reporter that contained the 035$a.
3. If there are other columns that you would like in your final report, go to the very last line and add something in the format `, row['call_number']` if the column you would like to add is called call_number in your original report.
4. Run the script using something like `python check_for_unique_oclc.py report-data.csv`
