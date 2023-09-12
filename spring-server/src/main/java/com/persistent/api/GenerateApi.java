/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech) (6.3.0-SNAPSHOT).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package com.persistent.api;

import com.persistent.model.GenerateCodePost200Response;
import com.persistent.model.GenerateCodePost400Response;
import com.persistent.model.GenerateCodePostRequest;
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

@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2023-09-12T06:33:44.779494988Z[UTC]")
@Validated
@Tag(name = "generate", description = "the generate API")
public interface GenerateApi {

    default Optional<NativeWebRequest> getRequest() {
        return Optional.empty();
    }

    /**
     * POST /generate/code : Generate code from OpenAPI specification
     *
     * @param generateCodePostRequest  (required)
     * @return Code generated successfully (status code 200)
     *         or Bad request (status code 400)
     */
    @Operation(
        operationId = "generateCodePost",
        summary = "Generate code from OpenAPI specification",
        responses = {
            @ApiResponse(responseCode = "200", description = "Code generated successfully", content = {
                @Content(mediaType = "application/json", schema = @Schema(implementation = GenerateCodePost200Response.class))
            }),
            @ApiResponse(responseCode = "400", description = "Bad request", content = {
                @Content(mediaType = "application/json", schema = @Schema(implementation = GenerateCodePost400Response.class))
            })
        }
    )
    @RequestMapping(
        method = RequestMethod.POST,
        value = "/generate/code",
        produces = { "application/json" },
        consumes = { "application/json" }
    )
    default ResponseEntity<GenerateCodePost200Response> generateCodePost(
        @Parameter(name = "GenerateCodePostRequest", description = "", required = true) @Valid @RequestBody GenerateCodePostRequest generateCodePostRequest
    ) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf("application/json"))) {
                    String exampleString = "{ \"message\" : \"message\" }";
                    ApiUtil.setExampleResponse(request, "application/json", exampleString);
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }
}
