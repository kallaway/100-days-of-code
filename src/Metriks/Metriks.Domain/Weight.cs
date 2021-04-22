using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Metriks.Domain.Common;
using Metriks.Domain.Data;
using Metriks.Domain.Models;
using Microsoft.Data.Sqlite;

namespace Metriks.Domain
{
    public class Weight
    {
        public (bool created, WeightMeasurement measurement) Create(WeightMeasurement measurement)
        {
            if (measurement is null)
            {
                throw new ArgumentNullException(nameof(measurement));
            }

            if (measurement.Id == Guid.Empty)
            {
                measurement.Id = Guid.NewGuid();
            }

            WeightDataStore store = new WeightDataStore();
            var result = store.Create(measurement);

            return (result, measurement);
        }

        public List<WeightMeasurement> Read()
        {
            WeightDataStore store = new WeightDataStore();
            var result = store.Read();

            return result;
        }
    }
}
