# Django Weather Application - Setup Guide

A simple Django-based weather application that fetches and displays weather information for a given city using a third-party weather API (like OpenWeatherMap).

---

## Requirements

### 1. System Requirements

* Python 3.8+
* pip
* Virtualenv (recommended)
* Git (optional, for version control)

### 2. Python Packages

* Django
* requests (to make API calls)


### 3. External Services

* **OpenWeatherMap API** (Free tier)

  * Sign up at [https://openweathermap.org/api](https://openweathermap.org/api) and get your API key.

---

## Project Setup Steps

### Step 1: Set up the Project Environment

```bash
//clone the repo
git clone https://github.com/quiesscent/q-plp-weather-app

//navigate to folder
cd q-plp-weather-app/climate

//create virtual environment
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### Step 2: Install Required Packages
```bash
pip install -r requirements.txt
```

### Step 3: Run the Server
```bash
python manage.py runserver
```


## Author
[Ephesians Lewis](https://the-quiesscent-hub.vercel.app)
