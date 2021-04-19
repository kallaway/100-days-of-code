namespace Metriks.Sdk
{
    /// <summary>
    /// Starting point to using the Metriks SDK.
    /// </summary>
    public static class Authentication
    {
        /// <summary>
        ///  Authenticates as necessary with the server to produce a valid client SDK
        /// </summary>
        /// <param name="consumingApplicationName">The name of the application that is consuming the SDK</param>
        /// <param name="metriksApiBaseAddress">The base address of the API</param>
        /// <returns></returns>
        public static Client GetClient(string consumingApplicationName, string metriksApiBaseAddress)
        {
            // TODO: Singleton?
            return new Client(consumingApplicationName, metriksApiBaseAddress);
        }
    }
}
