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
import javax.persistence.Entity;
import javax.persistence.Id;
/**
 * GenerateCodePost200Response
 */

@JsonTypeName("_generate_code_post_200_response")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2023-09-14T14:50:22.128927806Z[UTC]")
@Data
public class GenerateCodePost200Response {

  private String message;
  


}
