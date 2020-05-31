import requests
from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecret'

# db = SQLAlchemy(app)


# class City(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)


def get_weather_data(term1=''):
    li = []
    if term1 != '':
        r = requests.get(
            f'https://api.unsplash.com/search/collections?query={term1}&page=1&per_page=21&client_id=a3LeIdw1sJLTf4wV3b-9K9GUZ8UJ-PF9QkwL1mLAUYc')
        data = r.json()
        for img_data in data['results']:
            try:
                file_name = str(img_data['id']) + ".jpg"
                img_url = img_data['preview_photos'][0]['urls']['small']
                li.append(img_url)
            except:
                continue
        return li
    else:
        r = requests.get(
            f'https://api.unsplash.com/photos/random?count=21&client_id=a3LeIdw1sJLTf4wV3b-9K9GUZ8UJ-PF9QkwL1mLAUYc')
        data = r.json()
        for i in data:
            li.append(i['urls']['small'])
        return li


# @app.route('/')
# def index_get():
    # cities = City.query.all()
    # cities = cities[-2:]
    # cities = cities[::-1]

    # weather_data = []
    # i = 0

    # for city in cities:

    #     r = get_weather_data(city.name)
    #     print(city.name)

    #     weather = {
    #         'city': city.name,
    #         'temperature': r['main']['temp'],
    #         'description': r['weather'][0]['description'],
    #         'icon': r['weather'][0]['icon'],
    #     }

    #     weather_data.append(weather)
    # i += 1
    # if i == 1:
    #     break

    # return render_template('image.html', weather_data=weather_data)


@app.route('/', methods=['POST', 'GET'])
def index_post():
    err_msg = ''
    new_city = request.form.get('term')

    image_data = get_weather_data(new_city)

    if image_data != []:
        print("data found")
    #     # new_city_obj = City(name=new_city)

    #     # db.session.add(new_city_obj)
    #     # db.session.commit()
    else:
        print("data not found")
        err_msg = f'sorry the term {new_city} did not yield any results!'

    if err_msg:
        flash(err_msg, 'error')
    # else:
    #     flash('City added succesfully!')

    # return redirect(url_for('index_get'), data=new_city_data)
    # print(image_data)
    return render_template('index.html', image_data=image_data)


# @app.route('/aboutme', methods=['GET', 'POST'])
# def aboutme():
#     return render_template('about.html')


# @app.route('/showall')
# def showall():
#     cities = City.query.all()
#     cities = cities[::-1]
#     li = []
#     weather_data = []

#     for city in cities:

#         r = get_weather_data(city.name)
#         print(r)
#         if city.name.lower() not in li:
#             weather = {
#                 'city': city.name,
#                 'temperature': r['main']['temp'],
#                 'description': r['weather'][0]['description'],
#                 'icon': r['weather'][0]['icon'],
#             }

#             weather_data.append(weather)
#             li.append(city.name.lower())

#     return render_template('weather.html', weather_data=weather_data)


# @app.route('/random', methods=['POST', 'GET'])
# def randompost():
    #     err_msg = ''
    #     new_city = request.form.get('city')

    #     new_city_data = get_weather_data(new_city)

    #     if new_city_data['cod'] == 200:
    #         new_city_obj = City(name=new_city)

    #         db.session.add(new_city_obj)
    #         db.session.commit()
    #     else:
    #         err_msg = f'City {new_city} does not exist in the world!'

    #     if err_msg:
    #         flash(err_msg, 'error')
    #     else:
    #         flash('City added succesfully!')

    #     return redirect(url_for('showall'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
