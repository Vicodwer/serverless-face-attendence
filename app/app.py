# app.py

from flask import Flask, render_template_string
import pandas as pd
import os

app = Flask(__name__)
ATTENDANCE_FILE = "attendance.csv"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Attendance Dashboard</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        table { border-collapse: collapse; width: 80%; }
        th, td { border: 1px solid black; padding: 8px; text-align: center; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h2>Face Recognition Attendance Dashboard</h2>
    {{ table|safe }}
</body>
</html>
"""

@app.route("/")
def dashboard():
    if os.path.exists(ATTENDANCE_FILE):
        df = pd.read_csv(ATTENDANCE_FILE)
        table = df.to_html(index=False)
    else:
        table = "<p>No attendance records found.</p>"

    return render_template_string(HTML_TEMPLATE, table=table)


if __name__ == "__main__":
    app.run(debug=True)
