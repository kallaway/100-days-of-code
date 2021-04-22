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
            // Arrange
            var weightMeasurement = value.MapTo();

            // Act
            var bizLogic = new Domain.Weight();
            var bizResult = bizLogic.Create(weightMeasurement);

            // Response

            WeightCreated responseResult = WeightCreated.MapFrom(bizResult.measurement);

            if (bizResult.created)
            {
                return Created(AppendIdToCurrentPath(responseResult.Id.ToString()), responseResult);
            }
            else
            {
                return Conflict(responseResult);
            }

        }
    }
}
