from flask import abort, request
from openapi_server.config_test import db
from openapi_server.models.pet import Pet, Pet_schema, Pets_schema
from openapi_server.services.pagination_sorting import pagination_sorting
import logging

logging.basicConfig(level=logging.INFO)

class PetService:

    def get_pet_list():
        """
        This function retrieves paginated and sorted list of all pets from the database.
      
        It returns a list of pets in JSON format with a HTTP status code of 200.
        Retrieves a list of all pets in the database.

        :return: The list of pets.
        :rtype: list of dicts
        """
        logging.info(f"Getting pets list")
        pets = pagination_sorting(Pet)
        if not pets:
            logging.warn("No pet found!")
            abort(404, "No pet found")
        return Pets_schema.dump(pets)

    def get_pet(id):
        """
        Retrieves a pet by ID from the database.
        
        :param id: integer ID of the pet to retrieve
        :type id: int
        :return: The pet object
        :rtype: dict
        """
        logging.info(f"Getting pet with ID: {id}")

        pet = Pet.query.filter(Pet.id == id).one_or_none()
        if pet is not None:
            return Pet_schema.dump(pet)
        else:
            if id < 1:
                logging.error(f"Invalid ID: {id}.")
            else : 
                logging.error(f"Pet with ID: {id} does not exist")
            abort(404, f"Pet with ID: {id} does not exist")

    def add_pet(pet):
        """
        Adds a new pet to the database.
        The pet object must contain an 'id' field, which must not already exist in the database.

        :param pet: The pet object to add to the database
        :type pet: dict
        :return: The newly added pet object
        :rtype: dict
        :raises: 400 error if a pet with the same id already exists
        """
        id = pet.get("id")
        logging.info(f"Adding pet with ID: {id}")
        
        existing_pet = Pet.query.filter(Pet.id == id).one_or_none()

        if existing_pet is None:
            new_pet = Pet_schema.load(pet, session=db.session)
            db.session.add(new_pet)
            db.session.commit()
            logging.info(f"Successfully added pet with ID : {id}")
            return Pet_schema.dump(new_pet)
        else:
            logging.error(f"Pet with ID: {id} already exists")
            abort(400, f"Pet with ID: {id} already exists")

    def update_pet(pet):
        """
        Update an existing pet in the database with a specified id.
        
        :param id: integer ID of the pet to update.
        :type id: int
        :return: The updated pet object.
        :rtype: dict
        :raises: 404 error if the pet is not found
        """
        id = pet.get("id")
        logging.info(f"Updating pet with ID: {id}")
        existing_pet = Pet.query.filter(Pet.id == id).one_or_none()

        if existing_pet:
            update_pet = Pet_schema.load(pet, session=db.session)
            existing_pet.id = update_pet.id
            db.session.merge(existing_pet)
            db.session.commit()
            logging.info(f"Successfully updated pet with ID : {id}")
            return Pet_schema.dump(existing_pet)
        else:
            logging.error(f"Pet with ID: {id} not found")
            abort(404, f"Pet with ID: {id} not found")

    def delete_pet(id):
        """
        Delete the pet with the specified id.

        :param id: integer id of the pet to delete
        :type id: int
        :return: success message
        :raises: 400 error if the pet is not found
        """
        logging.info(f"Started processing of delete operation for ID: {id}")
        existing_pet = Pet.query.filter(Pet.id == id).one_or_none()

        if existing_pet:
            db.session.delete(existing_pet)
            db.session.commit()
            logging.info(f"Successfully completed the deletion operation for ID : {id}")
            return f"Pet with ID: {id} successfully deleted"
        else: 
            logging.error(f"Pet with ID: {id} not present!")
            abort(400, f"Pet with ID: {id} not found")

