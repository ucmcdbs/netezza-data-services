import falcon
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend

from routes.index import Index
from routes.store_sales import StoreSales
from util.netezza import Netezza
from util.auth import Auth

# netezza connection
nz = Netezza().connect()

# auth
basic_auth = BasicAuthBackend(Auth().user_loader)
auth_middleware = FalconAuthMiddleware(basic_auth, exempt_routes=['/'])

# falcon
api = falcon.App(middleware=[auth_middleware])

# items
api.add_route('/', Index())
api.add_route('/stores/{store}/sales', StoreSales(nz))
