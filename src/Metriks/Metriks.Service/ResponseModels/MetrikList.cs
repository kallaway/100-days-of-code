namespace Metriks.Service.ResponseModels
{
    public class MetrikList
    {
        public string NextPageToken { get; set; } = string.Empty;

        public int PageSize { get; set; }

    }
}