from conection import Connection as con
from user import user
class dbUser:
    def __init__(self):
        self.connection = con()
        self.cursor = self.connection.open()
        if self.cursor == None:
            raise Exception("Error al conectar a la base de datos")
        
    def save(self, user: user) -> bool:
        try:
            self.cursor.execute("""
                INSERT INTO usuarios (nombre, user_name, password, perfil)
                VALUES (%s, %s, %s, %s)
            """, (user.getNombre(), user.getUserName(), user.getPassword(), user.getPerfil()))
            self.connection.commit()
        except:
            return False
        return True
   
    def update(self, user: user) -> bool:
        try:
            self.cursor.execute("""
                UPDATE usuarios
                SET nombre = %s, user_name = %s, password = %s, perfil = %s
                WHERE usuario_id = %s
            """, (user.getNombre(), user.getUserName(), user.getPassword(), user.getPerfil(), user.getID()))
            self.connection.commit()
        except:
            return False
        return True
    
    def delete(self, user: user) -> bool:
        try:
            self.cursor.execute("""
                DELETE FROM usuarios
                WHERE usuario_id = %s
            """, (user.getID(),))
            self.connection.commit()
        except:
            return False
        return True
    
    def get(self, user: user) -> user:
        try:
            self.cursor.execute("""
                SELECT * FROM usuarios
                WHERE usuario_id = %s
            """, (user.getID(),))
            row = self.cursor.fetchone()
            user.setID(row[0])
            user.setNombre(row[1])
            user.setUserName(row[2])
            user.setPassword(row[3])
            user.setPerfil(row[4])
        except:
            return None
        return user