ERP Inventory & Order Management

(Backend - Django)
Develop a basic Inventory & Order Management API for an ERP system.
Requirements:
1.	Create a Django REST Framework API for: 
o	Managing inventory (Product, Stock, Supplier models).
o	Creating orders (Order, OrderItems models).
o	Updating stock when an order is placed.
2.	Design the MySQL/PostgreSQL schema for the inventory and orders.
3.	Implement API endpoints: 
o	POST /products - Add a new product.
o	GET /products - List all products.
o	POST /orders - Place an order (updates stock).
o	GET /orders - List all orders.
4.	Implement basic validation & exception handling.
________________________________________

(Frontend - Vue.js)
Build an Inventory & Order Management UI.
Requirements:
1.	Product List Page: 
o	Displays products with stock availability.
o	Add/Edit/Delete products (only Admins).
2.	Order Page: 
o	Place a new order.
o	Show order history.
3.	Use Vuex/Pinia (Vue.js) for state management.
4.	Ensure UI follows a clean dashboard layout with proper role-based access.
