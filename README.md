# Accounting-system-of-sold-goods

The system can include several stores. 

The system can have several warehouses with goods (belonging to a category, a product can only belong to one category, the same product can be in different warehouses). Any store has its own assortment and can sell goods from different warehouses (if store 1 sells item A from warehouse 1, then store 2 cannot sell item A from warehouse 1). 

User registration and authorization. An authorized user can view: stores and their goods, warehouses with available goods, a list of goods sold with an indication of its category, the store that sold it and the warehouse from which it was shipped.

## Project setup

```
git clone https://github.com/VasiliKavaleu/Accounting-system-of-sold-goods.git
```

### Install requirements
```
pip3 install -r requirements.txt
```

### Apply migrations 
```
python3 manage.py migrate 
```

### Run tests
```
python3 manage.py test && flake8
```

### Run 
```
python3 manage.py runserver 
```

###### Endpoints:

Create a new user - POST - */api/user/create/*

Create a new auth token for the user - POST - */api/user/token/*

Manage the authenticated user GET, PUT, PATCH - */api/user/me/*


Get all categories and create one - GET, POST - */api/category/*

Get a category, update and delete - GET, PUT, DELETE  - */api/category/<id>*


Get all products and create one - GET, POST - */api/products/*

Get a product, update and delete - GET, PUT, DELETE - */api/product/<id>/*


Get all storages and create one - GET, POST - */api/storages/*

Update and delete storage - PUT, DELETE - */api/storages/<id>/*


Displaying a list of products in accordance with the availability in storages and belonging to the assortment of stores - GET - */api/products_availability/*

Adding goods to storages and forming an assortment of stores - POST -  */api/products_availability/*


Getting a list of sold items - GET  - */api/sold_product/*

Adding an item to the list of sold items (in this case, removing a storage from the list of available storages for ordering goods) - POST - */api/sold_product/*


Getting a list of products sold by category (id) - GET  - */api/sold_product_by_category/*

Getting a list of goods sold by storage (id) - GET  - */api/sold_product_by_storage/*

Getting a list of products sold by store (id) - GET  - */api/sold_product_by_shop/*

Getting a list of products sold by product (id) - GET - */api/sold_product_by_product/*


