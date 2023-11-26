import io.restassured.RestAssured;
import io.restassured.authentication.BasicAuthScheme;
import io.restassured.http.ContentType;
import org.junit.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class APIEndpointValidationTest {

    private static final String BASE_URI = "https://reqres.in/api";
    private static final String USERNAME = "testuser";
    private static final String PASSWORD = "testpass";

    @BeforeClass
    public void setUp() {
        RestAssured.baseURI = BASE_URI;
    }

    @Test
    public void testGetUser() {
        given()
                .when()
                .get("/users/2")
                .then()
                .assertThat()
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
                .assertThat()
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
                .assertThat()
                .statusCode(200);
    }

    @Test
    public void testDeleteUser() {
        given()
                .when()
                .delete("/users/2")
                .then()
                .assertThat()
                .statusCode(204);
    }

    @Test
    public void testGetUsersWithPagination() {
        given()
                .when()
                .queryParam("page", 2)
                .get("/users")
                .then()
                .assertThat()
                .statusCode(200)
                .body("data", hasSize(6))
                .body("total_pages", equalTo(2))
                .body("page", equalTo(2));
    }

    @Test
    public void testRegisterUserWithBasicAuth() {
        BasicAuthScheme authScheme = new BasicAuthScheme();
        authScheme.setUserName(USERNAME);
        authScheme.setPassword(PASSWORD);
        given()
                .auth()
                .basic(authScheme.getUserName(), authScheme.getPassword())
                .when()
                .post("/register")
                .then()
                .assertThat()
                .statusCode(400);
    }

    @Test
    public void testGetUserWithPathVariable() {
        given()
                .when()
                .pathParam("id", 3)
                .get("/users/{id}")
                .then()
                .assertThat()
                .statusCode(200)
                .body("data.last_name", equalTo("Wong"));
    }
}