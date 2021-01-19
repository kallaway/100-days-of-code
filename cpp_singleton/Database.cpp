#include <iostream>
#include <string>

class Database
{
	protected:
		Database(const std::string db_id) : m_id(db_id) { };
		
		static Database* m_database;
		std::string m_id;

	public:
		
		/// Not cloneable
		Database(Database &other) = delete;

		/// Not assignable
		void operator=(const Database &) = delete;

		/// static method to control access to the singleton
		static Database *getInstance(const std::string& id);

		std::string value() const
		{
			return m_id;
		}
};

Database* Database::m_database = NULL;

Database* Database::getInstance(const std::string & id)
{
	if(m_database == NULL) 
	{
		m_database = new Database(id);
	}

	return m_database;
}

int main()
{
	Database* database = Database::getInstance("my_db");
	std::cout << database->value() << std::endl;

	Database* database2 = Database::getInstance("your_db");
	std::cout << database2->value() << std::endl;
}
