"""Run the package with:  uv run python -m sensor_analytics

Going through Python avoids the small .exe launcher uv generates for the
sensor-analytics command, which Windows Smart App Control can block.
"""

from sensor_analytics import main

main()
