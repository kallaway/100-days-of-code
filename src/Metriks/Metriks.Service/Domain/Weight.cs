using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Metriks.Service.Domain
{
    public class Weight
    {
        public WeightMeasurement Create(WeightMeasurement measurement)
        {
            if (measurement is null)
            {
                throw new ArgumentNullException(nameof(measurement));
            }

            if (measurement.Id == Guid.Empty)
            {
                measurement.Id = Guid.NewGuid();
            }

            return measurement;
        }
    }
}
