import nzpy
import logging

from dotenv import dotenv_values


class Netezza:

    def connect(self):
        config = dotenv_values(".env")

        host = config.get('NZ_HOST') or 'localhost'
        port = 5480
        database = config.get('NZ_DATABASE')
        user = config.get('NZ_USER')
        password = config.get('NZ_PASSWORD')

        conn = nzpy.connect(user=user,
                            password=password,
                            host=host,
                            port=port,
                            database=database,
                            securityLevel=1,
                            logLevel=logging.DEBUG)
        if conn is None:
            logging.error('Connection to Netezza failed')

        return conn
