# utils.py
import csv
def read_CSV_file():
    '''
    Read a particular CSV file into a list.
    monroe-county-crash-data2003-to-2015.csv
    The first row is assumed to be a header and is skipped
    @return the list
    '''
    csv_data = []
    with open("monroe-county-crash-data2003-to-2015.csv", newline='') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
    #   csv_data.append(header)        # We don't want the header row.
        for row in reader:
            csv_data.append(row)
    
    #print(csv_data)
    print (type(csv_data))      # It's a list of lists!
    return csv_data
    
