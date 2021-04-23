using Metriks.Sdk.Domains.Clients.ResponseModels;
using Metriks.Sdk.Domains.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.Sdk.Domains
{
    public interface IWeight
    {
        List<WeightMeasurement> GetList();

        Task<List<WeightMeasurement>> GetListAsync();

        WeightMeasurement Create(DateTime entryDate, double weight, string unit);

        Task<WeightMeasurement> CreateAsync(DateTime entryDate, double weight, string unit);
      
        bool Delete(Guid id);

        Task<bool> DeleteAsync(Guid id);

        WeightMeasurement Get(Guid id);

        Task<WeightMeasurement> GetAsync(Guid id);
    }
}
