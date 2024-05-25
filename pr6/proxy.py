class UserDataInterface:
    def get_password(self) -> str:
        raise NotImplementedError("Метод get_password должен быть переопределен")

    def set_password(self, password: str) -> None:
        raise NotImplementedError("Метод set_password должен быть переопределен")
class RealUserData(UserDataInterface):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def get_password(self) -> str:
        return self.password

    def set_password(self, password: str) -> None:
        self.password = password
class UserPasswordProxy(UserDataInterface):
    def __init__(self, real_user_data: RealUserData):
        self.real_user_data = real_user_data

    def get_password(self) -> str:
        return self.real_user_data.get_password()

    def set_password(self, password: str) -> None:
        self.real_user_data.set_password(password)
def main():
    real_user_data = RealUserData(username="GrishaSh", password="12345")
    user_password_proxy = UserPassword-Proxy(real_user_data=real_user_data)

    print(user_password_proxy.get_password())
    user_password_proxy.set_password("grisha12345")
    print(user_password_proxy.get_password())

if __name__ == "__main__":
    main()
