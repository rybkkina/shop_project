# Shop website
This is a shop website where users can easily find products they want, add them to cart, change quantity of the products they chose, make orders, but these actions are available only for authorized users (when a user wants to add a product to cart, he is being redirected to the registration page and then to the login page). The following images represent registration page, login page, the main page of the site, and the cart:
![Home page](https://github.com/rybkkina/shop_project/blob/main/README_photos/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%B7%202024-01-31%2022-31-45.png)
Home page
![](https://github.com/rybkkina/shop_project/blob/main/README_photos/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%B7%202024-01-31%2022-35-33.png)
Login form
![Checkout](https://github.com/rybkkina/shop_project/blob/main/README_photos/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%B7%202024-01-31%2022-42-54.png)
Checkout
![Payment](https://github.com/rybkkina/shop_project/blob/main/README_photos/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%B7%202024-01-31%2022-45-39.png)
Payment process
#### Technologies used: 
* Django Framework 

* Django REST Framework

* SQLite 

* Celery 

* RabbitMQ 

* Stripe payment system 

The following code in [tasks.py](https://github.com/rybkkina/shop_project/blob/main/orders/tasks.py) has task which sends an email after successfully creating an order. I use RabbitMQ broker as a broker and resulting backend for Celery.
Рayment application includes all the logic related to payments and integration with Stripe. Stripe Checkout integration consists of a checkout page hosted by Stripe that allows users to enter payment details, usually credit cards, and collects the payment. If the payment is successful, Stripe redirects the client to the success page. If the payment is canceled by the client or the payment fails, it redirects the client to the cancel page. 
The store also has a coupon system, which allows users to apply coupons and receive discounts, which are deducted from the total amount of the order.
#### Django REST Framework: 

* Wrote serializers, api_views, using viewsets , mixins and generic views. 

* Implemented token authentication 

* Create custom permissions class  which allows only administrators to change orders.