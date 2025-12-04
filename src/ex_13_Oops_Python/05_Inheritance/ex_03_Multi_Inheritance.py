class APIBase:
    def api_auth(self):
        print('Authenticatin API')


class DBBase:
    def db_connection(self):
        print('connection to the DB')


class TestHybrid(APIBase, DBBase):
    def run(self):
        self.api_auth()
        self.db_connection()
        print('Test Case Running')


obj = TestHybrid()
obj.run()