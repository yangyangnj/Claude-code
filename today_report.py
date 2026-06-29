"""Report today's time, date, and weather."""

import json
import urllib.request
from datetime import datetime


def report_datetime():
    """Print the current date and time."""
    now = datetime.now()
    print(f"Date:    {now.strftime('%A, %B %d, %Y')}")
    print(f"Time:    {now.strftime('%I:%M:%S %p')}")


def report_weather(city=""):
    """Fetch and print today's weather from wttr.in (no API key needed).

    Pass a city name (e.g. "London") or leave blank to auto-detect by IP.
    """
    url = f"https://wttr.in/{city}?format=j1"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.load(resp)
    except Exception as err:  # network error, bad city, service down, etc.
        print(f"Weather: unavailable ({err})")
        return

    current = data["current_condition"][0]
    area = data["nearest_area"][0]["areaName"][0]["value"]
    today = data["weather"][0]

    print(f"Location:{area}")
    print(f"Weather: {current['weatherDesc'][0]['value']}, "
          f"{current['temp_C']}°C ({current['temp_F']}°F)")
    print(f"         Feels like {current['FeelsLikeC']}°C, "
          f"humidity {current['humidity']}%")
    print(f"         High {today['maxtempC']}°C / Low {today['mintempC']}°C")


if __name__ == "__main__":
    import sys

    # Optional: pass a city as a command-line argument, e.g. `python today_report.py Tokyo`
    city = sys.argv[1] if len(sys.argv) > 1 else ""

    print("=" * 40)
    print("Today's Report")
    print("=" * 40)
    report_datetime()
    report_weather(city)
    print("=" * 40)
