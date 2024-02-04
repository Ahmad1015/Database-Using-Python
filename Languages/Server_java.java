import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

public class Server_java {
    public static void main(String[] args) {
        // GET request
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create("http://localhost:1000"))
              .build();

        client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
              .thenApply(HttpResponse::body)
              .thenAccept(System.out::println)
              .join();

        String data = "Can you just give me  SQL to create a table called Customers with ID , name , email as columns, After that give me SQL to add 2 different entries and then display everything in that Table.Just give me the sql lines, dont give me any character apart from it";

        // POST request
        HttpRequest requestPost = HttpRequest.newBuilder()
            .uri(URI.create("http://localhost:1000"))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString("{\"value\":\"" + data + "\"}"))
            .build();

        client.sendAsync(requestPost, HttpResponse.BodyHandlers.ofString())
              .thenApply(HttpResponse::body)
              .thenAccept(System.out::println)
              .join();
    }
}