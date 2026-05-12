-- Database & schema
CREATE DATABASE IF NOT EXISTS weather_db;
CREATE SCHEMA weather_db.weather_schema;
USE SCHEMA weather_db.weather_schema;

-- Storage integration (GCS)
CREATE STORAGE INTEGRATION gcs_weather_int ...;

-- Stage
CREATE STAGE weather_gcs_stage ...;

-- Raw table
CREATE TABLE raw_weather_gcs (raw_data VARIANT, ingested_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP());

-- Clean table
CREATE TABLE clean_weather (...);

-- Stream
CREATE STREAM raw_stream ON TABLE raw_weather_gcs;

-- Load task (every minute)
CREATE TASK load_new_files ... AS COPY INTO raw_weather_gcs ...;

-- Transform task
CREATE TASK transform_raw_to_clean ...;

-- Resume tasks
ALTER TASK load_new_files RESUME;
ALTER TASK transform_raw_to_clean RESUME;
