using Metriks.Sdk.Common;
using Metriks.Sdk.ResponseModels;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

namespace Metriks.Sdk.Domains
{
    internal class WeightApiClient : ApiClient, IWeight
    {
        HttpClient _client;

        public WeightApiClient(HttpClient client)
        {
            _client = client;
        }

        public List<WeightGet> GetWeight()
        {
            var requestTask = GetWeightAsync().ConfigureAwait(false).GetAwaiter();
            var result = requestTask.GetResult();

            return result;
        }


        public async Task<List<WeightGet>> GetWeightAsync()
        {
            string path = "api/Weight";

            var stringTask = _client.GetStringAsync(path);
            var msg = await stringTask;
            var resultList = DeserializeResults<WeightList>(msg);

            List<WeightGet> result = new List<WeightGet>();
            foreach (var item in resultList.Weights)
            {
                result.Add(item);
            }

            return result;
        }
    }
}
