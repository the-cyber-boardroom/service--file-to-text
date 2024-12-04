from unittest                                           import TestCase
from cbr_custom_open_sec_summit.fast_api.routes.Routes__Info import Routes__Info
from cbr_custom_open_sec_summit.utils.Version                import version__cbr_custom_open_sec_summit


class test__int__Routes__UK(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.routes_open_sec_summit = Routes__Info()

    def test_routes_setup(self):
        with self.routes_open_sec_summit as _:
            assert _.tag == 'info'
            _.setup_routes()
            assert '/version' in _.routes_paths()

    def test__version(self):
        with self.routes_open_sec_summit as _:
            assert _.version() == { 'version': version__cbr_custom_open_sec_summit }
