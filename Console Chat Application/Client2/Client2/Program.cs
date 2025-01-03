using System.Net.Sockets;
using System.Text;

namespace Client2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            const string serverAddress = "127.0.0.1";
            const int port = 5000;

            TcpClient client = new TcpClient();

            try
            {
                client.Connect(serverAddress, port);
                Console.WriteLine("Connected to the server!");

                NetworkStream stream = client.GetStream();

                // Thread for receiving messages

                Thread receiveThread = new Thread(() =>
                {
                    try
                    {
                        byte[] buffer = new byte[1024];
                        while (true)
                        {
                            int bytesRead = stream.Read(buffer, 0, buffer.Length);
                            if (bytesRead == 0) break;

                            string message = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                            Console.WriteLine(message);
                        }
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Error receiving data: {ex.Message}");
                    }
                });

                receiveThread.Start();

                //// Enter username
                //Console.WriteLine("Enter your username:");
                //string username = Console.ReadLine();
                //byte[] usernameBuffer = Encoding.UTF8.GetBytes(username);
                //stream.Write(usernameBuffer, 0, usernameBuffer.Length);

                // Main thread for sending messages

                while (true)
                {
                    string message = Console.ReadLine();
                    if (message.ToLower() == "exit") break;

                    byte[] buffer = Encoding.UTF8.GetBytes(message);
                    stream.Write(buffer, 0, buffer.Length);
                }

                Console.WriteLine("Disconnected from the server.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
            finally
            {
                client.Close();
            }

        }
    }
}
