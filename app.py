from flask import render_template, request, url_for, redirect, flash, Flask
import requests


app = Flask(__name__)
app.secret_key = 'the random string'

@app.route('/', methods=['POST', 'GET'])
def searsh():
   if request.method == "POST":
      try:
         query = request.form.get('city')
         if query:
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=51f137b0f0e24042f88fc1883e5eaed0".format(query)
         else:
            url = "http://api.openweathermap.org/data/2.5/weather?q=khartoum&appid=51f137b0f0e24042f88fc1883e5eaed0"
         r = requests.get(url).json()
         weather_data = []
         K = r['main']['temp']-273
         C = round(K, 2)
         weather_info = {
            'city' : r["name"],
            'temp' : C,
            'wind' : r['wind']['speed'],
            'icon' : r['weather'][0]['icon'],
            'des' : r['weather'][0]['description']
         }
         weather_data.append(weather_info)
         return render_template("home.htm", info=weather_data)
      except :
         flash("لمن نتمكن من ايجاد ما تبحث عنه الرجاء المحاولة مرة اخرى", "dengar")
         return render_template("404.htm")

   url = "http://api.openweathermap.org/data/2.5/weather?q=khartoum&appid=51f137b0f0e24042f88fc1883e5eaed0"
   r = requests.get(url).json()
   weather_data = []
   K = r['main']['temp']-273
   C = round(K, 2)
   weather_info = {
      'city' : r['name'],
      'temp' : C,
      'wind' : r['wind']['speed'],
      'icon' : r['weather'][0]['icon'],
      'des' : r['weather'][0]['description']
   }
   weather_data.append(weather_info)
   return render_template("home.htm", info=weather_data)

@app.errorhandler(404)
def page_not_fond(e):
    return render_template("404.htm"), 404

@app.errorhandler(500)
def page_not_fond(e):
    return render_template("500.htm"), 500

@app.errorhandler(403)
def page_not_fond(e):
    return render_template("403.htm"), 403



if __name__ == '__main__':
   app.run()
