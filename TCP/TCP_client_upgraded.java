import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TCP_client_upgraded {
    private static final String SERVER_IP = "localhost";
    private static final int SERVER_PORT = 6784;

    public static void main(String[] args) {
        try (Socket socket = new Socket(SERVER_IP, SERVER_PORT);
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             DataInputStream in = new DataInputStream(socket.getInputStream());
             Scanner scanner = new Scanner(System.in)) {

            System.out.println("Connected to server at " + SERVER_IP + ":" + SERVER_PORT);
            String input;
            do {
                System.out.print("Enter message (type 'exit' to quit): ");
                input = scanner.nextLine();

                out.writeUTF(input);
                System.out.println("Sent to server: " + input);

                String response = in.readUTF();
                System.out.println("Server response: " + response);

            } while (!input.equalsIgnoreCase("exit"));

        } catch (UnknownHostException e) {
            System.err.println("Server not found: " + e.getMessage());
        } catch (EOFException e) {
            System.err.println("Server has closed the connection: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("I/O error: " + e.getMessage());
        }
    }
}
