from flask import abort, request
from openapi_server.config_test import db
from openapi_server.models.product import Product, Product_schema, Products_schema
from openapi_server.services.pagination_sorting import pagination_sorting
import logging

logging.basicConfig(level=logging.INFO)

class ProductService:

    def get_product_list():
        """
        This function retrieves paginated and sorted list of all products from the database.
      
        It returns a list of products in JSON format with a HTTP status code of 200.
        Retrieves a list of all products in the database.

        :return: The list of products.
        :rtype: list of dicts
        """
        logging.info(f"Getting products list")
        products = pagination_sorting(Product)
        if not products:
            logging.warn("No product found!")
            abort(404, "No product found")
        return Products_schema.dump(products)

    def get_product(id):
        """
        Retrieves a product by ID from the database.
        
        :param id: integer ID of the product to retrieve
        :type id: int
        :return: The product object
        :rtype: dict
        """
        logging.info(f"Getting product with ID: {id}")

        product = Product.query.filter(Product.id == id).one_or_none()
        if product is not None:
            return Product_schema.dump(product)
        else:
            if id < 1:
                logging.error(f"Invalid ID: {id}.")
            else : 
                logging.error(f"Product with ID: {id} does not exist")
            abort(404, f"Product with ID: {id} does not exist")

    def add_product(product):
        """
        Adds a new product to the database.
        The product object must contain an 'id' field, which must not already exist in the database.

        :param product: The product object to add to the database
        :type product: dict
        :return: The newly added product object
        :rtype: dict
        :raises: 400 error if a product with the same id already exists
        """
        id = product.get("id")
        logging.info(f"Adding product with ID: {id}")
        
        existing_product = Product.query.filter(Product.id == id).one_or_none()

        if existing_product is None:
            new_product = Product_schema.load(product, session=db.session)
            db.session.add(new_product)
            db.session.commit()
            logging.info(f"Successfully added product with ID : {id}")
            return Product_schema.dump(new_product)
        else:
            logging.error(f"Product with ID: {id} already exists")
            abort(400, f"Product with ID: {id} already exists")

    def update_product(product):
        """
        Update an existing product in the database with a specified id.
        
        :param id: integer ID of the product to update.
        :type id: int
        :return: The updated product object.
        :rtype: dict
        :raises: 404 error if the product is not found
        """
        id = product.get("id")
        logging.info(f"Updating product with ID: {id}")
        existing_product = Product.query.filter(Product.id == id).one_or_none()

        if existing_product:
            update_product = Product_schema.load(product, session=db.session)
            existing_product.id = update_product.id
            db.session.merge(existing_product)
            db.session.commit()
            logging.info(f"Successfully updated product with ID : {id}")
            return Product_schema.dump(existing_product)
        else:
            logging.error(f"Product with ID: {id} not found")
            abort(404, f"Product with ID: {id} not found")

    def delete_product(id):
        """
        Delete the product with the specified id.

        :param id: integer id of the product to delete
        :type id: int
        :return: success message
        :raises: 400 error if the product is not found
        """
        logging.info(f"Started processing of delete operation for ID: {id}")
        existing_product = Product.query.filter(Product.id == id).one_or_none()

        if existing_product:
            db.session.delete(existing_product)
            db.session.commit()
            logging.info(f"Successfully completed the deletion operation for ID : {id}")
            return f"Product with ID: {id} successfully deleted"
        else: 
            logging.error(f"Product with ID: {id} not present!")
            abort(400, f"Product with ID: {id} not found")

