# İçe Aktarma
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Elektrikli cihazların enerji tüketimini hesaplamaya olanak tanıyan değişkenler
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# İlk sayfa
@app.route('/')
def index():
    return render_template('index.html')
# İkinci sayfa
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Üçüncü sayfa
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Hesaplama
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# Form
@app.route('/form')
def form():
    return render_template('form.html')

#Formun sonuçları
@app.route('/submit', methods=['POST'])
def submit_form():
    # Veri toplama için değişkenleri tanımlayın
    name = request.form['isim']
    email = request.form['email']
    adres= request.form['address']
    date= request.form['date']

    # Verilerinizi kaydedebilir veya e-posta ile gönderebilirsiniz
    with open('form.txt', 'a',) as f:
        f.write(name + '/'),
        f.write(email + '/'),
        f.write(adres + '/'),
        f.write(date + '/')

    return render_template('form_result.html',
                           # Değişkenleri buraya yerleştirin
                           name=name,
                           email=email,
                           adres=adres,
                           date=date
                           )
    

app.run(debug=True)
