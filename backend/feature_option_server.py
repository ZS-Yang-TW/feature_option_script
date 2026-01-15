import os
import csv
import requests
from datetime import datetime
from flask import Flask, jsonify, send_from_directory, request
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

API_URL = os.getenv('API_URL', "https://cool.testing.dlc.ntu.edu.tw/api/v1/accounts/{account_id}/features?hide_inherited_enabled=true&per_page=50&page={page}")
ACCOUNT_ID = os.getenv('ACCOUNT_ID', '')
CSV_DIR = os.path.join(os.path.dirname(__file__), 'csv')

app = Flask(__name__)

# Helper to fetch all feature options

def fetch_all_feature_options():
    all_features = []
    page = 1
    HEADERS = {
        'Cookie': os.getenv('API_COOKIE', ''),
        'User-Agent': os.getenv('API_USER_AGENT', ''),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
    }
    url = API_URL.replace('{account_id}', ACCOUNT_ID)
    while True:
        resp = requests.get(url.format(page=page), headers=HEADERS)
        print(f"[DEBUG] Fetching page {page}, status: {resp.status_code}")
        if resp.status_code != 200:
            print(f"[DEBUG] Response: {resp.text}")
            break
        data = resp.json()
        print(f"[DEBUG] Page {page} got {len(data)} items")
        if not data:
            break
        all_features.extend(data)
        page += 1
    print(f"[DEBUG] Total features fetched: {len(all_features)}")
    return all_features

# Helper to transform feature options

def transform_features(features):
    def checkmark(val):
        return '✅' if str(val).lower() == 'true' else ''
    rows = []
    for f in features:
        fo = f.get('feature_flag', {})
        rows.append({
            'Account ID': ACCOUNT_ID,
            'Feature Name': f.get('display_name', ''),
            'Feature Description': f.get('description', ''),
            'Hidden': checkmark(fo.get('hidden', False)),
            'Shadow': checkmark(f.get('shadow', False)),
            'Feature Preview': checkmark(f.get('beta', False)),
            'Enable': checkmark(fo.get('state', '') == 'on'),
            'Lock': checkmark(fo.get('locked', False)),
        })
    print(f"[DEBUG] Total features after transform: {len(rows)}")
    return rows

# Endpoint to fetch and save feature options
@app.route('/fetch_features', methods=['POST'])
def fetch_features():
    features = fetch_all_feature_options()
    rows = transform_features(features)
    if not rows:
        return jsonify({'error': 'No feature options found.'}), 204
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{timestamp}_feature_option_list.csv"
    filepath = os.path.join(CSV_DIR, filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        f.write(f"# Account ID: {ACCOUNT_ID}\n")
        writer = csv.DictWriter(f, fieldnames=[k for k in rows[0].keys() if k != 'Account ID'])
        writer.writeheader()
        for row in rows:
            row = dict(row)
            row.pop('Account ID', None)
            writer.writerow(row)
    return jsonify({'filename': filename})

# Endpoint to list CSV files
@app.route('/list_csvs')
def list_csvs():
    files = [f for f in os.listdir(CSV_DIR) if f.endswith('.csv')]
    files.sort(reverse=True)
    return jsonify(files)

# Endpoint to serve a CSV file
@app.route('/csv/<filename>')
def get_csv(filename):
    return send_from_directory(CSV_DIR, filename)

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('../frontend', path)

if __name__ == '__main__':
    os.makedirs(CSV_DIR, exist_ok=True)
    app.run(host='0.0.0.0', port=8000, debug=True)
