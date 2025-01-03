namespace Multi_threaded_Image_Processing
{
    using System;
    using System.Drawing;
    using System.Threading;

    class Program
    {
        static void ProcessImage(string imagePath, string outputPath)
        {
            Console.WriteLine($"Processing image: {imagePath}");

            // Load the image
            Bitmap bitmap = new Bitmap(imagePath);

            // Apply grayscale filter
            for (int y = 0; y < bitmap.Height; y++)
            {
                for (int x = 0; x < bitmap.Width; x++)
                {
                    Color pixelColor = bitmap.GetPixel(x, y);
                    int grayValue = (int)(pixelColor.R * 0.3 + pixelColor.G * 0.59 + pixelColor.B * 0.11);
                    bitmap.SetPixel(x, y, Color.FromArgb(grayValue, grayValue, grayValue));
                }
            }

            // Save the processed image
            bitmap.Save(outputPath);
            Console.WriteLine($"Image processed and saved as: {outputPath}");
        }

        static void Main()
        {
            string[] imagePaths = { "image1.jpg", "image2.jpg" };
            string[] outputPaths = { "image1_processed.jpg", "image2_processed.jpg" };

            Thread[] threads = new Thread[imagePaths.Length];
            for (int i = 0; i < imagePaths.Length; i++)
            {
                int index = i;  
                threads[i] = new Thread(() => ProcessImage(imagePaths[index], outputPaths[index]));
                threads[i].Start();
            }

            foreach (var thread in threads)
            {
                thread.Join(); // Wait for all image processing to finish
            }

            Console.WriteLine("All images processed.");
        }
    }

}
