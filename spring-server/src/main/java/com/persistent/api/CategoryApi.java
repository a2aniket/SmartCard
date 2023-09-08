/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech) (6.3.0-SNAPSHOT).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package com.persistent.api;

import com.persistent.model.Category;
import io.swagger.v3.oas.annotations.ExternalDocumentation;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.Parameters;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.context.request.NativeWebRequest;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.Valid;
import javax.validation.constraints.*;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Generated;
import com.persistent.util.Constants;

@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2023-09-08T12:47:52.630647626Z[UTC]")
@Validated
@Tag(name = "category", description = "Operations about category")
public interface CategoryApi {

    default Optional<NativeWebRequest> getRequest() {
        return Optional.empty();
    }

    /**
     * POST /category : Add a new category to the store
     * Add a new category to the store
     *
     * @param category Create a new category in the store (required)
     * @return Successful operation (status code 200)
     *         or Invalid input (status code 405)
     */
    @Operation(
        operationId = "addCategory",
        summary = "Add a new category to the store",
        description = "Add a new category to the store",
        tags = { "category" },
        responses = {
            @ApiResponse(responseCode = "200", description = "Successful operation", content = {
                @Content(mediaType = "application/json", schema = @Schema(implementation = Category.class)),
                @Content(mediaType = "application/xml", schema = @Schema(implementation = Category.class))
            }),
            @ApiResponse(responseCode = "405", description = "Invalid input")
        }
    )
    @RequestMapping(
        method = RequestMethod.POST,
        value = "/category",
        produces = { "application/json", "application/xml" },
        consumes = { "application/json", "application/xml", "application/x-www-form-urlencoded" }
    )
    default ResponseEntity<Category> addCategory(
        @Parameter(name = "Category", description = "Create a new category in the store", required = true) @Valid @RequestBody Category category
    ) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"name\" : \"Dog\", \"id\" : 1 }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/xml"))) {
                    String exampleString = "<category> <id>1</id> <name>Dog</name> </category>";
                    ApiUtil.setExampleResponse(request, "application/xml", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * DELETE /category/{categoryId} : Deletes a category
     * delete a category
     *
     * @param categoryId Category id to delete (required)
     * @return successful operation (status code 200)
     *         or Invalid category value (status code 400)
     */
    @Operation(
        operationId = "deleteCategory",
        summary = "Deletes a category",
        description = "delete a category",
        tags = { "category" },
        responses = {
            @ApiResponse(responseCode = "200", description = "successful operation", content = {
                @Content(mediaType = "application/json", schema = @Schema(implementation = Category.class)),
                @Content(mediaType = "application/xml", schema = @Schema(implementation = Category.class))
            }),
            @ApiResponse(responseCode = "400", description = "Invalid category value")
        }
    )
    @RequestMapping(
        method = RequestMethod.DELETE,
        value = "/category/{categoryId}",
        produces = { "application/json", "application/xml" }
    )
    default ResponseEntity<Category> deleteCategory(
        @Parameter(name = "categoryId", description = "Category id to delete", required = true, in = ParameterIn.PATH) @PathVariable("categoryId") Long categoryId
    ) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"name\" : \"Dog\", \"id\" : 1 }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/xml"))) {
                    String exampleString = "<category> <id>1</id> <name>Dog</name> </category>";
                    ApiUtil.setExampleResponse(request, "application/xml", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * GET /category/{categoryId} : Find category by ID
     * Returns a single category
     *
     * @param categoryId ID of category to return (required)
     * @return successful operation (status code 200)
     *         or Invalid ID supplied (status code 400)
     *         or Category not found (status code 404)
     */
    @Operation(
        operationId = "getCategory",
        summary = "Find category by ID",
        description = "Returns a single category",
        tags = { "category" },
        responses = {
            @ApiResponse(responseCode = "200", description = "successful operation", content = {
                @Content(mediaType = "application/json", schema = @Schema(implementation = Category.class)),
                @Content(mediaType = "application/xml", schema = @Schema(implementation = Category.class))
            }),
            @ApiResponse(responseCode = "400", description = "Invalid ID supplied"),
            @ApiResponse(responseCode = "404", description = "Category not found")
        }
    )
    @RequestMapping(
        method = RequestMethod.GET,
        value = "/category/{categoryId}",
        produces = { "application/json", "application/xml" }
    )
    default ResponseEntity<Category> getCategory(
        @Parameter(name = "categoryId", description = "ID of category to return", required = true, in = ParameterIn.PATH) @PathVariable("categoryId") Long categoryId
    ) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"name\" : \"Dog\", \"id\" : 1 }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/xml"))) {
                    String exampleString = "<category> <id>1</id> <name>Dog</name> </category>";
                    ApiUtil.setExampleResponse(request, "application/xml", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * GET /category : Get list of all categories
     * Returns list of categories
     *
     * @return successful operation (status code 200)
     *         or Invalid ID supplied (status code 400)
     *         or Category not found (status code 404)
     */
    @Operation(
        operationId = "getCategoryList",
        summary = "Get list of all categories",
        description = "Returns list of categories",
        tags = { "category" },
        responses = {
            @ApiResponse(responseCode = "200", description = "successful operation", content = {
                @Content(mediaType = "application/json", array = @ArraySchema(schema = @Schema(implementation = Category.class))),
                @Content(mediaType = "application/xml", array = @ArraySchema(schema = @Schema(implementation = Category.class)))
            }),
            @ApiResponse(responseCode = "400", description = "Invalid ID supplied"),
            @ApiResponse(responseCode = "404", description = "Category not found")
        }
    )
    @RequestMapping(
        method = RequestMethod.GET,
        value = "/category",
        produces = { "application/json", "application/xml" }
    )
    default ResponseEntity<List<Category>> getCategoryList(
        @RequestParam(value = "query_string", defaultValue = Constants.DEFAULT_SEARCH_CRITERIA, required = false) String queryString,
        @RequestParam(value = "pageNumber", defaultValue = Constants.DEFAULT_PAGE_NUMBER, required = false) Integer pageNumber,
        @RequestParam(value = "pageSize", defaultValue = Constants.DEFAULT_PAGE_SIZE, required = false) Integer pageSize,
        @RequestParam(value = "sortBy", defaultValue = Constants.DEFAULT_SORT_BY, required = false) String sortBy,
        @RequestParam(value = "sortDir", defaultValue = Constants.DEFAULT_SORT_DIR, required = false) String sortDir
        
    ) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "[ { \"name\" : \"Dog\", \"id\" : 1 }, { \"name\" : \"Dog\", \"id\" : 1 } ]";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/xml"))) {
                    String exampleString = "<category> <id>1</id> <name>Dog</name> </category>";
                    ApiUtil.setExampleResponse(request, "application/xml", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

    /**
     * PUT /category : Update an existing category
     * Update an existing category by Id
     *
     * @param category Update an existent category in the store (required)
     * @return Successful operation (status code 200)
     *         or Invalid ID supplied (status code 400)
     *         or Category not found (status code 404)
     *         or Validation exception (status code 405)
     */
    @Operation(
        operationId = "updateCategory",
        summary = "Update an existing category",
        description = "Update an existing category by Id",
        tags = { "category" },
        responses = {
            @ApiResponse(responseCode = "200", description = "Successful operation", content = {
                @Content(mediaType = "application/json", schema = @Schema(implementation = Category.class)),
                @Content(mediaType = "application/xml", schema = @Schema(implementation = Category.class))
            }),
            @ApiResponse(responseCode = "400", description = "Invalid ID supplied"),
            @ApiResponse(responseCode = "404", description = "Category not found"),
            @ApiResponse(responseCode = "405", description = "Validation exception")
        }
    )
    @RequestMapping(
        method = RequestMethod.PUT,
        value = "/category",
        produces = { "application/json", "application/xml" },
        consumes = { "application/json", "application/xml", "application/x-www-form-urlencoded" }
    )
    default ResponseEntity<Category> updateCategory(
        @Parameter(name = "Category", description = "Update an existent category in the store", required = true) @Valid @RequestBody Category category
    ) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"name\" : \"Dog\", \"id\" : 1 }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/xml"))) {
                    String exampleString = "<category> <id>1</id> <name>Dog</name> </category>";
                    ApiUtil.setExampleResponse(request, "application/xml", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }
}
