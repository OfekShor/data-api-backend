from flask import Flask, request, jsonify
import sqlite3
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_PATH = "stock.db"


@app.route("/run_query", methods=["POST"])
def run_query():
    query = request.json.get("query")
    try:
        with sqlite3.connect(DB_PATH) as conn:
            df = pd.read_sql_query(query, conn)
        return jsonify({"columns": df.columns.tolist(), "rows": df.values.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

