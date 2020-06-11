from flask import Flask,render_template,request,redirect,flash,url_for
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cities.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

def get_weather_data(city):
    url =f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=metric&appid=2867881485a7b01c5e1ccac12c6679de'
    return requests.get(url).json()

@app.route('/', methods=['GET','POST'])
def index():
    errormsg1 = "City does not exist."
    errormsg2 = "City is already added"
    errormsg3 = "Please type a city"
    if request.method == 'POST':
        new_city = request.form['city'].title()
        if new_city:
            new_city_object = City(name=new_city)
            existing_city = City.query.filter_by(name=new_city).all()
            if not existing_city:
                new_city_data = get_weather_data(new_city)
                #print(new_city_data)
                if new_city_data['cod'] == 200:
                    db.session.add(new_city_object)
                    db.session.commit()
                    flash("City Added!")
                else:
                    flash(errormsg1,'error')
            else:
                flash(errormsg2, 'error')
        else:
            flash(errormsg3, 'error')
        return redirect('/')
    else:
        all_cities = City.query.all()
        weather_info = []
        for city in all_cities:
            get_data = get_weather_data(city.name)
            weather_data = {
                "id":city.id,
                "City":city.name.title(),
                "Current Temperature":round(get_data['main']['temp'],1),
                "Humidity":round(get_data['main']['humidity'],1),
                "Description":get_data['weather'][0]['description']
                }

            weather_info.append(weather_data)       #list of weather data
            #for details in weather_info:
                #print(details)
        return render_template('index.html', weather_info=weather_info)


@app.route('/delete/<int:id>')
def delete(id):
    city_to_delete = City.query.get_or_404(id)
    db.session.delete(city_to_delete)
    db.session.commit()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
