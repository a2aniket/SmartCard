import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.testng.annotations.Test;

import static org.hamcrest.Matchers.*;
import static io.restassured.RestAssured.given;

public class ApiTests {

    @Test
    public void testGetUserById() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .when()
                .get("/users/2")
                .then()
                .statusCode(200)
                .body("data.first_name", equalTo("Janet"));
    }

    @Test
    public void testCreateUser() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .contentType(ContentType.JSON)
                .body("{\"name\": \"Sam\", \"job\": \"Project Leader\"}")
                .when()
                .post("/users")
                .then()
                .statusCode(201)
                .body("name", equalTo("Sam"))
                .body("job", containsString("Leader"));
    }

    @Test
    public void testUpdateUserById() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .contentType(ContentType.JSON)
                .body("{\"name\": \"Isha\", \"job\": \"Software Engineer\"}")
                .when()
                .put("/users/2")
                .then()
                .statusCode(200);
    }

    @Test
    public void testDeleteUserById() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .when()
                .delete("/users/2")
                .then()
                .statusCode(204);
    }

    @Test
    public void testGetUsersByPage() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .param("page", "2")
                .when()
                .get("/users")
                .then()
                .statusCode(200);
    }

    @Test
    public void testGetUserByIdWithPathParam() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .pathParam("id", "3")
                .when()
                .get("/users/{id}")
                .then()
                .statusCode(200)
                .body("data.last_name", equalTo("Wong"));
    }

    @Test
    public void testRegisterWithBasicAuth() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .auth()
                .preemptive()
                .basic("username", "password")
                .when()
                .post("/register")
                .then()
                .statusCode(400);
    }
}