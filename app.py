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
    time = int(request.form['time'])
    
    # Write the name and time to a file
    with open("times.txt", "a") as f:
        f.write(name + " " + str(time) + "\n")
    
    # The ranking system
    if time >= 35:
        rank = "Bronze Strider"
    elif time >= 30:
        rank = "Silver Sprinter"
    elif time >= 27:
        rank = "Gold Pacer"
    elif time >= 24:
        rank = "Platinum Racer"
    elif time >= 21:
        rank = "Diamond Dasher"
    elif time >= 19:
        rank = "Elite Striker"
    elif time >= 17:
        rank = "Champion Runner"
    else:
        rank = "Legendary Phantom"
    
    # Redirect to the ranks page with the name and time attched
    return render_template('ranks.html', name=name, time=time, rank=rank)
    

if __name__ == '__main__':
    app.run(debug=True)