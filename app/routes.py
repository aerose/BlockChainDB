from flask import Flask,request, send_from_directory,render_template, redirect, url_for
import os
from app.blockChain import *
from app.top import top
from app.Constants import mng

import argparse
import threading
target = mng

import parser

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
        #target.strg()
        return str(s)


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/add/add')
def add_add():
    if request.method == 'GET':
        data = request.args.get('data')
        target.bc.new_data(data)
        target.bc.new_block(0)
        #target.strg()
        return target.bc.printAll()


@app.route('/find')
def find():
    return render_template('index2.html')


@app.route('/find/find')
def find_find():
    if request.method == 'GET':
        target.bc.find(request.args.get('find'))

        return target.bc.spFind(request.args.get('find'))

@app.route('/revoke')
def revoke():
    s = target.bc.revoke()
    #target.strg()
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

@app.route('/old')
def index_old():

    method_name=["use","create", "delete"] 
    method_default = "use"

    if request.args.get("select_method") in method_name:
        method_default = request.args.get("select_country")

    return render_template("index.html", method=method_name, default=method_default)



@app.route('/rese')
def res():
    return render_template('rese.html')

@app.route('/rese/add')
def rese_add():  # 视图函数
    if request.method == 'GET':  # 请求方式是get
        name = request.args.get('name')  # args取get方式参数
        age = request.args.get('age')
        hobby = request.args.getlist('hobby')  # getlist取一键多值类型的参数
        return "姓名：%s 年龄：%s 爱好：%s" % (name, age, hobby)


@app.route('/templat')
def templat():
    ctx = {
        "name": '老王',
        "age": 12,
        "hobby": ["下棋", '电影'],
        "test": {"a": 1, "b": 2}
    }

    return render_template('templat.html', **ctx)  # 一定要是关键字参数 **ctx