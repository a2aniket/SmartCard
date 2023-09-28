package com.persistent.model;

import java.net.URI;
import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonTypeName;
import org.openapitools.jackson.nullable.JsonNullable;
import java.time.OffsetDateTime;
import javax.validation.Valid;
import javax.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import javax.annotation.Generated;

import lombok.Data;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import javax.persistence.Entity;
import javax.persistence.Id;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.JsonProcessingException;
import java.io.IOException;
import com.fasterxml.jackson.core.type.TypeReference;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.SequenceGenerator;
/**
 * GenerateCodePost200Response
 */

@JsonTypeName("_generate_code_post_200_response")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2023-09-28T11:04:46.764923567Z[UTC]")
@Data
@Entity
@AllArgsConstructor
@NoArgsConstructor
public class GenerateCodePost200ResponseDto {

  @JsonProperty("message")
  private String message;

  
  public GenerateCodePost200ResponseDto(GenerateCodePost200Response generateCodePost200Response){    
    ObjectMapper mapper = new ObjectMapper();
    try{    
        this.message = generateCodePost200Response.getMessage();
    }catch (Exception e) {
        e.printStackTrace();
    }
  }

  public GenerateCodePost200Response toEntity(){
    GenerateCodePost200Response generateCodePost200Response = new GenerateCodePost200Response();
    ObjectMapper mapper = new ObjectMapper();
    try{    
        generateCodePost200Response.setMessage(this.message);
    }catch (Exception e) {
        e.printStackTrace();
    }
    return generateCodePost200Response;   
  }


}

