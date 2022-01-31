from flask import render_template, request, redirect, session, flash
from usuarios_app import app
from usuarios_app.models.m_usuarios import Usuario
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt( app )

@app.route( '/', methods=['GET'] )
def inicio():
    return render_template( "create.html" )

#ruta read
@app.route( '/read', methods=['GET'] )
def read():
    listaUsuarios= Usuario.obtenerListaUsuarios()
    return render_template( "read.html", listaUsuarios = listaUsuarios )

#Ruta para agregar nuevos usuarios
@app.route( '/users/new', methods=['GET'] )
def newUser():
    return render_template( "create.html" )

#Ruta para agregar nuevos usuarios
@app.route( '/users/<first_name>', methods=['GET'] )
def readUser():
    return render_template( "read_user.html" )

#Registrar usuario
@app.route('/', methods=['POST'])
def registro ():
    nuevoUsuario = {
    "first_name" : request.form["first_name"],
    "last_name" : request.form["last_name"],
    "email" : request.form["email"]
    }
    # session["first_name"] = request.form["first_name"]
    # session["last_name"] = request.form["last_name"]
    resultado = Usuario.agregaUsuario( nuevoUsuario )
    return redirect( '/read' )

#Eliminar usuario
@app.route('/users/remove/<id>', methods=['POST'])
def eliminarUsuario (id):
    usuarioAEliminar = {
        "id" : id
    }
    resultado = Usuario.eliminarUsuario(usuarioAEliminar)
    return redirect('/read')


