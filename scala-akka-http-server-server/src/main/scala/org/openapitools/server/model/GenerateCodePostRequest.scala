package org.openapitools.server.model


/**
 * @param language The programming language to generate code for for example: ''null''
 * @param openAPIUrl The URL of the OpenAPI specification to generate code from for example: ''null''
*/
final case class GenerateCodePostRequest (
  language: String,
  openAPIUrl: String
)

