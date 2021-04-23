using Metriks.Sdk.Common;
using Metriks.Sdk.ResponseModels;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
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

        public List<WeightGet> GetList()
        {
            var responseTask = GetWeightAsync().ConfigureAwait(false).GetAwaiter();
            var result = responseTask.GetResult();

            return result;
        }

        public async Task<List<WeightGet>> GetWeightAsync()
        {
            string path = "api/Weight";

            var responseTask = _client.GetAsync(path);
            var response = await responseTask;
            var resultList = ProcessResults<WeightList>(response);

            List<WeightGet> result = new List<WeightGet>();
            foreach (var item in resultList.Weights)
            {
                result.Add(item);
            }

            return result;
        }

        public WeightCreated Create(DateTime entryDate, double weight, string unit)
        {
            var responseTask = CreateAsync(entryDate, weight, unit).ConfigureAwait(false).GetAwaiter();
            var result = responseTask.GetResult();

            return result;
        }

        public async Task<WeightCreated> CreateAsync(DateTime entryDate, double weight, string unit)
        {
            string path = "api/Weight";

            RequestModels.WeightCreate requestSource = new RequestModels.WeightCreate();
            requestSource.EntryDate = entryDate;
            requestSource.Weight = weight;
            requestSource.Unit = unit;

            var jsonContent = GetJsonContentType(requestSource);

            var responseTask = _client.PostAsync(path, jsonContent);
            var response = await responseTask;
            var result = ProcessResults<WeightCreated>(response);

            return result;
        }

        public bool Delete(Guid id)
        {
            var responseTask = DeleteAsync(id).ConfigureAwait(false).GetAwaiter();
            var result = responseTask.GetResult();

            return result;
        }

        public async Task<bool> DeleteAsync(Guid id)
        {
            string path = $"api/Weight/{id}";

            var responseTask = _client.DeleteAsync(path);
            var response = await responseTask;

            // Assume success means: 200, 202 or 204
            bool result = response.IsSuccessStatusCode;

            if (!result)
            {
                // Do nothing if the status is Not Found (keep the result as false)
                if (response.StatusCode != System.Net.HttpStatusCode.NotFound)
                {
                    //TODO: raise an event to a global event hub to let 3rd parties understand what went wrong.
                    throw new HttpRequestException(response.ReasonPhrase, null, response.StatusCode);
                }
            }

            return result;
        }
    }
}
