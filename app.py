import os
from flask import Flask, render_template, send_from_directory, request, redirect, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'google' # Folder where survey analysis files are stored

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reports')
def list_reports():
    files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f))]
    return render_template('reports.html', files=files, upload_folder=app.config['UPLOAD_FOLDER'])

@app.route('/reports/<filename>')
def serve_report(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/new_survey')
def new_survey_form():
    return render_template('new_survey.html')

@app.route('/submit_survey', methods=['POST'])
def submit_survey_form():
    # In a real application, you would process the form data here
    # For example, save it to a database or a file
    # For now, we'll just redirect to a simple confirmation or back to home.
    # You can access form data using request.form.get('field_name')
    # e.g., title = request.form.get('survey_title')
    # print(f"Received survey title: {title}") # Example
    return redirect(url_for('index')) # Redirect to home page after submission for now

if __name__ == '__main__':
    app.run(debug=True)
