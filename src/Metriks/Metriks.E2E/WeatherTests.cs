using Metriks.E2E.Common;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Diagnostics;

namespace Metriks.E2E
{
    [TestClass]
    public class WeatherTests
    {
        [TestMethod]
        [Scenario("Get weather should return 5 items")]
        [Given("an end-user with access to the server")]
        [When("a request to retrieve weather is submitted")]
        [Then("5 days of forecasts are returned")]
        public void Get_weather_should_return_5_items()
        {
            // Arrange
            var expectedCount = 5;
            var client = TestHelper.GetSdkClient();

            // Act
            var actual = client.Weather.GetWeather();

            // Assert
            Assert.IsNotNull(actual);
            Assert.AreEqual(expectedCount, actual.Count);
            foreach (var forecast in actual)
            {
                Assert.IsTrue(forecast.Date >= System.DateTime.Now.AddDays(-1), $"Invalid date: {forecast.Date}");
            }

        }
    }
}
