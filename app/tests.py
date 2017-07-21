
class UserInfo:
    def __init__(self, username, password):
        self.username = "username"
        self.password = "password"
class Account:
    def __init__(self, session):
        self.index = "index"
        self.activity = "activity"
        self.date = "date"
        self.session = True
        self.bucket_save = {self.activity : self.date}

