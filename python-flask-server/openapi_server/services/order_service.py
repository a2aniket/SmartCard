from flask import abort, request
from openapi_server.config_test import db
from openapi_server.models.order import Order, Order_schema, Orders_schema
from openapi_server.services.pagination_sorting import pagination_sorting
import logging

logging.basicConfig(level=logging.INFO)

class OrderService:

    def get_order_list():
        """
        This function retrieves paginated and sorted list of all orders from the database.
      
        It returns a list of orders in JSON format with a HTTP status code of 200.
        Retrieves a list of all orders in the database.

        :return: The list of orders.
        :rtype: list of dicts
        """
        logging.info(f"Getting orders list")
        orders = pagination_sorting(Order)
        if not orders:
            logging.warn("No order found!")
            abort(404, "No order found")
        return Orders_schema.dump(orders)

    def get_order(id):
        """
        Retrieves a order by ID from the database.
        
        :param id: integer ID of the order to retrieve
        :type id: int
        :return: The order object
        :rtype: dict
        """
        logging.info(f"Getting order with ID: {id}")

        order = Order.query.filter(Order.id == id).one_or_none()
        if order is not None:
            return Order_schema.dump(order)
        else:
            if id < 1:
                logging.error(f"Invalid ID: {id}.")
            else : 
                logging.error(f"Order with ID: {id} does not exist")
            abort(404, f"Order with ID: {id} does not exist")

    def add_order(order):
        """
        Adds a new order to the database.
        The order object must contain an 'id' field, which must not already exist in the database.

        :param order: The order object to add to the database
        :type order: dict
        :return: The newly added order object
        :rtype: dict
        :raises: 400 error if a order with the same id already exists
        """
        id = order.get("id")
        logging.info(f"Adding order with ID: {id}")
        
        existing_order = Order.query.filter(Order.id == id).one_or_none()

        if existing_order is None:
            new_order = Order_schema.load(order, session=db.session)
            db.session.add(new_order)
            db.session.commit()
            logging.info(f"Successfully added order with ID : {id}")
            return Order_schema.dump(new_order)
        else:
            logging.error(f"Order with ID: {id} already exists")
            abort(400, f"Order with ID: {id} already exists")

    def update_order(order):
        """
        Update an existing order in the database with a specified id.
        
        :param id: integer ID of the order to update.
        :type id: int
        :return: The updated order object.
        :rtype: dict
        :raises: 404 error if the order is not found
        """
        id = order.get("id")
        logging.info(f"Updating order with ID: {id}")
        existing_order = Order.query.filter(Order.id == id).one_or_none()

        if existing_order:
            update_order = Order_schema.load(order, session=db.session)
            existing_order.id = update_order.id
            db.session.merge(existing_order)
            db.session.commit()
            logging.info(f"Successfully updated order with ID : {id}")
            return Order_schema.dump(existing_order)
        else:
            logging.error(f"Order with ID: {id} not found")
            abort(404, f"Order with ID: {id} not found")

    def delete_order(id):
        """
        Delete the order with the specified id.

        :param id: integer id of the order to delete
        :type id: int
        :return: success message
        :raises: 400 error if the order is not found
        """
        logging.info(f"Started processing of delete operation for ID: {id}")
        existing_order = Order.query.filter(Order.id == id).one_or_none()

        if existing_order:
            db.session.delete(existing_order)
            db.session.commit()
            logging.info(f"Successfully completed the deletion operation for ID : {id}")
            return f"Order with ID: {id} successfully deleted"
        else: 
            logging.error(f"Order with ID: {id} not present!")
            abort(400, f"Order with ID: {id} not found")

