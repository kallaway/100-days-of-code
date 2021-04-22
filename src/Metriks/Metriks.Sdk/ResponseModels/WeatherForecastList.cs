using System.Collections.Generic;

namespace Metriks.Sdk.ResponseModels
{
    public class WeatherForecastList
    {
        public List<WeatherForecast> Forecasts { get; set; } = new List<WeatherForecast>();

        public static WeatherForecastList MapFrom(List<WeatherForecast> forecasts)
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
