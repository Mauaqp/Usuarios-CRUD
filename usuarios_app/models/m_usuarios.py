from usuarios_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    #Metodo de creación de usuarios
    @classmethod
    def agregaUsuario( cls, nuevoUsuario ):
        query = "INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
        resultado = connectToMySQL( "users_crud" ).query_db( query, nuevoUsuario )
        return resultado
    
    #Método para obtener lista de Usuarios
    @classmethod
    def obtenerListaUsuarios( cls ):
        query = "SELECT * FROM users;"
        resultado = connectToMySQL( "users_crud" ).query_db( query )
        listaUsuarios = []
        print(listaUsuarios)
        for u in resultado:
            listaUsuarios.append(cls(u))
        return listaUsuarios