import pandas as pd
import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
CORS(app)

def fetch_from_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anannya",
        database="crime_report_db"
    )
    query = """
    SELECT title AS `Crime Type`, created_at AS `Date of Occurrence`, latitude, longitude
    FROM crime_reports
"""

    df = pd.read_sql(query, conn)
    conn.close()
    return df

@app.route('/predict', methods=['POST'])
def predict_trend():
    try:
        print("✅ /predict hit")
        data = request.get_json()
        print("📦 Incoming data:", data)

        location = data.get('location')
        crime_type = data.get('crimeType')

        if not location or not crime_type:
            return jsonify({'error': 'Missing input values'}), 400


        # Dataset
        df_csv = pd.read_csv("C:/Users/HP/OneDrive/Desktop/crime report analysis/data/crime_dataset_india (1).csv")
        df_csv['Date of Occurrence'] = pd.to_datetime(df_csv['Date of Occurrence'], errors='coerce')
        df_csv.dropna(subset=['Date of Occurrence'], inplace=True)

        # Database
        df_db = fetch_from_database()
        df_db['Date of Occurrence'] = pd.to_datetime(df_db['Date of Occurrence'], errors='coerce')
        df_db.dropna(subset=['Date of Occurrence'], inplace=True)

        # Combine
        combined = pd.concat([df_csv, df_db])
        combined['Year'] = combined['Date of Occurrence'].dt.year

        # Filter
        filtered = combined[
            (combined['location'].str.lower() == location.lower()) &
            (combined['Crime Type'].str.lower() == crime_type.lower())
        ]

        if filtered.empty:
            return jsonify({'error': 'No matching records found.'}), 404

        yearly = filtered.groupby('Year').size().reset_index(name='Crime Count')
        X = yearly[['Year']]
        y = yearly['Crime Count']

        model = LinearRegression()
        model.fit(X, y)

        future_years = np.array([X['Year'].max() + i for i in range(1, 4)]).reshape(-1, 1)
        future_preds = model.predict(future_years)
        future_preds = np.round(future_preds).astype(int)

        # Plot
        plt.figure(figsize=(8, 5))
        plt.plot(X, y, marker='o', label='Actual')
        plt.plot(future_years, future_preds, marker='x', linestyle='--', color='red', label='Prediction')
        plt.title(f"{crime_type} Trends in {location}")
        plt.xlabel("Year")
        plt.ylabel("Crime Count")
        plt.legend()
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')

        return jsonify({
            'trend_chart': img_base64,
            'predictions': [
                {'year': int(y), 'predicted_crimes': int(p)}
                for y, p in zip(future_years.flatten(), future_preds)
            ]
        })

    except Exception as e:
        import traceback
        print("❌ Error in /predict:", str(e))
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

