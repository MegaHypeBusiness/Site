from flask import Flask, render_template, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Configurações do Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('megahype-ecddc1d8b75a.json', scope)
client = gspread.authorize(creds)

# Abra a planilha pelo nome
sheet = client.open("Novos Clientes").sheet1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data['name']
    tipo_servico = data['tipo_servico']
    phone = data['phone']

    # Adicione os dados na planilha
    sheet.append_row([name, tipo_servico, phone])

    return jsonify({'message': 'Dados enviados com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
