"""sensor-analytics: summarise a set of temperature sensor readings."""

import numpy as np

READINGS = [21.4, 22.0, 23.7, 25.1, 24.6, 23.2, 22.8, 26.3, 27.0, 25.4]


def summarise() -> dict:
    """Return the count, minimum, maximum and average of the readings."""
    values = np.array(READINGS)

    return {
        "count": int(values.size),
        "min_celsius": round(float(values.min()), 2),
        "max_celsius": round(float(values.max()), 2),
        "mean_celsius": round(float(values.mean()), 2),
    }


def main() -> None:
    """Print the summary to the terminal."""
    print("Sensor Analytics")
    print("-" * 28)
    for name, value in summarise().items():
        print(f"{name:<14} {value}")
