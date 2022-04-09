try:
    from api import app
    import unittest

except Exception as e:
    print(f'Some Modules are Missing {e}')


class FlaskTestCase(unittest.TestCase):
    
    
    #Check for the response 200
    def test_UserStatusSearch(self):
        tester = app.test_client(self)
        response = tester.get("/user_status?user_id=1&date=2017-01-01T10:00:00")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_IpRangeSearch(self):
        tester = app.test_client(self)
        response = tester.get("/ip_city?ip=10.12.0.100")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)        

    def test_AggregateUserCity(self):
        tester = app.test_client(self)
        response = tester.get("/user_city?user_status=paying&city=Munich")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    # check if the content is application/json
    def test_UserStatusSearch_content(self):
        tester = app.test_client(self)
        response = tester.get("/user_status?user_id=1&date=2017-01-01T10:00:00")
        self.assertEqual(response.content_type, "application/json")
    
    def test_IpRangeSearch_content(self):
        tester = app.test_client(self)
        response = tester.get("/ip_city?ip=10.12.0.100")
        self.assertEqual(response.content_type, "application/json")

    def test_AggregateUserCity_content(self):
        tester = app.test_client(self)
        response = tester.get("/user_city?user_status=paying&city=Munich")
        self.assertEqual(response.content_type, "application/json")

    
    # check for Data returned
    def test_UserStatusSearch_data(self):
        tester = app.test_client(self)
        response = tester.get("/user_status?user_id=1&date=2017-01-01T10:00:00")
        self.assertTrue(b'{"user_status":"paying"}' in response.data)

    def test_IpRangeSearch_data(self):
        tester = app.test_client(self)
        response = tester.get("/ip_city?ip=10.12.0.100")
        self.assertTrue(b'{"city":"Munich"}' in response.data)

    def test_AggregateUserCity_data(self):
        tester = app.test_client(self)
        response = tester.get("/user_city?user_status=paying&city=Munich")
        self.assertTrue(b'{"product_price":241.0}' in response.data)


if __name__ == "__main__":
    unittest.main()
