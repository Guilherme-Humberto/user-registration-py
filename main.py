from src.user import user

name = 'Guilherme'
email = 'primeiro@email.com'
newEmail = 'segundo@email.com'

user = user.User(name, email)

user.register()
user.updateUser(email, newEmail)
user.remove(email)