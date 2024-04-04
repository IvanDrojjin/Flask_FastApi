# Задание
# 📌 Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан
# cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# 📌 На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён
# cookie-файл с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.


from flask import Flask, render_template, request, redirect, url_for, session, make_response, flash
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'7d4bda27fba3c41496e71c00'
'''
import os
print(os.urandom(12).hex())
  # get new secret key from Python Console   '7d4bda27fba3c41496e71c00'
'''


@app.route('/')
def my_shop():
    if 'username' in session:
        username = session['username']
        mail = session['mail']
        return render_template('index.html', username=username, mail=mail)
    else:
        return redirect(url_for('login'))


@app.route('/clothes/')
def clothes():
    clothes = {
        'name': 'Наименование товара',
        'size': 'Размерный ряд',
        'amount': 'В наличии'
    }

    clothes_list = [
        {
            'name': 'КУРТКА АТОМ',
            'size': 'XS, S, M, L, XL, XXL, XXXL',
            'amount': 13
        },
        {
            'name': 'БРЮКИ АТОМ',
            'size': 'S, M, L, XXL',
            'amount': 25
        },
        {
            'name': 'Брюки',
            'size': 'XS, S, L, XXXL',
            'amount': 12
        }
    ]
    return render_template('odezhda.html', content=clothes_list)


@app.route('/shoes/')
def shoes():
    shoes = {
        'name': 'Наименование товара',
        'size': 'Размерный ряд',
        'amount': 'В наличии'
    }

    shoes_list = [
        {
            'name': 'Ботинки ЭПСИЛОН ЭП-1 электропроводящие',
            'size': '40-36',
            'amount': 15
        }, {
            'name': 'БОТИНКИ МОТОР 10 КПП',
            'size': '36-44',
            'amount': 33
        }, {
            'name': 'Ботинки PEZZOL ИНДИГО S3',
            'size': '39-44',
            'amount': 12
        }
    ]
    return render_template('obuv.html', content=shoes_list)


@app.route('/accessories/')
def accessories():
    accessories = {
        'name': 'Наименование товара',
        'size': 'Размеры',
        'amount': 'В наличии'
    }

    accessories_list = [
        {
            'name': 'КАСКА РОСОМЗ RFI-3 BIOT',
            'size': 's m l',
            'amount': 8
        },
        {
            'name': 'ОЧКИ I-SPECTOR БРАЙТОН',
            'size': 's m l',
            'amount': 10
        }, {
            'name': 'МАСКА SPIROTEK 9000',
            'size': 's m l',
            'amount': 11
        }
    ]
    return render_template('accessories.html', content=accessories_list)


@app.get('/login/')
def checker_get():
    return render_template('login.html')


@app.post('/login/')
def login():
    if request.method == 'POST':
        if not request.form['username']:
            flash('Ошибка, забыли ввести имя !', 'danger')
            return redirect(url_for('login'))
        if not request.form['mail']:
            flash('Ошибка, забыли ввести почту !', 'danger')
            return redirect(url_for('login'))
        # session
        session['username'] = escape(request.form.get('username'))
        session['mail'] = escape(request.form.get('mail'))
        # Cookie
        response = make_response(render_template('index.html', username=session['username'], mail=session['mail']))
        response.set_cookie('username', session['username'])
        response.set_cookie('mail', session['mail'])
        return response


@app.route('/logout/')
def logout():
    session.pop('username', None)  # remove key&value
    session.pop('mail', None)
    '''
    According to Flask's API their Session class is a wrapper around a python Dict. 
    According to the python documentation for dict.pop(): pop(key[, default])
    If key is in the dictionary, remove it and return its value, else return default. 
    If default is not given and key is not in the dictionary, a KeyError is raised.
    '''
    print(f'(Exit) username: {request.cookies.get("username")}')
    print(f'mail: {request.cookies.get("mail")}')
    response = make_response(render_template('login.html'))
    response.delete_cookie("username")
    response.delete_cookie("mail")
    # response.set_cookie(*request.cookies, expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
