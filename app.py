from flask import Flask, render_template
import pandas as pd
import csv

app = Flask(__name__)

csv_path = 'SteamReviews\\test_data.csv'

@app.route('/')
def index():
    data = pd.read_csv(csv_path).to_dict(orient='records')
    columns = data[0].keys()
    return render_template('table.html', data=data, columns=columns)


def trim_csv(input_path, output_path, row_limit):
    with open(input_path, 'r', newline='', encoding='utf-8') as infile, \
         open(output_path, 'w', newline='', encoding='utf-8') as outfile:
         
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for i, row in enumerate(reader):
            if i < row_limit:
                writer.writerow(row)

if __name__ == '__main__':
    app.run(debug=True)

    # input_csv_path = 'SteamReviews\\reviews-1230-2345.csv'
    # output_csv_path = 'SteamReviews\\reviews-115-1230.csv'
    # trim_csv(input_csv_path, output_csv_path, 10000)
    # print("running")