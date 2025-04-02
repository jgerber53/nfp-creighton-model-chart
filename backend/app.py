from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)
DATA_DIR = "data_files"

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

@app.route("/..")
def index():
    files = os.listdir(DATA_DIR)  # List available files
    return render_template("index.html", files=files)

@app.route("/create", methods=["POST"])
def create_file():
    filename = request.form["filename"] + ".csv"
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w") as f:
        f.write("Date, Value\n")  # Initialize a blank CSV
    return "File created!", 200

@app.route("/generate_chart", methods=["POST"])
def generate_chart():
    selected_file = request.form["selected_file"]
    # Run plotChart.py using subprocess
    os.system(f"python plotChart.py {os.path.join(DATA_DIR, selected_file)}")
    return "Chart generated!", 200

@app.route("/combine_charts", methods=["POST"])
def combine_charts():
    selected_files = request.form.getlist("selected_files")  # List of files
    file_paths = " ".join([os.path.join(DATA_DIR, f) for f in selected_files])
    os.system(f"python combineCharts.py {file_paths}")
    return "Combined charts!", 200

if __name__ == "__main__":
    app.run(debug=True)