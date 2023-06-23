### Useful Tileset CLI Commands

This is how I uploaded the shapefiles for the survey sites:

``tilesets upload-source oahahn locations-GeoJSON-source shapefiles/locations-GeoJSON.shp``
``tilesets create oahahn.locations-tiles --recipe shapefiles/locations-recipe.json --name "locations tile"``
``tilesets publish oahahn.locations-tiles``

and this is how I uploaded the shapefiles for the NSW LGA's:
``tilesets upload-source ohahn nsw-lgas-source shapefiles/nsw-lga-boundaries.json``
``tilesets create ohahn.lgas-tile --recipe shapefiles/lgas-recipe.json --name "lgas tile"``
``tilesets publish ohahn.lgas-tile``

Here are some other useful CLI commands:
``tilesets list-souces oahahn``
``tilesets delete-source oahahn locations-GeoJSON-source``

Here is how you set the access token:
``export MAPBOX_ACCESS_TOKEN=sk.eyJ1Ijoib2hhaG4iLCJhIjoiY2xqNzJnbHh3MG0yNjNlbHdhNDBqd2k4diJ9.d0M1vHgS4VuvGoyVNW1azQ``
 
This is the token for tileset-lrw on ohahn