using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.E2E.Common
{
    internal static class TestHelper
    {
        internal static string GetServerAddress()
        {
            return "https://localhost:44379/";
        }

        internal static string GetTestApplicationName()
        {
            return "Metriks E2E Tests";
        }

        internal static Sdk.Client GetSdkClient()
        {
            return Sdk.Authentication.GetClient(TestHelper.GetTestApplicationName(), TestHelper.GetServerAddress());
        }

        internal static DateTime GetRandomPastDate(int minInPast, int maxInPast)
        {
            Random rnd = new Random(Guid.NewGuid().GetHashCode());
            return DateTime.UtcNow.AddDays(rnd.Next(minInPast, maxInPast) * -1);
        }

        internal static double GetRandomDouble(int min, int max)
        {
            Random rnd = new Random(Guid.NewGuid().GetHashCode());
            return rnd.Next(min, max) + rnd.NextDouble();
        }

    }
}
