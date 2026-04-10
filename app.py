from flask import Flask, render_template
import requests
import csv
import io

app = Flask(__name__)

# Your specific Sheet ID from the URL you provided
SHEET_ID = "1hsnOOaz88370WvDKbAT_mMA2NhYxcH67IE3lNk8Pg24"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

@app.route('/')
def index():
    cat_list = []
    try:
        # Fetch the sheet as a CSV file
        response = requests.get(CSV_URL)
        response.encoding = 'utf-8'
        
        if response.status_code == 200:
            # Convert the text into a format Python's CSV reader understands
            f = io.StringIO(response.text)
            reader = csv.DictReader(f)
            
            for row in reader:
                # This automatically creates a dictionary using your headers 
                # (cat_breed, cat_desc, cat_pict)
                cat_list.append(row)
        else:
            print(f"Error: Could not reach sheet. Status code {response.status_code}")

    except Exception as e:
        print(f"Connection error: {e}")

    return render_template('index.html', cats=cat_list)

if __name__ == '__main__':
    app.run(debug=True)