using Metriks.Domain.Models;
using System;

namespace Metriks.Service.ResponseModels
{
    public class WeightGet
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

        public static WeightGet MapFrom(WeightMeasurement weight)
        {
            WeightGet result = new WeightGet();
            result.EntryDate = weight.EntryDate;
            result.Id = weight.Id;
            result.Unit = weight.Unit;
            result.Weight = weight.Weight;

            return result;
        }
    }
}
