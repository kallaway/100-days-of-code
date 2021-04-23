using System.Collections.Generic;

namespace Metriks.Sdk.Domains.Clients.ResponseModels
{
    internal class WeatherForecastList
    {
        public List<WeatherForecastGet> Forecasts { get; set; } = new List<WeatherForecastGet>();

        public static WeatherForecastList MapFrom(List<WeatherForecastGet> forecasts)
        {
            WeatherForecastList result = new WeatherForecastList();
            foreach (var forecast in forecasts)
            {
                result.Forecasts.Add(forecast);
            }

            return result;
        }
    }
}
