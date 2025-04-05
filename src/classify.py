import geopandas as gpd
import pandas as pd
import os
import logging
from utils.duckdb import initialize, spatial_extension
from utils.geo import convert_geom
from utils.logging import get_logger


def classify_structures(shp_path: str, type_col: str, tdam_id: str) -> None:
    """Validate structures data set.
    
    Args:
        shp_path (str): path to shapefile containing buildings data
        type_col (str): the column that indicates the structure type
    
    Returns:
        None
    """
    logger = get_logger(__name__)

    logger.info(f"Buildings path exists: {os.path.exists(shp_path)}")
    bldgs_gdf = gpd.read_file(shp_path)
    bldgs_df = convert_geom(bldgs_gdf)
    conn = initialize()
    spatial_extension(conn)

    # come up with better way to create table from the shp path
    conn.execute(f"CREATE TABLE IF NOT EXISTS bldgs_{tdam_id} AS SELECT * FROM bldgs_df")

    # create a csv from this
    result = conn.sql(f"SELECT DISTINCT {type_col}, Null AS 'DamageIndicator' FROM bldgs_{tdam_id} ORDER BY {type_col} ASC").fetchall()
    result_df = pd.DataFrame(result, columns=['Type', 'DamageIndicator'])
    output_filename = f'structural_mappings_{tdam_id}.csv'
    if not tdam_id == 'test':
        result_df.to_csv(f'{os.getcwd()}/tables/{output_filename}', index=False)

    logger.info(f"Created file: {output_filename}")
    logger.info("Next steps are for you to go into the output file and map all of the structure types to Damage Indicators.")

if __name__ == "__main__":
    classify_structures("/Users/madelinejones/Working/repos/TDAM/data/dummy_bldgs.shp", type_col='Type', id = "123")
    