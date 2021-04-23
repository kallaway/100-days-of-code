using Metriks.Sdk.Common;
using Metriks.Sdk.Domains.Clients.ResponseModels;
using Metriks.Sdk.Domains.Models;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

namespace Metriks.Sdk.Domains.Clients
{
    internal class WeightApiClient : ApiClient, IWeight
    {
        HttpClient _client;

        public WeightApiClient(HttpClient client)
        {
            _client = client;
        }

        public List<WeightMeasurement> GetList()
        {
            var responseTask = GetListAsync().ConfigureAwait(false).GetAwaiter();
            var result = responseTask.GetResult();

            return result;
        }

        public async Task<List<WeightMeasurement>> GetListAsync()
        {
            string path = "api/Weight";

            var responseTask = _client.GetAsync(path);
            var response = await responseTask;
            var resultList = ProcessResults<WeightList>(response);

            List<WeightMeasurement> result = new List<WeightMeasurement>();
            foreach (var item in resultList.Weights)
            {
                result.Add(item.MapTo());
            }

            return result;
        }

        public WeightMeasurement Create(DateTime entryDate, double weight, string unit)
        {
            var responseTask = CreateAsync(entryDate, weight, unit).ConfigureAwait(false).GetAwaiter();
            var result = responseTask.GetResult();

            return result;
        }

        public async Task<WeightMeasurement> CreateAsync(DateTime entryDate, double weight, string unit)
        {
            string path = "api/Weight";

            var requestSource = new RequestModels.WeightCreate();
            requestSource.EntryDate = entryDate;
            requestSource.Weight = weight;
            requestSource.Unit = unit;

            var jsonContent = GetJsonContentType(requestSource);

            var responseTask = _client.PostAsync(path, jsonContent);
            var response = await responseTask;
            var result = ProcessResults<WeightCreated>(response);

            return result.MapTo();
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

        public WeightMeasurement Get(Guid id)
        {
            var responseTask = GetAsync(id).ConfigureAwait(false).GetAwaiter();
            var result = responseTask.GetResult();

            return result;
        }

        public async Task<WeightMeasurement> GetAsync(Guid id)
        {
            string path = $"api/Weight/{id}";

            var responseTask = _client.GetAsync(path);
            var response = await responseTask;
            var result = ProcessResults<WeightGet>(response);

            return result.MapTo();
        }
    }
}
