import xmlrpclib

from flask import Flask
app = Flask(__name__)
# app.run(host= '172.20.10.3')
url = 'http://192.168.0.106:8069'
db = 'sms'
username = 'admin'
password = 'admin'
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "kike",
}])

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/tfi/zona/<string:name>")
def tfi(name):
    id = models.execute_kw(db, uid, password, 'tfi.zona', 'create', [{
    'name': name,}])
    if id:
        return "Zona creada: " + name + " con id: " + str(id)
    else:
        return "Error al crear zona"

# @app.route("/tfi/zona/")
# def zona():
#     return "Hello Zona"

if __name__ == "__main__":
    app.run(host='192.168.0.106',port=8080)

