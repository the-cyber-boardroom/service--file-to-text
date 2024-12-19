from unittest                                                           import TestCase
from service_file_to_text.testing.file_to_text__objs_for_tests import file_to_text__fast_api__client
from service_file_to_text.utils.Version                           import version__service_file_to_text



class test__client__Routes__Info(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = file_to_text__fast_api__client

    def test_raw__uk__homepage(self):
        response = self.client.get('/info/version')
        assert response.status_code == 200
        assert response.json()      == {'version': version__service_file_to_text }

