import io.restassured.RestAssured;
import io.restassured.authentication.BasicAuthScheme;
import io.restassured.http.ContentType;
import org.junit.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class ApiTest {

    @Test
    public void verifyGetUserById() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .when()
                .get("/users/2")
                .then()
                .statusCode(200)
                .body("data.first_name", equalTo("Janet"));
    }

    @Test
    public void verifyCreateUser() {
        RestAssured.baseURI = "https://reqres.in/api";
        String requestBody = "{\n" +
                "    \"name\": \"Sam\",\n" +
                "    \"job\": \"Project Leader\"\n" +
                "}";
        given()
                .contentType(ContentType.JSON)
                .body(requestBody)
                .when()
                .post("/users")
                .then()
                .statusCode(201)
                .body("name", equalTo("Sam"))
                .body("job", containsString("Leader"));
    }

    @Test
    public void verifyUpdateUser() {
        RestAssured.baseURI = "https://reqres.in/api";
        String requestBody = "{\n" +
                "    \"name\": \"Isha\",\n" +
                "    \"job\": \"Software Engineer\"\n" +
                "}";
        given()
                .contentType(ContentType.JSON)
                .body(requestBody)
                .when()
                .put("/users/2")
                .then()
                .statusCode(200);
    }

    @Test
    public void verifyDeleteUser() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .when()
                .delete("/users/2")
                .then()
                .statusCode(204);
    }

    @Test
    public void verifyGetUsersWithQueryParams() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .queryParam("page", 2)
                .when()
                .get("/users")
                .then()
                .statusCode(200);
    }

    @Test
    public void verifyGetUserByIdWithPathParams() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .pathParam("id", 3)
                .when()
                .get("/users/{id}")
                .then()
                .statusCode(200)
                .body("data.last_name", equalTo("Wong"));
    }

    @Test
    public void verifyRegisterWithBasicAuth() {
        RestAssured.baseURI = "https://reqres.in/api";
        BasicAuthScheme authScheme = new BasicAuthScheme();
        authScheme.setUserName("username");
        authScheme.setPassword("password");
        given()
                .auth().basic("username", "password")
                .when()
                .post("/register")
                .then()
                .statusCode(400);
    }

    @Test
    public void verifyGetUserWithCacheControl() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .when()
                .get("/users/2")
                .then()
                .statusCode(200)
                .header("Cache-Control", equalTo("max-age=14400"));
    }
}