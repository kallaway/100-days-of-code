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
        Domain.Weight _bizLogic;

        public WeightController()
        {
            _bizLogic = new Domain.Weight();
        }

        [HttpPost]
        [ProducesResponseType(StatusCodes.Status201Created)]
        [ProducesResponseType(StatusCodes.Status409Conflict)]
        public IActionResult Post([FromBody] WeightCreate value)
        {
            // Arrange
            var weightMeasurement = value.MapTo();

            // Act
            var bizResult = _bizLogic.Create(weightMeasurement);

            // Response
            WeightCreated responseResult = WeightCreated.MapFrom(bizResult.measurement);

            if (!bizResult.created)
            {
                return Conflict(responseResult);
            }

            return Created(AppendIdToCurrentPath(responseResult.Id.ToString()), responseResult);
        }

        [HttpGet]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public IActionResult Get()
        {
            // Arrange

            // Act
            var bizResult = _bizLogic.Read();

            // Response
            WeightList responseResult = WeightList.MapFrom(bizResult);

            return Ok(responseResult);
        }

        [HttpGet("{id}")]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public IActionResult Get(string id)
        {
            // Arrange
            if (!Guid.TryParse(id, out Guid properId))
            {
                return BadRequest("Expected the ID to be a UUID / GUID");
            }

            // Act
            var bizResult = _bizLogic.Read(properId);

            // Response
            WeightGet responseResult = WeightGet.MapFrom(bizResult);

            if (responseResult == null)
            {
                return NotFound();
            }

            return Ok(responseResult);
        }

        [HttpDelete("{id}")]
        [ProducesResponseType(StatusCodes.Status204NoContent)]
        public IActionResult Delete(string id)
        {
            // Arrange
            if (!Guid.TryParse(id, out Guid properId))
            {
                return BadRequest("Expected the ID to be a UUID / GUID");
            }

            // Act
            var result = _bizLogic.Delete(properId);

            // if the object was deleted, true is returned
            if (!result)
            {
                return NotFound();
            }

            return NoContent();
        }
    }
}
