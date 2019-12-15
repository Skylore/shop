from db import db
from controllers import seller_controller, customer_controller

database = db.DataBase()

u1 = database.sign_up('name1', '1234567', 'pass')
u1.setRole('seller')

controller1 = seller_controller.SellerController(u1)

p1 = controller1.add_product('prod_name1', 'prod_desk1')
p2 = controller1.add_product('prod_name2', 'prod_desk2')


u2 = database.sign_up('customer', 'customer_login', 'pass')

controller2 = customer_controller.CustomerController(u2)

controller2.buy_product(p1.getProductId())

controller1.reject_request(p1.getProductId())
