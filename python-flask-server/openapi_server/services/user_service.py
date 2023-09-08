from flask import abort, request
from openapi_server.config_test import db
from openapi_server.models.user import User, User_schema, Users_schema
from openapi_server.services.pagination_sorting import pagination_sorting
import logging

logging.basicConfig(level=logging.INFO)

class UserService:

    def get_user_list():
        """
        This function retrieves paginated and sorted list of all users from the database.
      
        It returns a list of users in JSON format with a HTTP status code of 200.
        Retrieves a list of all users in the database.

        :return: The list of users.
        :rtype: list of dicts
        """
        logging.info(f"Getting users list")
        users = pagination_sorting(User)
        if not users:
            logging.warn("No user found!")
            abort(404, "No user found")
        return Users_schema.dump(users)

    def get_user(id):
        """
        Retrieves a user by ID from the database.
        
        :param id: integer ID of the user to retrieve
        :type id: int
        :return: The user object
        :rtype: dict
        """
        logging.info(f"Getting user with ID: {id}")

        user = User.query.filter(User.id == id).one_or_none()
        if user is not None:
            return User_schema.dump(user)
        else:
            if id < 1:
                logging.error(f"Invalid ID: {id}.")
            else : 
                logging.error(f"User with ID: {id} does not exist")
            abort(404, f"User with ID: {id} does not exist")

    def add_user(user):
        """
        Adds a new user to the database.
        The user object must contain an 'id' field, which must not already exist in the database.

        :param user: The user object to add to the database
        :type user: dict
        :return: The newly added user object
        :rtype: dict
        :raises: 400 error if a user with the same id already exists
        """
        id = user.get("id")
        logging.info(f"Adding user with ID: {id}")
        
        existing_user = User.query.filter(User.id == id).one_or_none()

        if existing_user is None:
            new_user = User_schema.load(user, session=db.session)
            db.session.add(new_user)
            db.session.commit()
            logging.info(f"Successfully added user with ID : {id}")
            return User_schema.dump(new_user)
        else:
            logging.error(f"User with ID: {id} already exists")
            abort(400, f"User with ID: {id} already exists")

    def update_user(user):
        """
        Update an existing user in the database with a specified id.
        
        :param id: integer ID of the user to update.
        :type id: int
        :return: The updated user object.
        :rtype: dict
        :raises: 404 error if the user is not found
        """
        id = user.get("id")
        logging.info(f"Updating user with ID: {id}")
        existing_user = User.query.filter(User.id == id).one_or_none()

        if existing_user:
            update_user = User_schema.load(user, session=db.session)
            existing_user.id = update_user.id
            db.session.merge(existing_user)
            db.session.commit()
            logging.info(f"Successfully updated user with ID : {id}")
            return User_schema.dump(existing_user)
        else:
            logging.error(f"User with ID: {id} not found")
            abort(404, f"User with ID: {id} not found")

    def delete_user(id):
        """
        Delete the user with the specified id.

        :param id: integer id of the user to delete
        :type id: int
        :return: success message
        :raises: 400 error if the user is not found
        """
        logging.info(f"Started processing of delete operation for ID: {id}")
        existing_user = User.query.filter(User.id == id).one_or_none()

        if existing_user:
            db.session.delete(existing_user)
            db.session.commit()
            logging.info(f"Successfully completed the deletion operation for ID : {id}")
            return f"User with ID: {id} successfully deleted"
        else: 
            logging.error(f"User with ID: {id} not present!")
            abort(400, f"User with ID: {id} not found")

