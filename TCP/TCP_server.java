import java.io.*;
import java.net.*;

public class TCP_server {
    public static void main(String args[]) {
        ServerSocket serverSocket = null;
        Socket socket = null;

        try {
            int port = 6788; // Port number
            serverSocket = new ServerSocket(port);

            System.out.println("TCP Server waiting for client on port " + port);

            // Accept connection from client
            socket = serverSocket.accept();
            System.out.println("The client " + socket.getInetAddress() + ":" + socket.getPort() + " is connected");

            // Input and Output Streams
            DataInputStream in = new DataInputStream(socket.getInputStream());
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());

            // Read message from client
            String message = in.readUTF();
            System.out.println("Client said: " + message);

            // Send response
            out.writeUTF("Hello from TCP server!");

            // Close connections
            in.close();
            out.close();
            socket.close();
            serverSocket.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
