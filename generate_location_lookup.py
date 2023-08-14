import pandas as pd
import os
import geopandas as gpd
from shapely.geometry import Polygon


def generate_location_lookup(old_csvs, new_csvs):
    location_dataframe = pd.read_csv(os.path.join(old_csvs, 'location_dataframe.csv'))
    location_lookup = pd.DataFrame({
        'location_id': location_dataframe['location_id'],
        'lat': location_dataframe['lat'],
        'lon': location_dataframe['lon'],
        'area': location_dataframe['total_area'],
        'lga': location_dataframe['lga'],
        'lat_min': location_dataframe['lat_min'],
        'lat_max': location_dataframe['lat_max'],
        'lon_min': location_dataframe['lon_min'],
        'lon_max': location_dataframe['lon_max']
    })

    location_lookup = remove_null_rows(location_lookup)
    location_lookup = remove_geographic_outliers(location_lookup)
    location_lookup = remove_null_areas(location_lookup)
    location_lookup = create_shapefile(location_lookup)
    location_lookup.to_csv(os.path.join(new_csvs, 'location_lookup.csv'), index=False)


def remove_null_rows(location_lookup):
    # Drops rows where coordinates are null i.e. the location has not been flown
    rows_to_drop = []
    for idx, row in location_lookup.iterrows():
        lat_lon_null = pd.isnull(row['lat']) and pd.isnull(row['lon'])
        lat_lon_zero = (row['lat'] == 0) and (row['lon'] == 0)
        lat_min_null = pd.isnull(row['lat_min'])
        if lat_lon_null or lat_lon_zero or lat_min_null:
            rows_to_drop.append(idx)
    return location_lookup.drop(index=rows_to_drop)


def remove_geographic_outliers(location_lookup):
    # Cycle through the latitude and longitude columns and search for coordinates outside NSW
    remove_indices = []
    for idx, row in location_lookup.iterrows():
        latitude_outside_nsw = (row['lat'] < -37.505768) or (row['lat'] > -28.156804)
        longitude_outside_nsw = (row['lon'] < 140.993300) or (row['lon'] > 153.638805)
        if latitude_outside_nsw or longitude_outside_nsw:
            remove_indices.append(idx)

    # Remove vague detections
    return location_lookup.drop(index=remove_indices)


def remove_null_areas(location_lookup):
    """Drops LGAs which have null area i.e. haven't been flown yet"""
    # First group by LGA and count the combined area flown in each
    area_by_lga = location_lookup.groupby("lga")["area"].count()
    # Then drop LGAs with 0 combined area counts
    lgas_to_drop = []
    for lga, area in area_by_lga.items():
        if area == 0:
            lgas_to_drop.append(lga)
    for lga in lgas_to_drop:
        location_lookup = location_lookup.drop(location_lookup[location_lookup.lga == lga].index)
    return location_lookup


def create_shapefile(location_lookup):
    survey_small = location_lookup.drop(columns=['lat', 'lon'])
    survey_small['survey_sites'] = survey_small.apply(
        lambda x: Polygon(zip(
            [x.lon_min, x.lon_max, x.lon_max, x.lon_min],
            [x.lat_min, x.lat_min, x.lat_max, x.lat_max])
        ), axis=1
    )
    survey_small = survey_small.drop(columns=['lon_min', 'lon_max', 'lat_min', 'lat_max'])
    survey_geoframe = gpd.GeoDataFrame(
        survey_small, geometry=survey_small.survey_sites, crs="EPSG:4326"
    )
    survey_geoframe.drop('survey_sites', axis=1, inplace=True)
    survey_geoframe.to_file(filename='shapefiles/locations.shp', driver="GeoJSON")
    return location_lookup.drop(columns=['lon_min', 'lon_max', 'lat_min', 'lat_max'])
