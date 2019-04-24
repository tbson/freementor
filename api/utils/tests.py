from django.test import TestCase
from utils.helpers.res_tools import getToken
# Create your tests here.


class UtilsTestCase(TestCase):

    def test_getToken(self):
        input = {
            'HTTP_COOKIE': ' sessionid=3eilw4un5izyfat3rd6lf6tga28apy9q; Domain=None; expires=None; Max-Age=None; Path=/',
            'PATH_INFO': '/api/v1/admin/profile/',
            'REMOTE_ADDR': '127.0.0.1',
            'REQUEST_METHOD': 'GET',
            'SCRIPT_NAME': '',
            'SERVER_NAME': 'testserver',
            'SERVER_PORT': '80',
            'SERVER_PROTOCOL': 'HTTP/1.1',
            'QUERY_STRING': '',
            'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyOCwidXNlcm5hbWUiOiJ0YnNvbiIsImV4cCI6MTUwMDI3ODQ2OCwiZW1haWwiOiJ0YnNvbjg3QGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTAwMDE5MjY4fQ.P__R3CdRRdPFI6IkpMFeFKdEoK6pkqxieKdMqJ3It7I'
        }
        self.assertEqual(
            getToken(input),
            'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyOCwidXNlcm5hbWUiOiJ0YnNvbiIsImV4cCI6MTUwMDI3ODQ2OCwiZW1haWwiOiJ0YnNvbjg3QGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTAwMDE5MjY4fQ.P__R3CdRRdPFI6IkpMFeFKdEoK6pkqxieKdMqJ3It7I'
        )
        self.assertEqual(
            getToken({}),
            ''
        )
