using Metriks.Sdk.Domains.Models;
using System;

namespace Metriks.Sdk.Domains.Clients.ResponseModels
{
    internal class WeightGet
    {
        /// <summary>
        /// Unique ID of the weight metric
        /// </summary>
        public Guid Id { get; set; }

        /// <summary>
        /// Date of the entry - when was the weight measurement taken
        /// </summary>
        public DateTime EntryDate { get; set; }

        /// <summary>
        /// The numeric representation of the weight
        /// </summary>
        public double Weight { get; set; }

        /// <summary>
        /// Unit of measurement: Ounces, Pounds, Tons, Gram, Kilogram, Tonne, Stone
        /// </summary>
        public string Unit { get; set; }

        public WeightMeasurement MapTo()
        {
            var result = new WeightMeasurement();
            result.EntryDate = this.EntryDate;
            result.Id = this.Id;
            result.Unit = this.Unit;
            result.Weight = this.Weight;

            return result;
        }
    }
}
