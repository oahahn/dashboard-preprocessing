### Useful Tileset CLI Commands

This is how I uploaded the shapefiles for the survey sites:

``tilesets upload-source oahahn locations-GeoJSON-source shapefiles/locations-GeoJSON.shp``
``tilesets create oahahn.locations-tiles --recipe shapefiles/locations-recipe.json --name “locations tile”``
``tilesets publish oahahn.locations-tiles``

and this is how I uploaded the shapefiles for the NSW LGA's:
``tilesets upload-source oahahn nsw-lgas-GeoJSON-source nsw-lgas-GeoJSON.json``
``tilesets create oahahn.lgas-surveys-tiles --recipe lgas-locations-recipe.json --name “lgas locations tile”``
``tilesets publish oahahn.lgas-surveys-tiles``

Here are some other useful CLI commands:
``tilesets list-souces oahahn``
``tilesets delete-source oahahn locations-GeoJSON-source``
 