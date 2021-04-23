using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace Metriks.Sdk.Common
{
    internal class ApiClient
    {
        protected StringContent GetJsonContentType(object value)
        {
            return new StringContent(SerializeRequest(value), System.Text.Encoding.UTF8, "application/json");
        }

        protected string SerializeRequest(object value)
        {
            JsonSerializerOptions options = new JsonSerializerOptions() { PropertyNameCaseInsensitive = true };
            string json = JsonSerializer.Serialize(value);

            return json;
        }

        protected T ProcessResults<T>(HttpResponseMessage httpResponseMessage)
        {
            JsonSerializerOptions options = new JsonSerializerOptions() { PropertyNameCaseInsensitive = true };

            if (httpResponseMessage.IsSuccessStatusCode)
            {
                var stringTask = httpResponseMessage.Content.ReadAsStringAsync().ConfigureAwait(false).GetAwaiter();
                string contentString = stringTask.GetResult();

                var result = JsonSerializer.Deserialize<T>(contentString, options);
                return result;
            }

            // TODO: Make the return type nullable 
            //return default(T);
            throw new HttpRequestException(httpResponseMessage.ReasonPhrase, null, httpResponseMessage.StatusCode);
        }
    }
}
