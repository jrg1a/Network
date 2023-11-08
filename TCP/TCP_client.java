import java.io.*;
import java.net.*;

public class TCP_client {
    public static void main(String args[]) {
        Socket socket = null;
        String serverIP = "localhost";
        int serverPort = 6785;

        try {
            socket = new Socket(serverIP, serverPort);

            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            DataInputStream in = new DataInputStream(socket.getInputStream());

            // Send message to server
            out.writeUTF("Hei, dette er fra client!");

            // Read response from server
            String response = in.readUTF();
            System.out.println("Server says: " + response);

            // Close connections
            out.close();
            in.close();
            socket.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
