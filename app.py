import os
port = os.environ.get('PORT', 5000)
from bottle import route, run
run(host='0.0.0.0', port=port)
# port = int(os.environ.get('PORT', 17995))
print(dir(os))
a=1+1
b=2+2
a+b
print ('''<html>
<head><title>My first Python CGI app</title></head>
<body>
<p>Hello, 'world'!</p>
</body>
</html>''')
# Run the app.
