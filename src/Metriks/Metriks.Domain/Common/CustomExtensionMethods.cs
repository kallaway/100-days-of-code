using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.Domain.Common
{
    public static class CustomExtensionMethods
    {
        public static int ToUnixTimeSeconds(this DateTime dateTime)
        {
            return (int)dateTime.Subtract(new DateTime(1970, 1, 1, 0, 0, 0)).TotalSeconds;
        }
    }
}
