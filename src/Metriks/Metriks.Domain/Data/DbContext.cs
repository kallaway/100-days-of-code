using Microsoft.Data.Sqlite;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace Metriks.Domain.Data
{
    public class DbContext
    {

        /// <summary>
        /// Initializes the database assumes nothing exists
        /// </summary>
        /// <returns></returns>
        public bool Init()
        {
            bool initSucceeded = true;

            RemoveExistingDatabaseAsNecessary();

            if (!IsDataSourceValid())
            {
                initSucceeded = false;
                throw new ApplicationException("SQLite data source could not be validated.");
            }

            var tableCommands = GetTableSchemaCommands();

            if (!ParseCommands(tableCommands))
            {
                initSucceeded = false;
                throw new ApplicationException("SQLite data source failed to create schema tables.");
            }

            return initSucceeded;
        }

        /// <summary>
        /// Gets the connection string. Will use the full path of the assembly for the database name.
        /// </summary>
        /// <returns>A valid connection string</returns>
        public static string GetConnectionString()
        {
            string dbPath = GetDatabaseFilePath();
            return $"Data Source={dbPath}";
        }

        /// <summary>
        /// Gets the path to the database. If in-memory is configured, this is where that is set.
        /// </summary>
        /// <returns>A path to the physical database file or :memory: for memory stores</returns>
        private static string GetDatabaseFilePath()
        {
            string _dbName = "test.db";  // ":memory:";

            var currentDirectory = System.IO.Directory.GetCurrentDirectory();
            var dbPath = Path.Combine(currentDirectory, _dbName);
            // dbPath = ":memory:" // In-Memory DB

            return dbPath;
        }

        /// <summary>
        /// Grabs table schemas from the embedded resources
        /// </summary>
        /// <returns></returns>
        private List<string> GetTableSchemaCommands()
        {
            var resourceName = "Metriks.Domain.Data.Schema.Tables.sql";
            var result = ParseResourceIntoCommands(resourceName);

            return result;
        }

        /// <summary>
        ///  Determines if the data source is valid by pulling the version from the database 
        /// </summary>
        /// <returns>True if the data source can be queried</returns>
        private bool IsDataSourceValid()
        {
            bool isValid = false;
            string cs = GetConnectionString(); ;
            string stm = "SELECT SQLITE_VERSION()";

            using (var con = new SqliteConnection(cs))
            {
                con.Open();

                using (var cmd = new SqliteCommand(stm, con))
                {
                    string version = cmd.ExecuteScalar().ToString();
                    Console.WriteLine($"SQLite version: {version}");
                    if (!string.IsNullOrWhiteSpace(version))
                    {
                        isValid = true;
                    }
                }
            }

            return isValid;
        }

        /// <summary>
        ///  Determines is the database file path matches the pattern for a in-memory store or a file
        /// </summary>
        /// <param name="databaseFilePath"></param>
        /// <returns></returns>
        private bool IsMemoryStore(string databaseFilePath)
        {
            return databaseFilePath.Equals(":memory:", StringComparison.InvariantCultureIgnoreCase);
        }

        /// <summary>
        /// Executes commands against the configured data store
        /// </summary>
        /// <param name="commands"></param>
        /// <returns></returns>
        private bool ParseCommands(List<string> commands)
        {
            bool successfullyExecutedCommands = true;
            string cs = GetConnectionString();

            using (var con = new SqliteConnection(cs))
            {
                con.Open();
                using (var cmd = new SqliteCommand(string.Empty, con))
                {
                    foreach (var command in commands)
                    {
                        cmd.CommandText = command;
                        try
                        {
                            int result = cmd.ExecuteNonQuery();

                        }
                        catch (Exception)
                        {
                            Console.WriteLine($"Failed to execute {command}");
                            successfullyExecutedCommands = false;
                        }
                    }
                }
            }

            return successfullyExecutedCommands;
        }

        /// <summary>
        /// Pulls the embedded resource from the assembly and parses out commands using GO as a seperator for commands
        /// </summary>
        /// <param name="resourceName"></param>
        /// <returns></returns>
        private List<string> ParseResourceIntoCommands(string resourceName)
        {
            var assembly = Assembly.GetExecutingAssembly();

            var result = new List<string>();

            using (Stream stream = assembly.GetManifestResourceStream(resourceName))
            {
                using (StreamReader reader = new StreamReader(stream))
                {
                    StringBuilder sb = new StringBuilder();
                    while (reader.Peek() > 0)
                    {
                        var line = reader.ReadLine();
                        if (line.Trim().ToUpper() != "GO")
                        {
                            if (!ShouldIgnoreLine(line))
                            {
                                sb.AppendLine(line.Trim());
                            }
                        }
                        else
                        {
                            result.Add(sb.ToString());
                            sb.Clear();
                        }
                    }

                    // Add any leftover lines where someone may have forgotten to add "GO" as a final seperator
                    // Ignore blank lines
                    if (sb.Length > 0)
                    {
                        result.Add(sb.ToString());
                    }
                }
            }

            return result;
        }

        /// <summary>
        /// If a file based database is being used, this will remove it.
        /// </summary>
        private void RemoveExistingDatabaseAsNecessary()
        {

            string dbFilePath = GetDatabaseFilePath();

            if (!IsMemoryStore(GetDatabaseFilePath()))
            {
                System.IO.File.Delete(dbFilePath);
            }
        }

        /// <summary>
        /// Determines if a line should be ignored.
        /// </summary>
        /// <param name="line">A line of SQL read out of an embedded resource</param>
        /// <returns></returns>
        private static bool ShouldIgnoreLine(string line)
        {
            bool shouldIgnore = false;

            if (line.StartsWith("--"))
            {
                shouldIgnore = true;
            }
            else if (string.IsNullOrWhiteSpace(line))
            {
                shouldIgnore = true;
            }

            return shouldIgnore;
        }
    }
}
