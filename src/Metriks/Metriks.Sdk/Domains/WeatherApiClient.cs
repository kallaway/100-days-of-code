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

            var stringTask = _client.GetStringAsync(path);
            var msg = await stringTask;
            var resultList = DeserializeResults<WeatherForecastList>(msg);

            List<WeatherForecast> result = new List<WeatherForecast>();
            foreach (var item in resultList.Forecasts)
            {
                result.Add(item);
            }

            return result;
        }

        public List<WeatherForecast> GetWeather()
        {
            var requestTask = GetWeatherAsync().ConfigureAwait(false).GetAwaiter();
            var result = requestTask.GetResult();

            return result;
        }
    }
}
