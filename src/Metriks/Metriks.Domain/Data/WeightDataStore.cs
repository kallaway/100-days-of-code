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
    public class WeightDataStore : ISimpleDataStore<WeightMeasurement>
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

        public bool Delete(Guid id)
        {
            throw new NotImplementedException();
        }

        public WeightMeasurement Read(Guid id)
        {
            WeightMeasurement result = null;

            var connString = DbContext.GetConnectionString();
            using (var con = new SqliteConnection(connString))
            {
                StringBuilder sb = new StringBuilder();
                sb.AppendLine("SELECT id, entry_date, weight, unit");
                sb.AppendLine("FROM WeightMeasurements ");
                sb.AppendLine("WHERE id=@id ");

                con.Open();
                using (var cmd = new SqliteCommand(sb.ToString(), con))
                {
                    cmd.Parameters.Add(new SqliteParameter("@id", id.ToString()));

                    using (var dr = cmd.ExecuteReader(System.Data.CommandBehavior.SingleRow))
                    {
                        while (dr.Read())
                        {
                            result = new WeightMeasurement();
                            result.Id = Guid.Parse((string)dr["id"]);
                            result.EntryDate = new DateTime(1970, 1, 1, 0, 0, 0).AddSeconds((long)dr["entry_date"]);
                            result.Weight = (double)dr["weight"];
                            result.Unit = (string)dr["unit"];                            
                        }
                    }
                }
            }

            return result;
        }

        public List<WeightMeasurement> Read()
        {
            var result = new List<WeightMeasurement>();

            var connString = DbContext.GetConnectionString();
            using (var con = new SqliteConnection(connString))
            {
                StringBuilder sb = new StringBuilder();
                sb.AppendLine("SELECT id, entry_date, weight, unit");
                sb.AppendLine("FROM WeightMeasurements ");

                con.Open();
                using (var cmd = new SqliteCommand(sb.ToString(), con))
                {
                    using (var dr = cmd.ExecuteReader())
                    {
                        while (dr.Read())
                        {
                            var measurement = new WeightMeasurement();
                            measurement.Id = Guid.Parse((string)dr["id"]);
                            measurement.EntryDate = new DateTime(1970, 1, 1, 0, 0, 0).AddSeconds((long)dr["entry_date"]);
                            measurement.Weight = (double)dr["weight"];
                            measurement.Unit = (string)dr["unit"];

                            result.Add(measurement);
                        }
                    }
                }
            }

            return result;
        }

        public WeightMeasurement Update(WeightMeasurement measurement)
        {
            throw new NotImplementedException();
        }
    }
}
