using System;
using System.Collections.Generic;

namespace Metriks.Domain.Data
{
    public interface ISimpleDataStore<T>
    {
        bool Create(T measurement);

        T Read(Guid id);

        List<T> Read();

        T Update(T measurement);

        bool Delete(Guid id);
    }
}
