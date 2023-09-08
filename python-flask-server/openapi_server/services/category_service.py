from flask import abort, request
from openapi_server.config_test import db
from openapi_server.models.category import Category, Category_schema, Categorys_schema
from openapi_server.services.pagination_sorting import pagination_sorting
import logging

logging.basicConfig(level=logging.INFO)

class CategoryService:

    def get_category_list():
        """
        This function retrieves paginated and sorted list of all categorys from the database.
      
        It returns a list of categorys in JSON format with a HTTP status code of 200.
        Retrieves a list of all categorys in the database.

        :return: The list of categorys.
        :rtype: list of dicts
        """
        logging.info(f"Getting categorys list")
        categorys = pagination_sorting(Category)
        if not categorys:
            logging.warn("No category found!")
            abort(404, "No category found")
        return Categorys_schema.dump(categorys)

    def get_category(id):
        """
        Retrieves a category by ID from the database.
        
        :param id: integer ID of the category to retrieve
        :type id: int
        :return: The category object
        :rtype: dict
        """
        logging.info(f"Getting category with ID: {id}")

        category = Category.query.filter(Category.id == id).one_or_none()
        if category is not None:
            return Category_schema.dump(category)
        else:
            if id < 1:
                logging.error(f"Invalid ID: {id}.")
            else : 
                logging.error(f"Category with ID: {id} does not exist")
            abort(404, f"Category with ID: {id} does not exist")

    def add_category(category):
        """
        Adds a new category to the database.
        The category object must contain an 'id' field, which must not already exist in the database.

        :param category: The category object to add to the database
        :type category: dict
        :return: The newly added category object
        :rtype: dict
        :raises: 400 error if a category with the same id already exists
        """
        id = category.get("id")
        logging.info(f"Adding category with ID: {id}")
        
        existing_category = Category.query.filter(Category.id == id).one_or_none()

        if existing_category is None:
            new_category = Category_schema.load(category, session=db.session)
            db.session.add(new_category)
            db.session.commit()
            logging.info(f"Successfully added category with ID : {id}")
            return Category_schema.dump(new_category)
        else:
            logging.error(f"Category with ID: {id} already exists")
            abort(400, f"Category with ID: {id} already exists")

    def update_category(category):
        """
        Update an existing category in the database with a specified id.
        
        :param id: integer ID of the category to update.
        :type id: int
        :return: The updated category object.
        :rtype: dict
        :raises: 404 error if the category is not found
        """
        id = category.get("id")
        logging.info(f"Updating category with ID: {id}")
        existing_category = Category.query.filter(Category.id == id).one_or_none()

        if existing_category:
            update_category = Category_schema.load(category, session=db.session)
            existing_category.id = update_category.id
            db.session.merge(existing_category)
            db.session.commit()
            logging.info(f"Successfully updated category with ID : {id}")
            return Category_schema.dump(existing_category)
        else:
            logging.error(f"Category with ID: {id} not found")
            abort(404, f"Category with ID: {id} not found")

    def delete_category(id):
        """
        Delete the category with the specified id.

        :param id: integer id of the category to delete
        :type id: int
        :return: success message
        :raises: 400 error if the category is not found
        """
        logging.info(f"Started processing of delete operation for ID: {id}")
        existing_category = Category.query.filter(Category.id == id).one_or_none()

        if existing_category:
            db.session.delete(existing_category)
            db.session.commit()
            logging.info(f"Successfully completed the deletion operation for ID : {id}")
            return f"Category with ID: {id} successfully deleted"
        else: 
            logging.error(f"Category with ID: {id} not present!")
            abort(400, f"Category with ID: {id} not found")

