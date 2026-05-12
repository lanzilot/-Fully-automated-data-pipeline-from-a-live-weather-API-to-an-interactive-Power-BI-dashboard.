## Production‑ready, fully automated data pipeline from a live weather API to an interactive Power BI dashboard

    Extract -fetches live weather from Open‑Meteo (free, no API key) every 5 minutes
    Load -JSON files uploaded to Google Cloud Storage (GCS) bucket
    Ingest - Snowflake’s external stage + scheduled task (or Snowpipe) loads raw JSON into a VARIANT table
    Transform - Stream + Task incrementally flattens JSON into a relational CLEAN_WEATHER table (handles duplicates, casts is_day correctly)
    Automate - Two Snowflake tasks run every minute – one loads new files, the other transforms new rows
    Visualise - Power BI connects via DirectQuery to CLEAN_WEATHER. Live dashboard shows latest temperature (KPI) and historical trend

