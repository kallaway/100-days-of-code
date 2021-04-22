using Metriks.Domain.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Metriks.Service.ResponseModels
{
    public class WeightCreated
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

        public static WeightCreated MapFrom(WeightMeasurement weight)
        {
            WeightCreated result = new WeightCreated();
            result.EntryDate = weight.EntryDate;
            result.Id = weight.Id;
            result.Unit = weight.Unit;
            result.Weight = weight.Weight;

            return result;
        }
                
    }
}
