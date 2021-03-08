# Accounting-system-of-sold-goods

The system can include several stores. 

The system can have several warehouses with goods (belonging to a category, a product can only belong to one category, the same product can be in different warehouses). Any store has its own assortment and can sell goods from different warehouses (if store 1 sells item A from warehouse 1, then store 2 cannot sell item A from warehouse 1). 

User registration and authorization. An authorized user can view: stores and their goods, warehouses with available goods, a list of goods sold with an indication of its category, the store that sold it and the warehouse from which it was shipped.

## Project setup
```
git clone https://github.com/VasiliKavaleu/Accounting-system-of-sold-goods.git
```

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
