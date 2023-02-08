# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/07/2023
# Description: Write a class named SatData that reads a JSON file containing
# data on 2010 SAT results for New York City and writes the data to a text file in
# CSV format.
import json


class SatData:
    """Represents data on 2010 SAT result in NYC."""

    def __init__(self):
        with open('sat.json', 'r') as infile:
            self._data = json.load(infile)['data']

    def save_as_csv(self, dbns):
        """Saves and reformats SAT data to a csv."""
        sat_list = []
        for data in self._data:
            if data[8] in dbns:
                sat_list.append(data)

        with open('output.csv', 'w') as outfile:
            label: [str(index) for index in range(len(sat_list[3]))]
            for row in sat_list:
                sat_data = []
                for item in row:
                    if ',' in str(item):
                        sat_data.append("\"" + item + "\"")
                    else:
                        sat_data.append(str(item))
                outfile.write(','.join(sat_data))
                outfile.write('\n')
        outfile.close()


# sd = SatData()
# dbns = ["02M303", "02M294", "01M450", "02M418"]
# sd.save_as_csv(dbns)
