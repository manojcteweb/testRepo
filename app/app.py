```python
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

CRM_API_URL = 'https://api.crm-system.com/customers'
PROJECT_CUSTOMERS = {}

def fetch_customers_from_crm():
    try:
        response = requests.get(CRM_API_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {'error': str(e)}

def update_local_customers():
    customers = fetch_customers_from_crm()
    if 'error' not in customers:
        PROJECT_CUSTOMERS.update({c['id']: c for c in customers})

@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(list(PROJECT_CUSTOMERS.values()))

@app.route('/sync', methods=['POST'])
def sync_customers():
    update_local_customers()
    return jsonify({'status': 'success'})

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    update_local_customers()
    app.run(debug=True)
```