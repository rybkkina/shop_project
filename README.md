# Shop website
This is a shop website where users can easily find products they want, add them to cart, change quantity of the products they chose, make orders, but these actions are available only for authorized users (when a user wants to add a product to cart, he is being redirected to the registration page and then to the login page). The following images represent registration page, login page, the main page of the site, and the cart:
![Home page](/home/masha/PycharmProjects/shop/myshop/README_photos/Знімок екрана з 2024-01-31 22-31-45.png)
Home page
![](/home/masha/PycharmProjects/shop/myshop/README_photos/Знімок екрана з 2024-01-31 22-35-33.png)
Login form
![Checkout](/home/masha/PycharmProjects/shop/myshop/README_photos/Знімок екрана з 2024-01-31 22-42-54.png)
Checkout
![Payment](/home/masha/PycharmProjects/shop/myshop/README_photos/Знімок екрана з 2024-01-31 22-45-39.png)
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