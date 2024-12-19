from unittest                                           import TestCase
from service_file_to_text.fast_api.routes.Routes__Info import Routes__Info
from service_file_to_text.utils.Version                import version__service_file_to_text


class test__int__Routes__UK(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.routes_file_to_text = Routes__Info()

    def test_routes_setup(self):
        with self.routes_file_to_text as _:
            assert _.tag == 'info'
            _.setup_routes()
            assert '/version' in _.routes_paths()

    def test__version(self):
        with self.routes_file_to_text as _:
            assert _.version() == { 'version': version__service_file_to_text }
