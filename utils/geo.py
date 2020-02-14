import math
import xarray as xr

# calculate area grid for summary stats
def calc_area(lat, pixeldegree):
    area_km2 = (110.45 * pixeldegree) * (111.1944 * pixeldegree) * math.cos(lat * (math.pi / 180.0))
    area_ha  = area_km2 * 100
    return area_ha

def create_area_grid(da, res=0.1):
    da_area = xr.zeros_like(da)
    da_area.attrs = {'long_name': 'area', 'units': 'ha'}
    da_area.name = 'area'
    for lat in da_area.lat.values:
        da_area.loc[{'lat': lat}] = calc_area(lat, res)
    return da_area
