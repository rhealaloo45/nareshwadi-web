# nareshwadi-web: DairyTrack farm analytics

DairyTrack is the web dashboard of a cattle-management system built for Nareshwadi Learning Centre (June 2024 – June 2025). The landing page shows live temperature and humidity readings from farm sensors. A prediction page estimates a cow's daily milk production with a Random Forest model, and a third page lays out the planned disease-prediction screen.

The system's other web part is [milk_prod](https://github.com/rhealaloo45/milk_prod), the standalone milk-yield prediction service.

**Demo video of the app:** [watch on Google Drive](https://drive.google.com/file/d/11BQ3Qv-VxpQNHI4r4o9K69amzxmMTIhk/view)

## The wider system

The full system included a Random Forest that predicted disease and milk-yield trends from each cow's last 10 days of milk records, at 94% accuracy, along with 7-day milk production analytics. The training notebook and the evaluation behind the 94% figure are not in this repo. This repo is the Django dashboard.

## Pages

| URL | What it does |
|---|---|
| `/` | Landing page with two live charts, farm temperature and farm humidity, embedded from a ThingSpeak IoT channel (the last 60 readings, refreshed every 15 seconds) |
| `/milk` | Milk-production prediction. The form takes breed (HF cross, Jersey cross, Gir), age, health status, housing type, vaccinated and dewormed, and the page shows the predicted daily production in litres |
| `/disease` | Disease-prediction page: the input and output layout only, not yet connected to a model |

## How the prediction works

`app/views.py` loads `app/model/model.pkl` once at startup: a scikit-learn `RandomForestRegressor` (the same model file as in milk_prod). Each `/milk` submission is encoded by `app/forms.py` into the six features in training order (`Breed, Age, HealthStatus, HousingType, Vaccinated, Dewormed`), predicted, and shown on the same page. Errors appear on the page instead of crashing the request.

## Stack

Python, Django 4.1, scikit-learn 1.6.1, joblib, Bootstrap, ThingSpeak (IoT sensor charts). `settings.py` is set up for MongoDB through djongo.

## Run it locally

The model was pickled with scikit-learn 1.6.1, so install that exact version.

```bash
cd analytics
python -m venv .venv && source .venv/bin/activate
pip install "django>=4.1,<5" "scikit-learn==1.6.1" joblib numpy
```

`analytics/settings.py` points at a hosted MongoDB database through `djongo`. The pages don't read or write app data, so for local use you can switch `DATABASES` to SQLite:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

Then:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000 for the dashboard and http://127.0.0.1:8000/milk for the predictor.

## Project structure

```
analytics/
├── analytics/          Django settings and root URLs
├── app/
│   ├── views.py        landing, milk prediction, disease page
│   ├── forms.py        prediction inputs and their encodings
│   ├── utils.py        experimental 10-day LSTM helper (not wired up)
│   └── model/model.pkl trained RandomForestRegressor
├── templates/          landing page, prediction and disease pages
└── static/             CSS and images
```
