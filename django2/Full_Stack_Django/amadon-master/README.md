## Welcome to Amadon
There are some serious issues with this code! Follow the instructions below to understand what those issues are, and then figure out how to resolve them.

Instructions
------------

1. Clone this repository and peruse the code
2. Run makemigrations and migrate to create the necessary database tables
3. Seed the database with a few products (i.e. go into the Django shell and create a few products)
4. Run the server and make a purchase
5. Add some basic styling (use Bootstrap or another CSS framework)
6. Calculate and display the following values on the checkout.html page:
    - the total amount charged for the most recent order
    - the total quantity of ordered items across all orders combined
    - the total amount charged across all orders combined
7. After making an order, hit the refresh button while on the checkout page and say yes/confirm if prompted. What do you notice?
8. Fix this issue so that users don't inadvertently make another order by mistake!
9. Go back to the order form and use your browser's inspect element tool. Change the price of an item and then place an order. What do you notice?
10. Fix this issue so that users don't get to set the price of their items!
