from builder import create_complex
from exporter import RedisMapMonitor

my_map = create_complex(width=20, height=8)
# paint_all(my_map)

monitor = RedisMapMonitor(my_map)
monitor.export_map()