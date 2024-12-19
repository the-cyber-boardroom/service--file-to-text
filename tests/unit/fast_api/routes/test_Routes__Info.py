from unittest                                           import TestCase
from service_file_to_text.fast_api.routes.Routes__Info import Routes__Info
from service_file_to_text.utils.Version                import version__service_file_to_text


class test_Routes__Info(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.routes_info = Routes__Info()

    def test_version(self):
        assert self.routes_info.version() == {'version': version__service_file_to_text}

    def test_setup_routes(self):
        with self.routes_info as _:
            assert _.routes_paths() == []
            _.setup_routes()
            assert _.routes_paths() == ['/ping', '/version' ]