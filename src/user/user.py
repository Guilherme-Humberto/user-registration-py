import json

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def getUsers():
        with open('./src/data/users.json', 'r') as file:
            users = file.read()
            return json.loads(users) 

    @staticmethod
    def writeUsers(userData):
        with open('./src/data/users.json', 'w') as file:
            json.dump(userData, file)
            print('[UPDATE USER]: List of users updated')

    def findUser(self, email):
        usersList = self.getUsers()
        userFilter = filter(
            lambda user: email == user['email'], 
            usersList['users']
        )
        return list(userFilter)

    def register(self):
        user = self.findUser(self.email)
        if(len(user) >= 1): 
            return print('[ADD USER]: User already exists')

        user = { 'name': self.name, 'email': self.email }
        userData = self.getUsers()
        userData['users'].append(user)
        
        self.writeUsers(userData)
        print('[ADD USER]: User added')
        return

    def remove(self, email):
        user = self.findUser(email)
        if(len(user) == 0): 
            return print('[REMOVE USER]: User not found')
            
        userData = self.getUsers()
        userData['users'].remove(user[0])
        self.writeUsers(userData)
        print('[REMOVE USER]: User deleted')
        return

    def updateUser(self, oldEmail, newEmail):
        findByOldEmail = self.findUser(oldEmail)
        findByNewEmail = self.findUser(newEmail)

        if len(list(findByOldEmail)) == 0: 
            print('[UPDATE USER]: User not found')
            return
            
        if len(list(findByNewEmail)) >= 1: 
            print('[UPDATE USER]: User already exists')
            return

        userOld = findByOldEmail[0]
        userData = self.getUsers()
        userData['users'].remove(userOld)

        newUser = { 'name': userOld['name'], 'email': newEmail }
        userData['users'].append(newUser)

        self.writeUsers(userData)
        print('[UPDATE USER]: User updated')
        return