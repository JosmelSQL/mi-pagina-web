from flask import Flask, render_template
import os

# Forzamos la ruta absoluta sin importar de dónde lea Flask
ruta_base = os.path.dirname(os.path.abspath(__file__))
ruta_templates = os.path.join(ruta_base, 'templates')
ruta_static = os.path.join(ruta_base, 'static')

# Le pasamos las rutas absolutas directamente a Flask
app = Flask(__name__, template_folder=ruta_templates, static_folder=ruta_static)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/preguntas')
def preguntas():
    return render_template('preguntas.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    # ¡Cambiamos el puerto a 5002!
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port)
    # app.run(debug=True, port=5002)