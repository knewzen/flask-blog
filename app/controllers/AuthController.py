from flask import render_template, request, redirect, flash, url_for
from app.models.User import User
from config.database import db
from . import bcrypt

class AuthController(object):


    def login(self):
        return render_template('auth/login/index.html', users=usr)
        
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

        
