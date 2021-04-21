using Metriks.Service.RequestModels;
using Metriks.Service.ResponseModels;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Metriks.Service.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class WeightController : MetrikControllerBase
    {
        [HttpPost]
        [ProducesResponseType(StatusCodes.Status201Created)]
        public IActionResult Post([FromBody] WeightCreate value)
        {
            var result = new WeightCreated();
            result.Id = Guid.NewGuid();
            result.EntryDate = value.EntryDate;
            result.Unit = value.Unit;
            result.Weight= value.Weight;

            var uri = GetCurrentPathUri();
            uri.Path += "/" + result.Id;

            return Created(uri.Uri, result);
        }


    }
}
