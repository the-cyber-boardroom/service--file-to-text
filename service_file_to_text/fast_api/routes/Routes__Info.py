from osbot_fast_api.api.Fast_API_Routes  import Fast_API_Routes
from service_file_to_text.utils.Version import version__service_file_to_text

ROUTES_PATHS__INFO = ['/info/version',  '/info/ping']

class Routes__Info(Fast_API_Routes):
    tag :str = 'info'

    def ping(self):
        return 'pong (edited on live OSS session)'

    def version(self):
        return {'version': version__service_file_to_text}

    
    def setup_routes(self):
        self.add_route_get(self.ping)
        self.add_route_get(self.version)

