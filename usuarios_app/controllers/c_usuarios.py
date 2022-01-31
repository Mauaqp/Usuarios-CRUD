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
@app.route( '/users/<int:id>')
def readUser(id):
    data = {
        "id" : id
    }
    #El "usuario = ..."" es el nombre con el cual se enlazará a la base de datos con el html
    return render_template( "read_user.html", usuario = Usuario.get_one(data) )

#Ruta para desplegar el usuario que se quiere editar
@app.route( '/users/edit/<int:id>', methods=["GET"] )
def despliegaEditar( id ):
    usuarioAEditar = {
        "id" : id
    }
    resultado = Usuario.get_one( usuarioAEditar )
    return render_template( "edit.html", usuario = resultado)

#Ruta para EDITAR usuarios existentes
@app.route( '/users/edit/<int:id>', methods=["POST"])
def editarUsuario(id):
    usuarioAEditar = {
        #indicar el id es IMPORTANTE para que reconozca la correspondencia en la bd
        "id" : id,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    resultado = Usuario.editarUsuario(usuarioAEditar)
    # siempre revisar que la redirección sea correcta y no esté creando o buscando otras 
    return redirect( "/read" )

#Registrar usuario
@app.route('/', methods=['POST'])
def registro ():
    nuevoUsuario = {
    "first_name" : request.form["first_name"],
    "last_name" : request.form["last_name"],
    "email" : request.form["email"]
    }
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
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


