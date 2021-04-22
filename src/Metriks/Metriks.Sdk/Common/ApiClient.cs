using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace Metriks.Sdk.Common
{
    internal class ApiClient
    {       
        protected static T DeserializeResults<T>(string msg)
        {
            JsonSerializerOptions options = new JsonSerializerOptions() { PropertyNameCaseInsensitive = true };
            var result = JsonSerializer.Deserialize<T>(msg, options);
            return result;
        }
    }
}
