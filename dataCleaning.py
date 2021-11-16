import pandas as pd
import numpy as np
import csv

def clean_data():
    og_df = pd.read_json('house_3.json')
    og_df.to_csv('clean_data.csv', index = None)
    og_df = pd.read_csv('clean_data.csv')
    csvFile = []
    f = open('clean_data.csv', 'w', encoding = 'UTF-8', newline='')
    writer = csv.writer(f)
    with open('og_data.csv', mode ='r', encoding = 'UTF-8')as file:     
        csvFile = csv.reader(file) 
        count = 0
        for lines in csvFile:
            split = lines[0].split(",")
            # id, city, views, price_usd, space, room, latitude, longitude, poster_type
            lines[0] = split[len(split) - 1]
            lines = [count] + lines[0:1] + [lines[3]] + lines[7:10] + lines[14:16]
            lines[4] = lines[4][6:-3]
            lines[5] = lines[5][0]
            lines = [lines[0]] + lines[2:]
            if count == 0:
                lines[0] = "ID"
                lines[1] = "Views"
                lines[2] = "Price (USD)"
                lines[3] = "Space (m^2)"
                lines[4] = "Number of Rooms"
                lines[5] = "Normalized Latitude"
                lines[6] = "Normalized Longitude"
            else:
                if lines[0] == "" or lines[1] == "" or lines[2] == "" or lines[3] == "" or lines[4] == "" or lines[5] == "" or lines[6] == "":
                    continue
                lines[1] = int(lines[1])
                lines[2] = int(lines[2].replace(',', ''))
                lines[3] = float(lines[3])
                lines[4] = int(lines[4])
                lines[5] = (float(lines[5]) - 41) * 100
                lines[6] = (float(lines[6]) - 44) * 100

            writer.writerow(lines)
            count += 1

if __name__ == '__main__':
    clean_data()