using Metriks.Domain.Models;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Metriks.Service.ResponseModels
{
    public class WeightList : MetrikList
    {
        public List<WeightGet> Weights { get; set; } = new List<WeightGet>();

        public static WeightList MapFrom(List<WeightMeasurement> weights)
        {
            WeightList result = new WeightList();
            foreach (var weight in weights)
            {
                result.Weights.Add(WeightGet.MapFrom(weight));
            }

            return result;
        }
    }
}
