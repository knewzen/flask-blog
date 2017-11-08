from flask import render_template, request, redirect, flash, url_for, \
session, jsonify
from app.models.User import User
from config.database import db
from flask_login import login_user
from . import bcrypt

class AuthController(object):


    # login view
    def login(self):
        return render_template('auth/login/index.html')

    def login_check(self):
        users = User()
        form = request.form

        username = form['username']
        password = form['password']

        try:
            user = users.query.filter_by(username=username).first()

            if not user:
                raise Exception('maaf ada yang salah')

            hash_data = bcrypt.check_password_hash(user.password, password)

            if hash_data :
                session['id']       = user.id
                session['username'] = user.username

                return session['username']
            else:
                raise Exception("maaf password atau username salah")  
        except Exception as e:
            flash('maaf password anda salah','danger')
            return redirect(url_for('route.login')) 

             



    # register view 
    def register(self):
        return render_template('auth/register/index.html')

    def register_check(self):

        fullname = request.form['fullname']
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password'])

        check_data = self.is_data_exist(username)
        
        if check_data :
            flash('maaf username telah ada, silahkan menggunakan username yang lain','danger')
            return redirect(url_for('route.register'))

        user = User(fullname=fullname,username=username,password=password)
        db.session.add(user)
        db.session.commit()

        flash('berhasil bertambah , silahkan login','success')
        return redirect(url_for('route.register'))

    def is_data_exist(self,args):

        users = User()
        user = users.query.filter_by(username=args).first()

        if(user):
            return True
        else:
            return False
    


        
