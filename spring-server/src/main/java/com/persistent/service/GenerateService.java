/**
 * Service class for handling CRUD operations on Generate resource.
 */
package com.persistent.service;
import java.lang.reflect.Field;
import java.util.ArrayList;

import java.util.List;
import java.util.Optional;
import com.persistent.model.GenerateDto;

import javax.persistence.Query;
import javax.persistence.criteria.CriteriaBuilder;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import lombok.extern.log4j.Log4j2;
import com.persistent.exception.InvalidIdException;
import com.persistent.exception.ResourceNotFoundException;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import com.persistent.util.Constants;


@Service
@Log4j2
public class GenerateService {
    @Autowired
    private GenerateRepository generateRepository;

    @PersistenceContext
    private EntityManager entityManager;

    /**
     * This method is used to retrieve the generate list from the database.
     * @return On successful operation the generate list.
     *         or Warning message as "No generate found!".
     * @param pageNumber Page number to be displayed.
     * @param pageSize Number of records to be displayed per page.
     * @param sortBy Column name to sort the list by.
     * @param sortDir Sort direction i.e. ASC or DESC.
     */
    public List<GenerateDto> getGenerateList(String queryString, Integer pageNumber, Integer pageSize, String sortBy, String sortDir) {
        
        log.info("Getting generate list");
        String message = null;
        Sort sort = null;
        
        // Checking and correcting the input values
        pageNumber = PaginationAndSorting.checkPageNumber(pageNumber);
        pageSize = PaginationAndSorting.checkPageSize(pageSize);
        sortBy = PaginationAndSorting.checkColumnName(GenerateDto.class,sortBy);
        sortDir = PaginationAndSorting.checkSortDirection(sortDir);
        sort = PaginationAndSorting.setSortObject(sortBy, sortDir);
       
        // Creating the page request object.
        // Page number starts from 0.
        // So, we are decrementing the page number by 1.
        // For example, if page number is 1 then it will be 0.
        Pageable pageable = PageRequest.of(--pageNumber, pageSize, sort);

        List<GenerateDto> generateList = null;
        CriteriaBuilder criteriaBuilder = entityManager.getCriteriaBuilder();
        
        generateList = Searching.generatePredicateList(GenerateDto.class,queryString, entityManager,criteriaBuilder, sortBy, sortDir, pageable);
       
        if (generateList == null) {
            message = "No generate found!";
            log.warn(message);
        }
        return generateList;
    }

    /**
     * This method is used to retrieve a generate with the specified ID.
     * @param id The ID of the generate to retrieve.
     * @return On successful operation the generate with specified ID.
     * @throws InvalidIdException If incorrect ID is provided.
     * @throws ResourceNotFoundException If the generate object is not found. 
     */
    public GenerateDto getGenerate(Long id) {
        log.info("Getting generate with id {}", id);

        if(id < 1) {
            String message = "Invalid id : "+ id;
            log.error(message);
            throw new InvalidIdException(message);
        }

        Optional<GenerateDto> generate = generateRepository.findById(id);
        
        if(generate.isPresent()) {
            return generate.get();
        } else {
            String message = "Generate with id " + id + " is not present!";
            log.error(message);
            throw new ResourceNotFoundException(message);
        }
    }

    /**
     * This method adds a new generate to the database with given information.
     * @param generate The generate object that needs to be added.
     * @return On successful operation the added generate is returned.
     */
    public GenerateDto addGenerate(GenerateDto generate ) {
        log.info("Adding generate");
        return generateRepository.save(generate);
    }

    /**
     * This method deletes the generate to the database with given information.
     * @param id The id of generate that needs to be deleted.
     * @return On successful operation the deleted generate is returned.
     * @throws InvalidIdException If incorrect ID is provided.
     * @throws ResourceNotFoundException If the generate object is not found.
     */
    public GenerateDto deleteGenerate(Long id) {
        log.info("Started processing of delete operation");

        if(id < 1) {
            String message = "Invalid id : "+id;
            log.error(message);
            throw new InvalidIdException(message);
        }

        Optional<GenerateDto> generate = generateRepository.findById(id);
        
        if(generate.isPresent()) {
            generateRepository.deleteById(id);
            log.info("Successfully completed the deletion operation for ID : {}",id);
            return generate.get();
        } else {
            String message = "Generate with id "+id+" is not present!";
            log.error(message);
            throw new ResourceNotFoundException(message);
        }
    }

    /**
     * This method updates an existing generate in the database.
     * @param generate The generate object that needs to be updated.
     * @return On successful operation the updated generate object is returned.
     * @throws ResourceNotFoundException If the generate object is not found.
     */
    public GenerateDto updateGenerate(GenerateDto generate ) {
        log.info("Updating generate with id {}",generate.getId());
        long id = generate.getId();

        if(id < 1) {
            String message = "Invalid id : "+id;
            log.error(message);
            throw new InvalidIdException(message);
        }

        Optional<GenerateDto> generateToBeUpdated = generateRepository.findById(id);
        
        if(generateToBeUpdated.isPresent()) {
            return generateRepository.save(generate);
        } else {
            String message = "Generate with id "+id+" is not present!";
            log.error(message);
            throw new ResourceNotFoundException(message);
        }
    }

}
