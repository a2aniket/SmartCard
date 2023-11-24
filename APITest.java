import io.restassured.RestAssured;
import io.restassured.authentication.BasicAuthScheme;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.equalTo;

public class APIEndpointTest {

    @BeforeClass
    public void setup() {
        RestAssured.baseURI = "https://reqres.in/api";
    }

    @Test
    public void testGetUser() {
        given()
                .when()
                .get("/users/2")
                .then()
                .statusCode(200)
                .body("data.first_name", equalTo("Janet"));
    }

    @Test
    public void testCreateUser() {
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
    public void testUpdateUser() {
        given()
                .contentType(ContentType.JSON)
                .body("{\"name\": \"Isha\", \"job\": \"Software Engineer\"}")
                .when()
                .put("/users/2")
                .then()
                .statusCode(200);
    }

    @Test
    public void testDeleteUser() {
        given()
                .when()
                .delete("/users/2")
                .then()
                .statusCode(204);
    }

    @Test
    public void testGetUsersWithQuery() {
        given()
                .queryParam("page", "2")
                .when()
                .get("/users")
                .then()
                .statusCode(200);
    }

    @Test
    public void testGetUserByIdWithPathParam() {
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
        BasicAuthScheme basicAuthScheme = new BasicAuthScheme();
        basicAuthScheme.setUserName("username");
        basicAuthScheme.setPassword("password");

        given()
                .auth()
                .basic("username", "password")
                .when()
                .post("/register")
                .then()
                .statusCode(400);
    }
}