/**
 * Controller class for handling CRUD operations on Generate resource.
 */
package com.persistent.api;
import com.persistent.model.GenerateCodePost200Response;
import com.persistent.model.GenerateCodePost400Response;
import com.persistent.model.GenerateCodePostRequest;

import com.persistent.model.Generate;
import com.persistent.model.GenerateDto;
import com.persistent.service.GenerateService;



import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.multipart.MultipartFile;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import org.springframework.web.context.request.NativeWebRequest;

import javax.validation.constraints.*;
import javax.validation.Valid;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Generated;
import com.persistent.util.Constants;

@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2023-11-22T12:35:31.704Z[UTC]")
@Controller
@RequestMapping("${openapi.codeGeneration.base-path:/v1/apigen}")
public class GenerateApiController implements GenerateApi {

    private final NativeWebRequest request;

    /**
     * Service instance for database operations.
     */
    @Autowired
    private GenerateService generateService;

    @Autowired
    public GenerateApiController(NativeWebRequest request) {
        this.request = request;
    }

    @Override
    public Optional<NativeWebRequest> getRequest() {
        return Optional.ofNullable(request);
    }

    /**
     * Services the generateCodePost API POST call.
     * @return The Generate object with the API call response and appropriate HTTP 
     *         Status code.
     */
    @Override
    public ResponseEntity<GenerateCodePost200Response> generateCodePost(@Parameter(name = "GenerateCodePostRequest", description = "", required = true) @Valid @RequestBody GenerateCodePostRequest generateCodePostRequest
    ){
            return new ResponseEntity<GenerateCodePost200Response>(HttpStatus.NOT_IMPLEMENTED);
    }
}
