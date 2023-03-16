from dotenv import dotenv_values


class Auth:

    def user_loader(self, username, password):
        config = dotenv_values(".env")

        the_username = config.get('AUTH_USERNAME')
        the_password = config.get('AUTH_PASSWORD')

        if username == the_username and password == the_password:
            return {"username": username}

        return None
