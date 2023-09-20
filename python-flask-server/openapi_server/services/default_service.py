from flask import abort, request
from openapi_server.config_test import db
from openapi_server.models.default import Default, Default_schema, Defaults_schema
from openapi_server.services.pagination_sorting import pagination_sorting
import logging

logging.basicConfig(level=logging.INFO)

class DefaultService:

    def get_default_list():
        """
        This function retrieves paginated and sorted list of all defaults from the database.
      
        It returns a list of defaults in JSON format with a HTTP status code of 200.
        Retrieves a list of all defaults in the database.

        :return: The list of defaults.
        :rtype: list of dicts
        """
        logging.info(f"Getting defaults list")
        defaults = pagination_sorting(Default)
        if not defaults:
            logging.warn("No default found!")
            abort(404, "No default found")
        return Defaults_schema.dump(defaults)

    def get_default(id):
        """
        Retrieves a default by ID from the database.
        
        :param id: integer ID of the default to retrieve
        :type id: int
        :return: The default object
        :rtype: dict
        """
        logging.info(f"Getting default with ID: {id}")

        default = Default.query.filter(Default.id == id).one_or_none()
        if default is not None:
            return Default_schema.dump(default)
        else:
            if id < 1:
                logging.error(f"Invalid ID: {id}.")
            else : 
                logging.error(f"Default with ID: {id} does not exist")
            abort(404, f"Default with ID: {id} does not exist")

    def add_default(default):
        """
        Adds a new default to the database.
        The default object must contain an 'id' field, which must not already exist in the database.

        :param default: The default object to add to the database
        :type default: dict
        :return: The newly added default object
        :rtype: dict
        :raises: 400 error if a default with the same id already exists
        """
        id = default.get("id")
        logging.info(f"Adding default with ID: {id}")
        
        existing_default = Default.query.filter(Default.id == id).one_or_none()

        if existing_default is None:
            new_default = Default_schema.load(default, session=db.session)
            db.session.add(new_default)
            db.session.commit()
            logging.info(f"Successfully added default with ID : {id}")
            return Default_schema.dump(new_default)
        else:
            logging.error(f"Default with ID: {id} already exists")
            abort(400, f"Default with ID: {id} already exists")

    def update_default(default):
        """
        Update an existing default in the database with a specified id.
        
        :param id: integer ID of the default to update.
        :type id: int
        :return: The updated default object.
        :rtype: dict
        :raises: 404 error if the default is not found
        """
        id = default.get("id")
        logging.info(f"Updating default with ID: {id}")
        existing_default = Default.query.filter(Default.id == id).one_or_none()

        if existing_default:
            update_default = Default_schema.load(default, session=db.session)
            existing_default.id = update_default.id
            db.session.merge(existing_default)
            db.session.commit()
            logging.info(f"Successfully updated default with ID : {id}")
            return Default_schema.dump(existing_default)
        else:
            logging.error(f"Default with ID: {id} not found")
            abort(404, f"Default with ID: {id} not found")

    def delete_default(id):
        """
        Delete the default with the specified id.

        :param id: integer id of the default to delete
        :type id: int
        :return: success message
        :raises: 400 error if the default is not found
        """
        logging.info(f"Started processing of delete operation for ID: {id}")
        existing_default = Default.query.filter(Default.id == id).one_or_none()

        if existing_default:
            db.session.delete(existing_default)
            db.session.commit()
            logging.info(f"Successfully completed the deletion operation for ID : {id}")
            return f"Default with ID: {id} successfully deleted"
        else: 
            logging.error(f"Default with ID: {id} not present!")
            abort(400, f"Default with ID: {id} not found")

