import duckdb
import os

DAMAGE_INDICATORS_PATH = os.path.join(os.getcwd(), 'tables', 'damage_indicators.csv')
DAMAGE_MAPPINGS_PATH = os.path.join(os.getcwd(), 'tables', 'damage_mappings.csv')

def spatial_extension(conn: duckdb.DuckDBPyConnection):
    """Install spatial extension if needed.
    
    Args:
        conn (duckdb.DuckDBPyConnection): Connection to the database.

    Returns:
        conn (duckdb.DuckDBPyConnection): Connection to the database.
    """

    # Check if the spatial extension is installed
    try:
        conn.execute("LOAD SPATIAL;")
        print("Spatial extension is installed.")
    except duckdb.IOException:
        print("Spatial extension is NOT installed.")
        conn.install_extension("spatial")
    
    conn.load_extension("spatial")

    return conn


def initialize(rebuild_tables: bool = False):
    conn = duckdb.connect('tdam.db')
    create_tables(conn, rebuild_tables)
    return conn

def create_tables(conn: duckdb.DuckDBPyConnection, replace: bool = False):
    if replace:
        create_statement = "CREATE OR REPLACE TABLE"
    else:
        create_statement = "CREATE TABLE IF NOT EXISTS"
    conn.execute(f"{create_statement} damage_indicators AS SELECT * FROM read_csv('{DAMAGE_INDICATORS_PATH}')")
    conn.execute(f"{create_statement} damage_mappings AS SELECT * FROM read_csv('{DAMAGE_MAPPINGS_PATH}')")