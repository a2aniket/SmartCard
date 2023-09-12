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
 * GenerateCodePostRequest
 */

@JsonTypeName("_generate_code_post_request")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2023-09-12T06:54:12.378002081Z[UTC]")
@Data
@Entity
@AllArgsConstructor
@NoArgsConstructor
public class GenerateCodePostRequestDto {

  @JsonProperty("language")
  private String language;

  @JsonProperty("openAPIUrl")
  private String openAPIUrl;

  
  public GenerateCodePostRequestDto(GenerateCodePostRequest generateCodePostRequest){    
    ObjectMapper mapper = new ObjectMapper();
    try{    
        this.language = generateCodePostRequest.getLanguage();
        this.openAPIUrl = generateCodePostRequest.getOpenAPIUrl();
    }catch (Exception e) {
        e.printStackTrace();
    }
  }

  public GenerateCodePostRequest toEntity(){
    GenerateCodePostRequest generateCodePostRequest = new GenerateCodePostRequest();
    ObjectMapper mapper = new ObjectMapper();
    try{    
        generateCodePostRequest.setLanguage(this.language);
        generateCodePostRequest.setOpenAPIUrl(this.openAPIUrl);
    }catch (Exception e) {
        e.printStackTrace();
    }
    return generateCodePostRequest;   
  }


}

