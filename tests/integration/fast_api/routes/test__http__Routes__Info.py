from unittest                                     import TestCase
from osbot_fast_api.utils.Fast_API_Server         import Fast_API_Server

from service_file_to_text.testing.file_to_text__objs_for_tests import file_to_text__fast_api__app
from service_file_to_text.utils.Version                           import version__service_file_to_text



class test__http__Routes__Info(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fast_api_server = Fast_API_Server(app=file_to_text__fast_api__app)
        cls.fast_api_server.start()
        assert cls.fast_api_server.is_port_open() is True

    @classmethod
    def tearDownClass(cls):
        cls.fast_api_server.stop()
        assert cls.fast_api_server.is_port_open() is False

    def test_http__uk__articles_html(self):
        response = self.fast_api_server.requests_get('/info/version')
        assert response.status_code == 200
        assert response.json()      == {'version': version__service_file_to_text }
