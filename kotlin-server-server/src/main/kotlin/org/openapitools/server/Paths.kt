/**
* Code Generation API
* No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
*
* The version of the OpenAPI document: 1.0.0
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
package org.openapitools.server

import io.ktor.locations.*
import org.openapitools.server.models.*

@KtorExperimentalLocationsAPI
object Paths {
    /**
     * Generate code from OpenAPI specification
     * 
     * @param generateCodePostRequest  
     */
    @Location("/generate/code") class generateCodePost(val generateCodePostRequest: GenerateCodePostRequest)

}
