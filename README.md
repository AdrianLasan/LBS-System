# Campus LBS

A minimal Location-Based Service (LBS) app using **Django + PostGIS + DRF + Leaflet**.

## Features
- PostGIS-backed spatial models (PointField, SRID 4326)
- REST API (DRF) with GeoJSON responses
- Spatial queries:
  1. Nearest N places to a coordinate
  2. Within-radius search
  3. Filter by category
- Responsive map UI (Leaflet + Bootstrap)

## Quickstart (Local, no Docker)
1. Install software: Python 3.10+, PostgreSQL 16, PostGIS 3, Git.
2. Create DB and enable PostGIS:
   ```sql
   CREATE DATABASE campus_lbs;
   \c campus_lbs
   CREATE EXTENSION postgis;
   ```
3. Copy `.env.example` to `.env` and adjust (DB user/pass as needed).
4. Create venv and install deps:
   ```bash
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r campus_lbs/requirements.txt
   ```
5. Apply migrations and load sample data:
   ```bash
   cd campus_lbs
   python manage.py migrate
   python manage.py loaddata fixtures.json
   python manage.py runserver
   ```
6. Open http://127.0.0.1:8000/ — pan the map, try buttons.

## Docker (Bonus)
```bash
cp .env.example .env
docker compose up --build
```
- App: http://localhost:8000/
- pgAdmin: http://localhost:5050/ (admin@example.com / admin)

## API
- `/api/places/` — list GeoJSON
- `/api/places/nearest/?lat=53.35&lng=-6.26&limit=10`
- `/api/places/within/?lat=53.35&lng=-6.26&km=0.5`

## Tech
- Django, DRF, DRF-GIS
- PostGIS
- Leaflet, Bootstrap

## Notes
- Timezone: Europe/Dublin
- SRID 4326 (WGS84)

## Why it worked before (Docker) and why it broke now

## Folder layout vs import paths
- 'places' and 'config' live under campus_lbs/, but code/      settings were written as if they were top-level ("places", "config").
- Django then couldn’t find the app’s migrations or the right settings module.

## GDAL not discoverable on Windows
- Without OSGeo4W (and PATH/GDAL_DATA/PROJ_LIB), django.contrib.gis raises:
“Could not find the GDAL library … Is GDAL installed?”

## Loading fixtures before migrating
- Running loaddata before the places tables exist causes:
relation "places_category" does not exist

## Multiple manage.py or wrong settings module
- DJANGO_SETTINGS_MODULE points to config.settings instead of campus_lbs.config.settings, Django uses the wrong project.
