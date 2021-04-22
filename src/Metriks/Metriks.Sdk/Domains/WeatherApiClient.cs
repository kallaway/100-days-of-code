using Metriks.Sdk.Common;
using Metriks.Sdk.ResponseModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.Sdk.Domains
{
    internal class WeatherApiClient : ApiClient, IWeather
    {
        HttpClient _client;

        public WeatherApiClient(HttpClient client)
        {
            _client = client;
        }

        public async Task<List<WeatherForecast>> GetWeatherAsync()
        {
            string path = "api/WeatherForecast";

            var responseTask = _client.GetAsync(path);
            var response = await responseTask;
            var resultList = ProcessResults<WeatherForecastList>(response);

            List<WeatherForecast> result = new List<WeatherForecast>();
            foreach (var item in resultList.Forecasts)
            {
                result.Add(item);
            }

            return result;
        }

        public List<WeatherForecast> GetWeather()
        {
            var responseTask = GetWeatherAsync().ConfigureAwait(false).GetAwaiter();
            var result = responseTask.GetResult();

            return result;
        }
    }
}
