# Задание No9
# 📌 Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна(шапка, меню, подвал), и
# дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# 📌 Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def my_shop():
    return render_template('index.html')


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
    # return render_template('odezhda.html', **clothes, clothes_list=clothes_list)


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
        },        {
            'name': 'БОТИНКИ МОТОР 10 КПП',
            'size': '36-44',
            'amount': 33
        },          {
            'name': 'Ботинки PEZZOL ИНДИГО S3',
            'size': '39-44',
            'amount': 12 
        }
    ]
    return render_template('obuv.html', content=shoes_list)
    # return render_template('obuv.html', **shoes, shoes_list=shoes_list, content=shoes_list)


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
        },{
            'name': 'МАСКА SPIROTEK 9000',
            'size': 's m l',
            'amount': 11
        }
    ]
    # return render_template('accessories.html', **accessories, accessories_list=accessories_list, content=accessories_list)
    return render_template('accessories.html', content=accessories_list)



if __name__ == '__main__':
    app.run(debug=True)
