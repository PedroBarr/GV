#-------------------------------------------------------------------------------
# Name:        index
# Purpose:     index file for adoracionysanidad.com
#
# Author:      Pedro Barr
#
# Created:     09/19/1999
# Copyright:   (c) estudiantes 2020
# Licence:     Ur Anus
#-------------------------------------------------------------------------------

#importe de librerias
from flask import Flask, render_template, redirect, url_for, session

#inicializacion de la aplicacion
app = Flask(__name__)
transm="Viernes 20:00 Hs COL"

#inicializacion de la llave secreta
app.secret_key="appLogin"

#configuracion de ruta /
@app.route('/')
def index():
    session['mess']={}
    session['mess']['stream'] = f"Proxima transmisión %s" % transm
    return render_template('index.html')

#configuracion de ruta /linked
@app.route('/linked')
def link():
    return redirect('')

#configuracion de ruta /website
@app.route('/website')
def website():
    session['mess']={}
    return render_template('website.html')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
