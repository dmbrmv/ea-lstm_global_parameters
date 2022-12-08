import pandas as pd
import geopandas as gpd


def create_gdf_for_plot(df: pd.DataFrame,
                        geom_df: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """[summary]

    Args:
        df ([type]): [description]
        geom_df ([type]): [description]

    Returns:
        [type]: [description]
    """
    pd.options.mode.chained_assignment = None  # type: ignore
    df['geometry'] = geom_df['centroids']
    df = gpd.GeoDataFrame(df)

    return df


def get_mae_prcp(gauge, differ_files, area_data):
    precip, prcp = differ_files[gauge][['precip', 'prcp']].groupby(
        pd.Grouper(freq='1Y')).sum().mean().values

    area = area_data.loc[gauge, 'ws_area']

    return (precip, prcp, area)
