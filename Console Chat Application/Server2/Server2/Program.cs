using System.Net;
using System.Net.Sockets;
using System.Text;

namespace Server2
{
    internal class Program
    {
        private static Dictionary<string, TcpClient> clients = new Dictionary<string, TcpClient>();
        private static object lockObject = new object();
        static void Main(string[] args)
        {
            TcpListener server = new TcpListener(IPAddress.Any, 5000);
            server.Start();
            Console.WriteLine($"Server started ......");

            while (true)
            {
                TcpClient client = server.AcceptTcpClient();
                Thread clientThread = new Thread(() => HandleClient(client));
                clientThread.Start();
            }

        }

        private static void HandleClient(TcpClient client)
        {
            NetworkStream stream = client.GetStream();
            string username = null;

            try
            {
                // Ask for username
                byte[] welcomeBuffer = Encoding.UTF8.GetBytes("Enter your username: ");
                stream.Write(welcomeBuffer, 0, welcomeBuffer.Length);

                byte[] buffer = new byte[1024];
                int bytesRead = stream.Read(buffer, 0, buffer.Length);
                username = Encoding.UTF8.GetString(buffer, 0, bytesRead).Trim();

                lock (lockObject)
                {
                    // Check if username is already taken
                    if (clients.ContainsKey(username))
                    {
                        string errorMessage = "Username already taken. Disconnecting.\n";
                        byte[] errorBuffer = Encoding.UTF8.GetBytes(errorMessage);
                        stream.Write(errorBuffer, 0, errorBuffer.Length);
                        client.Close();
                        return;
                    }

                    // Add client to the dictionary
                    clients[username] = client;
                }

                Console.WriteLine($"{username} connected.");
                BroadcastMessage($"[Server]: {username} has joined the chat.");

                while (true)
                {
                    buffer = new byte[1024];
                    bytesRead = stream.Read(buffer, 0, buffer.Length);
                    if (bytesRead == 0) break;

                    string message = Encoding.UTF8.GetString(buffer, 0, bytesRead).Trim();
                    Console.WriteLine($"Received from {username}: {message}");

                    if (message.StartsWith("/send"))
                    {
                        // Command format: /send <targetUsername> <message>
                        string[] parts = message.Split(' ', 3);
                        if (parts.Length == 3)
                        {
                            string targetUsername = parts[1];
                            string clientMessage = parts[2];

                            lock (lockObject)
                            {
                                if (clients.TryGetValue(targetUsername, out TcpClient targetClient))
                                {
                                    string forwardedMessage = $"[From {username}]: {clientMessage}";
                                    byte[] forwardedBuffer = Encoding.UTF8.GetBytes(forwardedMessage);
                                    targetClient.GetStream().Write(forwardedBuffer, 0, forwardedBuffer.Length);
                                    Console.WriteLine($"Message from {username} forwarded to {targetUsername}");
                                }
                                else
                                {
                                    string errorMessage = "Error: Target user not found.\n";
                                    byte[] errorBuffer = Encoding.UTF8.GetBytes(errorMessage);
                                    stream.Write(errorBuffer, 0, errorBuffer.Length);
                                }
                            }
                        }
                        else
                        {
                            string errorMessage = "Error: Invalid message format.\n";
                            byte[] errorBuffer = Encoding.UTF8.GetBytes(errorMessage);
                            stream.Write(errorBuffer, 0, errorBuffer.Length);
                        }
                    }
                    else if (message == "/list")
                    {
                        // List all connected clients
                        lock (lockObject)
                        {
                            string clientList = "Connected users: " + string.Join(", ", clients.Keys) + "\n";
                            byte[] listBuffer = Encoding.UTF8.GetBytes(clientList);
                            stream.Write(listBuffer, 0, listBuffer.Length);
                        }
                    }
                    else
                    {
                        BroadcastMessage($"[{username}]: {message}");
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error with {username}: {ex.Message}");
            }
            finally
            {
                lock (lockObject)
                {
                    if (username != null) clients.Remove(username);
                }
                Console.WriteLine($"{username} disconnected.");
                BroadcastMessage($"[Server]: {username} has left the chat.");
                client.Close();
            }
        }

        private static void BroadcastMessage(string message)
        {
            lock (lockObject)
            {
                byte[] buffer = Encoding.UTF8.GetBytes(message + "\n");
                foreach (var client in clients.Values)
                {
                    try
                    {
                        client.GetStream().Write(buffer, 0, buffer.Length);
                    }
                    catch
                    {
                        // Ignore errors while broadcasting
                    }
                }
            }
        }

    }
}
