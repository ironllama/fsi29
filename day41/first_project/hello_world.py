from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, Mundo!</p>"

@app.route("/nameform")
def hello_world_form():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
    </style>
</head>

<body>
    <form action="/nameandcolorform" method="POST">
        <label>Name: <input name="name" /></label>
        <label>Color: <input name="color"></label>
        <button>Go!</button>
    </form>
</body>

</html>
"""

@app.route("/nameajax")
def hello_world_ajax():
    ret_str = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
    </style>
</head>

<body>
    <form>
        <label>Name: <input name="name" /></label>
        <label>Color: <input name="color"></label>
        <button type="button">Go!</button>
    </form>
    <script>
        const nameInput = document.querySelector("input");
        const colorInput = document.querySelector("label:nth-child(2)>input");
        const button = document.querySelector("button");

        button.addEventListener("click", () => {
            fetch("/nameandcolorajax", {
                method: "post",
                headers: { "Content-type": "application/json" },
                body: JSON.stringify({
                    name: nameInput.value,
                    color: colorInput.value,
                }),
            }).then(res => res.text())
            .then(res => {
                document.body.innerHTML = res;
            });
        })
    </script>
</body>

</html>
"""
    return ret_str


@app.route("/ping")
def ping():
	return "pong"

@app.route("/party")
def partyparty():
  return """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Party Party!</title>
  <style>
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }
    img {
      height: 400px;
    }
  </style>
</head>

<body>
  <img src="static/excited-party-mode-baby-y6ohsg4asvx4171u.webp" alt="Baby NHL Penguins fan is very excited">
</body>
</html>
"""

@app.get("/nameandcolor")
def name_color():
  in_name = request.args.get('name', 'Adam')
  in_color = request.args.get('color', 'black')
  return f"<h1 style='color: {in_color}'>Hello, {in_name}</h1>"

@app.post("/nameandcolorform")
def name_color_form():
  in_name = request.form.get('name', 'Adam')
  in_color = request.form.get('color', 'black')
  return f"<h1 style='color: {in_color}'>Hello, {in_name}</h1>"

@app.post("/nameandcolorajax")
def name_color_ajax():
  in_json = request.json
  in_name = in_json.get('name', 'Adam')
  in_color = in_json.get('color', 'black')
  return f"<h1 style='color: {in_color}'>Hello, {in_name}</h1>"

# Expects x-www-form-urlencoded data and returns 'text/plain'
@app.route("/add10", methods=['POST'])
def add10():
  in_form = request.form
  in_num = int(in_form.get('number', '0'))
  return str(in_num + 10)  # Must cast to string for return

# Expects application/json and return application/json
@app.post("/multiply10")
def multiply10():
  in_json = request.json
  in_num = int(in_json.get('number', '0'))
  return { "result": in_num * 10 }  # Dictionary gets turned into JSON string


valid_tokens = ["apple", "orange", "pear"]
@app.get("/valid_token/<new_token>")
def check_token(new_token):
    if new_token in valid_tokens:
        return ("GOOD!")
    else:
        return ("BAD!")
