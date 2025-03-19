from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Submit the form
@app.route('/submit', methods=['POST'])
def submit():
    
    # Get the name and time from the form
    name = request.form['name']
    time = request.form['time']
    
    # Write the name and time to a file
    with open("times.txt", "a") as f:
        f.write(name + " " + time + "\n")
    
    # Redirect to the ranks page with the name and time attched
    return render_template('ranks.html', name=name, time=time)
    

if __name__ == '__main__':
    app.run(debug=True)