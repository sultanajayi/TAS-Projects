class User :
    __password = "password"

    def get_password(self):
        return "self.__password"


class ActiveUser(User):

    def get_password(self):
        return "*********"

activeUser = ActiveUser()

print(activeUser.get_password())
