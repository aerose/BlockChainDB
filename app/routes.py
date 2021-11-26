from flask import Flask,request,render_template

from app.blockChain import *
from app.top import top
from app.Constants import mng


target = mng
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = app.config.get('UPLOAD_FOLDER')


@app.route('/create')
def create_create():
    if request.method == 'GET':
        name = request.args.get('name')
        s = target.list_add(name)
        return str(s)

@app.route('/showDB')
def showDB():
    return target.showDB()


@app.route('/use')
def use():
    if request.method == 'GET':
        name = request.args.get('DBname')
        return str(target.use(name))
    

@app.route('/delDB')
def delDB():
    if request.method == 'GET':
        name = request.args.get('name')
        s = str(target.delete(name))
        return str(s)




@app.route('/add/add')
def add_add():
    if request.method == 'GET':
        data = request.args.get('data')
        target.bc.new_data(data)
        target.bc.new_block(0)
        return target.bc.printAll()




@app.route('/find/find')
def find_find():
    if request.method == 'GET':
        target.bc.find(request.args.get('find'))

        return target.bc.spFind(request.args.get('find'))

@app.route('/revoke')
def revoke():
    s = target.bc.revoke()
    return str(s)

@app.route('/showall')
def showall():
    return target.bc.printAll()

@app.route('/quit')
def quit():
    target.strg()
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def index2():
    return render_template('index2.html')




