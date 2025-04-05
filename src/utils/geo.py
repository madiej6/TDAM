import geopandas as gpd
import logging

def convert_geom(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Convert geometry column to WKT geometry.
    
    Args:
        gdf (GeoDataFrame): geodataframe to convert geometry column to WKT
    
    Returns:
        df (DataFrame): a geodataframe with the geometry column dropped, plus a new column named "geom_wkt"
    """

    gdf['geom_wkt'] = gdf.geometry.to_wkt()
    cols = list(gdf.columns)
    logging.info(cols)
    cols.remove('geometry')
    df = gdf[cols]


    return df
