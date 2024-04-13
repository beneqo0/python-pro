from flask import Flask
import random
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href=/facts> <h1> linkacz do random faktu <h1> <a>'

@app.route('/nevergonnagiveyouup')
def nevergonagiveuap():
    return "never gona giv ju ap"

@app.route('/facts')
def facts():
    lista=[
        "Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń",
        "Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów",
        "Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych.",
        "Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy",
        ]
    a= random.choice(lista)
    return f'<h1>{a}<h1>' #and '<a href="/"> powrot <a>'

#@app.route('/img')
#def randomimages():
    #imagee=os.listdir('images')
    #image= random.choice(imagee)
   # with open(b'images/image}','rb') as b
    #return 'b'
@app.route("/coinflip")
def coin_flip():
    coin= [ "reszek","orzeł"]
    a = random.choice(coin)
    return a


app.run(debug=True)
