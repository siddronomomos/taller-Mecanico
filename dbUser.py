import conection as con
import user
class dbUser:
    def __init__(self):
        createDB = con.connection()
        cursor = createDB.open()
        cursor.execute("CREATE TABLE IF NOT EXISTS user (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), username VARCHAR(20), password VARCHAR(20), profile VARCHAR(20))")
        createDB.commit()
        createDB.close()


    def save(self, user):
        conn = con.connection()
        cursor = conn.open()
        cursor.execute("INSERT INTO user (id, name, username, password, profile) VALUES (%s, %s, %s, %s, %s)", (user.getID(), user.getName(), user.getUsername(), user.getPassword(), user.getProfile()))
        conn.commit()
        conn.close()
        return True
    
    def update(self, user):
        conn = con.connection()
        cursor = conn.open()
        cursor.execute("UPDATE user SET name = %s, username = %s, password = %s, profile = %s WHERE id = %s", (user.getName(), user.getUsername(), user.getPassword(), user.getProfile(), user.getID()))
        conn.commit()
        conn.close()
        return True
    
    def delete(self, user):
        conn = con.connection()
        cursor = conn.open()
        cursor.execute("DELETE FROM user WHERE id = %s", (user.getID(),))
        conn.commit()
        conn.close()
        return True
    
    def get(self, id):
        conn = con.connection()
        cursor = conn.open()
        cursor.execute("SELECT * FROM user WHERE id = %s", (id,))
        row = cursor.fetchone()
        conn.close()
        if row is not None:
            userObj = user.user()
            userObj.setID(row[0])
            userObj.setName(row[1])
            userObj.setUsername(row[2])
            userObj.setPassword(row[3])
            userObj.setProfile(row[4])
            return userObj
        return False