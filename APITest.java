import io.restassured.RestAssured;
import io.restassured.authentication.AuthenticationScheme;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class APITest {

    // Test 1
    @Test
    public void testGetUser() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .when()
                .get("/users/2")
                .then()
                .assertThat().statusCode(200)
                .body("data.first_name", equalTo("Janet"));
    }

    // Test 2
    @Test
    public void testCreateUser() {
        RestAssured.baseURI = "https://reqres.in/api";
        String request = "{\"name\": \"Sam\", \"job\": \"Project Leader\"}";
        given()
                .header("Content-Type", "application/json")
                .body(request)
                .when()
                .post("/users")
                .then()
                .assertThat().statusCode(201)
                .body("name", equalTo("Sam"))
                .body("job", containsString("Leader"));
    }

    // Test 3
    @Test
    public void testUpdateUser() {
        RestAssured.baseURI = "https://reqres.in/api";
        String request = "{\"name\": \"Isha\", \"job\": \"Software Engineer\"}";
        given()
                .header("Content-Type", "application/json")
                .body(request)
                .when()
                .put("/users/2")
                .then()
                .assertThat().statusCode(200);
    }

    // Test 4
    @Test
    public void testDeleteUser() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .when()
                .delete("/users/2")
                .then()
                .assertThat().statusCode(204);
    }

    // Test 5
    @Test
    public void testGetUsersWithPageQueryParameter() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .param("page", "2")
                .when()
                .get("/users")
                .then()
                .assertThat().statusCode(200);
    }

    // Test 6
    @Test
    public void testGetUserWithIdPathParam() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .pathParam("id", "3")
                .when()
                .get("/users/{id}")
                .then()
                .assertThat().statusCode(200)
                .body("data.last_name", equalTo("Wong"));
    }

    // Test 7
    @Test
    public void testRegisterUserWithBasicAuth() {
        RestAssured.baseURI = "https://reqres.in/api";
        given()
                .auth().basic("username", "password")
                .when()
                .post("/register")
                .then()
                .assertThat().statusCode(400);
    }
}