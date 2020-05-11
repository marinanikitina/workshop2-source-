from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY']='123456'

@app.route('/')
def start():
    return 'hi there'


@app.route('https://workshop2nikitina.herokuapp.com/api/<action>', methods=['GET'])
def apiget(action):
    if action == "client":
        return render_template("client.html", client=client_dictionary)

    elif action == "event":
        return render_template("event.html", event=event_dictionary)

    elif action == "all":
        return render_template("all.html", client=client_dictionary, event=event_dictionary)

    else:
        return render_template("404.html", action_value=action)


@app.route('https://workshop2nikitina.herokuapp.com/api/client/submit', methods=['POST'])
def client_submit():
    if (request.method == 'POST'):
        return str(request.form['first_name']) + " " + str(request.form['number'])


@app.route('/api/event/submit', methods=['POST'])
def event_submit():
    if (request.method == 'POST'):
        return str(request.form['name']) + " " + str(request.form['price'])


if __name__ == '__main__':
    client_dictionary = {
        "client_name": "Bob",
        "client_number":"20-20-32",
    }

    event_dictionary = {
        "event_name": "Concert",
        "event_price": 100,
    }

    app.run()
