using Metriks.Service.Domain;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Metriks.Service.RequestModels
{
    public class WeightCreate
    {
        /// <summary>
        /// Date of the entry - when was the weight measurement taken
        /// </summary>
        public DateTime EntryDate { get; set; }

        /// <summary>
        /// The numeric representation of the weight
        /// </summary>
        public float Weight { get; set; }

        /// <summary>
        /// Unit of measurement: Ounces, Pounds, Tons, Gram, Kilogram, Tonne, Stone
        /// </summary>
        public string Unit { get; set; }

        public WeightMeasurement MapTo()
        {
            WeightMeasurement measurement = new WeightMeasurement();
            MapTo(measurement);
            return measurement;
        }
        public void MapTo(WeightMeasurement measurement)
        {
            measurement.EntryDate = this.EntryDate;
            measurement.Weight = this.Weight;
            measurement.Unit = this.Unit;
        }
    }
}
