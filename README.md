# [E-Commerce Blueprint](https://buysell-by-osama-mohamed.herokuapp.com) By Flask

[<img src="https://www.djangoproject.com/s/img/logos/django-logo-negative.png" width="200" title="E-Commerce Blueprint" >](https://buysell-by-osama-mohamed.herokuapp.com)
[<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" width="150" title="E-Commerce Blueprint" >](https://buysell-by-osama-mohamed.herokuapp.com)


## For live preview :
> [E-Commerce Blueprint](https://buysell-by-osama-mohamed.herokuapp.com)


## E-commerce website containes:
* User register 
* User login
* User logout 
* Change password
* Reset password
* User delete account
* Order products
* Edit order quantity
* Delete order
* Add review to products
* Calculate avg to every product
* Contact us message



## Usage :
### Run project by :

``` python

# change database connection information in settings.py DATABASES default values with your info then run 

1. export FLASK_APP=buy_sell.py

2. python -m flask run

# OR you can use

1. export FLASK_APP=buy_sell.py

2. flask run

```

That's it.

## Done :

Now the project is running at `http://localhost:5000` and your routes is:


| Route                                                      | HTTP Method 	   | Description                           	      |
|:-----------------------------------------------------------|:----------------|:---------------------------------------------|
| {host}       	                                             | GET       	     | Home page                                    |
| {host}/contact_us                                          | POST     	     | Contact us message                           |
| {host}/products_price_range                                | POST     	     | Search products by price range               |
| {host}/products/{id}                                       | POST     	     | All products page                            |
| {host}/user_forget_password                                | GET      	     | Forget password page                         |
| {host}/user_forget_password_email                          | POST     	     | Send reset password e-mail                   |
| {host}//user_reset_password/{id}/{random_for_reset}        | POST     	     | Enter new password                           |
| {host}/user_register                                       | POST     	     | User register                                |
| {host}/user_login                                          | POST     	     | User login                                   |
| {host}/user_logout                                         | GET     	       | User logout                                  |
| {host}/user_account                                        | GET     	       | User profile                                 |
| {host}/user_profile_picture                                | POST     	     | Change user profile image                    |
| {host}/user_change_password/                               | POST     	     | User change password                         |
| {host}/delete_user_account                                 | POST    	       | Delete user account                          |
| {host}/add_product_to_cart/{id}                            | POST     	     | Add order to cart                            |
| {host}/add_product_to_cart_from_slider/{id}                | POST     	     | Add order to cart from slider                |
| {host}/increase_cart_product_quantity/{id}                 | POST     	     | Increase order quantity                      |
| {host}/edit_cart_product_quantity/{id}                     | POST     	     | Enter order quantity                         |
| {host}/decrease_cart_product_quantity/{id}                 | POST     	     | Decrease order quantity                      |
| {host}/delete_product_from_cart/{id}                       | POST     	     | Delete order                                 |
| {host}/add_to_cart                                         | POST   	       | Cart                                         |
| {host}/buy                                                 | POST     	     | Buy orders                                   |
| {host}/product_review/{id}                                 | POST     	     | Add product review                           |
| {host}/slider_product_review/{id}                          | POST     	     | Add slider product review                    |
| {host}/preview_production/{id}                             | GET     	       | Product detail                               |
| {host}/preview_production_slider/{id}                      | GET     	       | Slider Product detail                        |
| {host}/categories/{category}                               | GET     	       | Search products by category                  |
| {host}/user_search                                         | POST     	     | Search in products name                      |






| Admin Route                                                         | HTTP Method 	   | Description                 	      |
|:--------------------------------------------------------------------|:-----------------|:-----------------------------------|
| {host}/admin/admin_forget_password                                  | GET       	     | Reset password for admin           |
| {host}/admin/admin_forget_password_email                            | POST       	     | Send reset password e-mail         |
| {host}/admin/admin_reset_password/{id}/{random_for_reset}           | POST       	     | Enter new password                 |
| {host}/admin/login                                                  | POST       	     | Admin login                        |
| {host}/admin/logout                                                 | GET       	     | Admin logout                       |
| {host}/admin/admin_change_password/                                 | POST       	     | Admin change password              |
| {host}/admin/delete_admin_account                                   | POST       	     | Delete admin account               |
| {host}/admin/                                                       | POST       	     | Admin Dashboard                    |
| {host}/admin/upload_picture                                         | POST       	     | Admin change image                 |
| {host}/admin/admin_profile_picture                                  | POST       	     | Admin change profile image         |
| {host}/admin/add_product                                            | POST       	     | Admin add product                  |
| {host}/admin/edit_product/{id}                                      | POST       	     | Admin edit product                 |
| {host}/admin/delete_product/{id}                                    | POST       	     | Admin delete product               |
| {host}/admin/delete_all_products                                    | POST       	     | Admin delete all products          |
| {host}/admin/delete_review_products/{id}/{id2}                      | POST       	     | Admin delete product review        |
| {host}/admin/delete_all_review_products                             | POST       	     | Admin delete all product reviews   |
| {host}/admin/add_product_slider                                     | POST       	     | Admin add slider product           |
| {host}/admin/edit_product_slider/{id}                               | POST       	     | Admin edit slider product          |
| {host}/admin/delete_product_slider/{id}                             | POST       	     | Admin delete slider product        |
| {host}/admin/delete_all_slider_products                             | POST       	     | Admin delete all slider products   |
| {host}/admin/delete_review_slider_product/{id}/{id2}                | POST       	     | Admin delete slider product review |
| {host}/admin/delete_all_slider_products_reviews                     | POST       	     | Admin delete all slider product reviews|
| {host}/admin/add_user                                               | POST       	     | Admin create user account          |
| {host}/admin/delete_user/{id}                                       | POST       	     | Admin delete user account          |
| {host}/admin/add_category                                           | POST       	     | Admin add category                 |
| {host}/admin/edit_category/{current_category}                       | POST       	     | Admin edit category                |
| {host}/admin/delete_category/{category}                             | POST       	     | Admin delete category              |
| {host}/admin/delete_all_categories                                  | POST       	     | Admin delete all catigories        |
| {host}/admin/delete_all_users                                       | POST       	     | Admin delete all users accounts    |
| {host}/admin/delete_all_accounts                                    | POST             | Admin delete all accounts          |
| {host}/admin/accept_orders/{id}                                     | POST       	     | Admin accept order                 |
| {host}/admin/accept_all_orders                                      | POST       	     | Admin accept all orders            |
| {host}/admin/reject_orders/{id}                                     | POST       	     | Admin reject order                 |
| {host}/admin/reject_all_orders                                      | POST       	     | Admin reject all orders            |
| {host}/admin/search                                                 | POST       	     | Admin search in products name      |
| {host}/admin/slider_products_table                                  | GET       	     | Admin slider products table        |
| {host}/admin/products_table                                         | GET       	     | Admin products table               |
| {host}/admin/categories_table                                       | GET       	     | Admin categories table             |
| {host}/admin/categories/{category}                                  | POST       	     | Admin search products by category  |
| {host}/admin/users_table                                            | GET       	     | Admin users table                  |
| {host}/admin/orders_table                                           | GET       	     | Admin orders table                 |
| {host}/admin/review_products                                        | GET       	     | Admin products reviews table       |
| {host}/admin/review_slider_products                                 | GET       	     | Admin slider products reviews table|
| {host}/admin/product/{id}                                           | GET       	     | Admin preview product              |
| {host}/admin/slider/{id}                                            | GET       	     | Admin preview slider product       |
| {host}/admin/messages_table                                         | GET       	     | Admin contact us messages table    |
| {host}/admin/message/{id}                                           | GET       	     | Admin preview contact us message   |
| {host}/admin/delete_message/{id}                                    | POST       	     | Admin delete contact us message    |
| {host}/admin/delete_all_messages                                    | POST       	     | Admin delete all contact us message|
| {host}/admin/delete_all_seen_messages                               | POST       	     | Admin delete all seen messages     |
| {host}/admin/delete_all_not_seen_messages                           | POST       	     | Admin delete all not seen messages |
| {host}/admin/show_orders/{username}                                 | GET       	     | Admin show all orders by user table|
| {host}/admin/accept_order_user/{username}/{id}                      | GET       	     | Admin accept order by user         |
| {host}/admin/accept_all_orders_user/{username}                      | GET       	     | Admin accept all orders by user    |
| {host}/admin/reject_order_user/{username}/{id}                      | GET       	     | Admin reject order by user         |
| {host}/admin/reject_all_orders_user/{username}                      | GET       	     | Admin reject all orders by user    |




For detailed explanation on how project work, read the [Flask Docs](http://flask.pocoo.org/docs/0.12/) and [MySQLDB Docs](https://dev.mysql.com/doc/)

## Developer
This project made by [Osama Mohamed](https://www.facebook.com/osama.mohamed.ms)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
