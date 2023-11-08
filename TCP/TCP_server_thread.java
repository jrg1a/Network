import java.io.*;
import java.net.*;
import java.util.concurrent.*;
import java.util.logging.*;

public class TCP_server_thread {
    private static final Logger LOGGER = Logger.getLogger(TCP_server_thread.class.getName());
    private static final int PORT = 6784; // endre port etter ønske!

    public static void main(String[] args) {
        ExecutorService clientHandlingExecutor = Executors.newCachedThreadPool();

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            LOGGER.info("TCP Server is running on port " + PORT);

            while (true) {
                try {
                    Socket clientSocket = serverSocket.accept();
                    clientHandlingExecutor.submit(new ClientHandler(clientSocket));
                } catch (IOException ex) {
                    LOGGER.log(Level.SEVERE, null, ex);
                }
            }
        } catch (IOException e) {
            LOGGER.log(Level.SEVERE, "Server Exception: ", e);
        } finally {
            clientHandlingExecutor.shutdown();
        }
    }

    private static class ClientHandler implements Runnable {
        private final Socket clientSocket;

        public ClientHandler(Socket socket) {
            this.clientSocket = socket;
        }

        public void run() {
            LOGGER.info("Connected to " + clientSocket.getRemoteSocketAddress());
        
            try (DataInputStream in = new DataInputStream(clientSocket.getInputStream());
                 DataOutputStream out = new DataOutputStream(clientSocket.getOutputStream())) {
        
                String message;
                while (true) {
                    try {
                        message = in.readUTF();
                        LOGGER.info("Received: " + message);
                        out.writeUTF("Echo: " + message);
        
                        if (message.equalsIgnoreCase("exit")) {
                            LOGGER.info("Client disconnected gracefully.");
                            break;
                        }
                    } catch (EOFException e) {
                        LOGGER.info("Client disconnected.");
                        break;
                    }
                }
            } catch (IOException e) {
                LOGGER.log(Level.SEVERE, "ClientHandler Exception: ", e);
            } finally {
                try {
                    clientSocket.close();
                } catch (IOException ex) {
                    LOGGER.log(Level.SEVERE, "Error closing the client socket", ex);
                }
            }
        }
        
    }
}
