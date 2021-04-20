using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Diagnostics;

namespace Metriks.E2E
{
    [TestClass]
    public class WeatherUnitTests
    {
        [TestMethod]
        public void GetWeatherShouldReturn5Items()
        {
            // Arrange
            var expectedCount = 5;
            var client = Metriks.Sdk.Authentication.GetClient("Metriks E2E Tests", "https://localhost:44379/");

            // Act
            var weatherTask = client.GetWeatherAsync().ConfigureAwait(false).GetAwaiter();
            var weatherForecast = weatherTask.GetResult();

            // Assert
            Assert.IsNotNull(weatherForecast);
            Assert.AreEqual(expectedCount, weatherForecast.Count);
            foreach (var forecast in weatherForecast)
            {
                Assert.IsTrue(forecast.Date >= System.DateTime.Now.AddDays(-1), $"Invalid date: {forecast.Date}");
            }

        }
    }
}
