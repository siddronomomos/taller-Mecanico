import dbUser
import user
import tkinter as tk
from tkinter import messagebox
class frmUser(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('User Form')
        self.geometry('300x200')
        self.user = user.user()
        self.dbUser = dbUser.dbUser()
        self.createWidgets()
        self.bind('<Return>', self.save)

    def createWidgets(self):
        self.lblName = tk.Label(self, text='Name:')
        self.lblName.pack()
        self.entName = tk.Entry(self)
        self.entName.pack()
        self.lblUsername = tk.Label(self, text='Username:')
        self.lblUsername.pack()
        self.entUsername = tk.Entry(self)
        self.entUsername.pack()
        self.lblPassword = tk.Label(self, text='Password:')
        self.lblPassword.pack()
        self.entPassword = tk.Entry(self, show='*')
        self.entPassword.pack()
        self.lblProfile = tk.Label(self, text='Profile:')
        self.lblProfile.pack()
        self.entProfile = tk.Entry(self)
        self.entProfile.pack()
        self.btnSave = tk.Button(self, text='Save', command=self.save)
        self.btnSave.pack()
        self.btnUpdate = tk.Button(self, text='Update', command=self.update)
        self.btnUpdate.pack()
        self.btnDelete = tk.Button(self, text='Delete', command=self.delete)
        self.btnDelete.pack()
        self.btnGet = tk.Button(self, text='Get', command=self.get)
        self.btnGet.pack()
        self.btnClear = tk.Button(self, text='Clear', command=self.clear)
        self.btnClear.pack()

    def save(self, event=None):
        self.user.setName(self.entName.get())
        self.user.setUsername(self.entUsername.get())
        self.user.setPassword(self.entPassword.get())
        self.user.setProfile(self.entProfile.get())
        self.dbUser.save(self.user)
        messagebox.showinfo('Save', 'User saved successfully!')
        self.clear()

    def update(self):
        self.user.setName(self.entName.get())
        self.user.setUsername(self.entUsername.get())
        self.user.setPassword(self.entPassword.get())
        self.user.setProfile(self.entProfile.get())
        self.dbUser.update(self.user)
        messagebox.showinfo('Update', 'User updated successfully!')
        self.clear()

    def delete(self):
        self.user.setName(self.entName.get())
        self.user.setUsername(self.entUsername.get())
        self.user.setPassword(self.entPassword.get())
        self.user.setProfile(self.entProfile.get())
        self.dbUser.delete(self.user)
        messagebox.showinfo('Delete', 'User deleted successfully!')
        self.clear()

    def get(self):
        self.user = self.dbUser.get(self.entName.get())
        self.entName.delete(0, tk.END)
        self.entName.insert(0, self.user.getName())
        self.entUsername.delete(0, tk.END)
        self.entUsername.insert(0, self.user.getUsername())
        self.entPassword.delete(0, tk.END)
        self.entPassword.insert(0, self.user.getPassword())
        self.entProfile.delete(0, tk.END)
        self.entProfile.insert(0, self.user.getProfile())

    def clear(self):
        self.entName.delete(0, tk.END)
        self.entUsername.delete(0, tk.END)
        self.entPassword.delete(0, tk.END)
        self.entProfile.delete(0, tk.END)

if __name__ == '__main__':
    app = frmUser()
    app.mainloop()
        