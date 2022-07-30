from ninja import NinjaAPI

from core.apis.bank_api import api as bank_api
from core.apis.user_api import api as user_api
from core.apis.product_category_api import api as category_api
from core.apis.product_api import api as product_api
from core.apis.purchase_api import api as purchase_api

api = NinjaAPI()

api.add_router('', bank_api)
api.add_router('', user_api)
api.add_router('', category_api)
api.add_router('', product_api)
api.add_router('', purchase_api)