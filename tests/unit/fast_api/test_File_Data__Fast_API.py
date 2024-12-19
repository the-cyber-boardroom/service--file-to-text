from unittest                                                  import TestCase
from service_file_to_text.fast_api.File_To_Text__Fast_API      import File_To_Text__Fast_API
from service_file_to_text.fast_api.routes.Routes__Info         import ROUTES_PATHS__INFO
from service_file_to_text.markitdown.routes.Routes__Markitdown import ROUTES_PATHS__MARKITDOWN


class test_File_To_Text__Fast_API(TestCase):

    def setUp(self):
        self.fast_api = File_To_Text__Fast_API()

    def test_base_path(self):
        assert self.fast_api.base_path == '/'
        assert self.fast_api.enable_cors is True

    def test_setup_routes(self):
        self.fast_api.setup()
        routes = self.fast_api.routes_paths()

        assert routes == sorted(['/', '/config/info', '/config/status', '/config/version'] \
                                 + ROUTES_PATHS__INFO                                      \
                                 + ROUTES_PATHS__MARKITDOWN                                )



