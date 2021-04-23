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
        ISimpleDataStore<WeightMeasurement> _store;
                
        public Weight()
        {
            _store = new WeightDataStore();
        }

        public Weight(ISimpleDataStore<WeightMeasurement> store)
        {
            _store = store;
        }

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

            var result = _store.Create(measurement);

            return (result, measurement);
        }

        public List<WeightMeasurement> Read()
        {
            var result = _store.Read();

            return result;
        }

        public WeightMeasurement Read(Guid id)
        {
            var result = _store.Read(id);

            return result;
        }

        public bool Delete(Guid id)
        {
            var result = _store.Delete(id);

            return result;
        }
    }
}
