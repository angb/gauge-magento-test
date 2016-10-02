Magento Order
=====================

Create a new customer
--------------------------------------

* Create customer account for "Ann" "Smith" with "ann@test.com"

Login from App
--------------------------------------

* Login from app as user "ann@test.com"

Add Products to Cart
--------------------------------------

* Create a cart from app as user "ann@test.com"
* Add item with sku "24-WB04" to cart from app as user "ann@test.com"

Payment and Order
--------------------------------------

* Process and submit order for cart from app as user "ann@test.com" with firstname="Ann" lastname="Smith" street="1 Street" city="Brisbane" region="QLD" postcode="1234" country="AU" telephone="55-555-55"

Verify Order as Admin
--------------------------------------

*  Login as Admin
*  Check order exists for user "ann@test.com"
*  Verify order contains item with sku "24-WB04"

Logout and Cleanup
--------------------------------------

* User "ann@test.com" closes browser
* User "admin" closes browser