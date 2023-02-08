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
        with open('sat.json') as infile:
            self._data = json.load(infile)
            self._header = [header['name'] for header in self._data['meta']['view']['columns']][8:]
            self._data = self._data['data']

    def save_as_csv(self, dbns):
        """Saves and reformats SAT data to a csv."""
        sat_list = []
        for row in self._data:
            if row[8] in dbns:
                sat_list.append(row[8:])
        with open('output.csv', 'w') as outfile:
            outfile.write(','.join(header for header in self._header) + '\n')
            for row in sat_list:
                outfile.write(','.join(str(index) for index in row) + '\n')
        outfile.close()


# sd = SatData()
# dbns = ["02M303", "02M294", "01M450", "02M418"]
# sd.save_as_csv(dbns)
