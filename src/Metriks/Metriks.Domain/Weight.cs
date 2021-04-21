using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Metriks.Domain.Models;
using Microsoft.Data.Sqlite;

namespace Metriks.Domain
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

            WriteToDatabase(measurement);

            return measurement;
        }

        public void WriteToDatabase(WeightMeasurement measurement)
        {
            string cs = "Data Source=:memory:";
            string stm = "SELECT SQLITE_VERSION()";

            using var con = new SqliteConnection(cs);
            con.Open();

            using var cmd = new SqliteCommand(stm, con);
            string version = cmd.ExecuteScalar().ToString();

            Console.WriteLine($"SQLite version: {version}");
            throw new NotImplementedException("Write logic for initiating the database and then writing to it!");
        }
    }
}
