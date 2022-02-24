using System;

namespace TestApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string yourName;
            Console.WriteLine("What is your name?");
            yourName = Console.ReadLine();
            Console.WriteLine("Hello {0}", yourName);        
        }
    }
}