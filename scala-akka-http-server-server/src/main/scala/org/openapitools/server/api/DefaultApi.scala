package org.openapitools.server.api

import akka.http.scaladsl.server.Directives._
import akka.http.scaladsl.server.Route
import akka.http.scaladsl.model.StatusCodes
import akka.http.scaladsl.marshalling.ToEntityMarshaller
import akka.http.scaladsl.unmarshalling.FromEntityUnmarshaller
import akka.http.scaladsl.unmarshalling.FromStringUnmarshaller
import org.openapitools.server.AkkaHttpHelper._
import org.openapitools.server.model.GenerateCodePost200Response
import org.openapitools.server.model.GenerateCodePost400Response
import org.openapitools.server.model.GenerateCodePostRequest


class DefaultApi(
    defaultService: DefaultApiService,
    defaultMarshaller: DefaultApiMarshaller
) {

  
  import defaultMarshaller._

  lazy val route: Route =
    path("generate" / "code") { 
      post {  
            entity(as[GenerateCodePostRequest]){ generateCodePostRequest =>
              defaultService.generateCodePost(generateCodePostRequest = generateCodePostRequest)
            }
      }
    }
}


trait DefaultApiService {

  def generateCodePost200(responseGenerateCodePost200Response: GenerateCodePost200Response)(implicit toEntityMarshallerGenerateCodePost200Response: ToEntityMarshaller[GenerateCodePost200Response]): Route =
    complete((200, responseGenerateCodePost200Response))
  def generateCodePost400(responseGenerateCodePost400Response: GenerateCodePost400Response)(implicit toEntityMarshallerGenerateCodePost400Response: ToEntityMarshaller[GenerateCodePost400Response]): Route =
    complete((400, responseGenerateCodePost400Response))
  /**
   * Code: 200, Message: Code generated successfully, DataType: GenerateCodePost200Response
   * Code: 400, Message: Bad request, DataType: GenerateCodePost400Response
   */
  def generateCodePost(generateCodePostRequest: GenerateCodePostRequest)
      (implicit toEntityMarshallerGenerateCodePost400Response: ToEntityMarshaller[GenerateCodePost400Response], toEntityMarshallerGenerateCodePost200Response: ToEntityMarshaller[GenerateCodePost200Response]): Route

}

trait DefaultApiMarshaller {
  implicit def fromEntityUnmarshallerGenerateCodePostRequest: FromEntityUnmarshaller[GenerateCodePostRequest]



  implicit def toEntityMarshallerGenerateCodePost400Response: ToEntityMarshaller[GenerateCodePost400Response]

  implicit def toEntityMarshallerGenerateCodePost200Response: ToEntityMarshaller[GenerateCodePost200Response]

}

