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
 * GenerateCodePost400Response
 */

@JsonTypeName("_generate_code_post_400_response")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2023-09-20T12:11:19.052532203Z[UTC]")
@Data
@Entity
@AllArgsConstructor
@NoArgsConstructor
public class GenerateCodePost400ResponseDto {

  @JsonProperty("message")
  private String message;

  
  public GenerateCodePost400ResponseDto(GenerateCodePost400Response generateCodePost400Response){    
    ObjectMapper mapper = new ObjectMapper();
    try{    
        this.message = generateCodePost400Response.getMessage();
    }catch (Exception e) {
        e.printStackTrace();
    }
  }

  public GenerateCodePost400Response toEntity(){
    GenerateCodePost400Response generateCodePost400Response = new GenerateCodePost400Response();
    ObjectMapper mapper = new ObjectMapper();
    try{    
        generateCodePost400Response.setMessage(this.message);
    }catch (Exception e) {
        e.printStackTrace();
    }
    return generateCodePost400Response;   
  }


}

