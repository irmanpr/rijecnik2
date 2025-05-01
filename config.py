import urllib.parse

# Database connection string
SERVER = "irman"
DATABASE = "RIJECNIK"
USERNAME = "sa"
PASSWORD = "bismillah"

# Encode password if necessary
params = urllib.parse.quote_plus(f"DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}")

SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQL Server Connection
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=sqlse-irman-dev-001.database.windows.net;"
    "Database=sql-irman-dev-da-dw-001;"
    "Uid=irman;"
    "Pwd=Banjaluka!99;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=90;"
)

