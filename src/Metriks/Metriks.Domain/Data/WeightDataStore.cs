using Metriks.Domain.Common;
using Metriks.Domain.Models;
using Microsoft.Data.Sqlite;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.Domain.Data
{
    public class WeightDataStore : IDataStore<WeightMeasurement>
    {
        public bool Create(WeightMeasurement measurement)
         {
            bool result = false;
            var connString = DbContext.GetConnectionString();
            using (var con = new SqliteConnection(connString))
            {
                StringBuilder sb = new StringBuilder();
                sb.AppendLine("INSERT INTO WeightMeasurements ");
                sb.AppendLine("(id, entry_date, weight, unit) ");
                sb.AppendLine("SELECT @id, @entry_date, @weight, @unit");
                sb.AppendLine("WHERE NOT EXISTS (SELECT id FROM WeightMeasurements WHERE id=@id) ");


                con.Open();
                using (var cmd = new SqliteCommand(sb.ToString(), con))
                {
                    cmd.Parameters.Add(new SqliteParameter("@id", measurement.Id.ToString()));
                    cmd.Parameters.Add(new SqliteParameter("@entry_date", measurement.EntryDate.ToUnixTimeSeconds()));
                    cmd.Parameters.Add(new SqliteParameter("@weight", measurement.Weight));
                    cmd.Parameters.Add(new SqliteParameter("@unit", measurement.Unit));

                    var insertCount = cmd.ExecuteNonQuery();
                    if (insertCount > 0)
                    {
                        result = true;
                    }
                }
            }

            return result;
        }

        public bool Delete(string id)
        {
            throw new NotImplementedException();
        }

        public WeightMeasurement Read(string id)
        {
            throw new NotImplementedException();
        }

        public WeightMeasurement Update(WeightMeasurement measurement)
        {
            throw new NotImplementedException();
        }
    }

    public interface IDataStore<T>
    {
        bool Create(T measurement);

        T Read(string id);

        T Update(T measurement);

        bool Delete(string id);
    }
}
