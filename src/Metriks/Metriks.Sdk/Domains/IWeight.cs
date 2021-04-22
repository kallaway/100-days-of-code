﻿using Metriks.Sdk.ResponseModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.Sdk.Domains
{
    public interface IWeight
    {
        List<WeightGet> GetWeight();

        Task<List<WeightGet>> GetWeightAsync();
    }
}
