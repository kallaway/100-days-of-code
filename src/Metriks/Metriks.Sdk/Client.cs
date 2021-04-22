using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using System.Text.Json;
using Metriks.Sdk.ResponseModels;
using Metriks.Sdk.Common;
using Metriks.Sdk.Domains;

namespace Metriks.Sdk
{
    public class Client
    {
        private static HttpClient _client;

       public IWeather Weather { get; set; }
      
        /// <summary>
        /// Intializes the client and sets the request header user-agent to the consumingApplicationName
        /// </summary>
        /// <param name="consumingApplicationName">The name of the application that is consuming the SDK</param>
        /// <param name="metriksApiBaseAddress">The base address of the API</param>
        internal Client(string consumingApplicationName, string metriksApiBaseAddress)
        {
            InitializeClient(consumingApplicationName, metriksApiBaseAddress);
            Weather = new Weather(_client);
        }

        private static void InitializeClient(string consumingApplicationName, string apiBaseAddress)
        {
            _client = new HttpClient();
            _client.DefaultRequestHeaders.Accept.Clear();
            _client.DefaultRequestHeaders.Accept.Add(
                new MediaTypeWithQualityHeaderValue("application/json"));
            _client.DefaultRequestHeaders.Add("User-Agent", consumingApplicationName);
            _client.BaseAddress = new Uri(apiBaseAddress);
        }

      

    }
}
