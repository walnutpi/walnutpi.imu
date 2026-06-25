import os

class qma6100_:
    SYSFS_BASE = "/sys/kernel/qma6100p/device"
    _SYSFS_PATHS = [
        f"{SYSFS_BASE}/in_accel_x_input",
        f"{SYSFS_BASE}/in_accel_y_input",
        f"{SYSFS_BASE}/in_accel_z_input",
    ]

    def __init__(self):
        pass

    def is_available(self) -> bool:
        return os.path.exists(self._SYSFS_PATHS[0])

    def read(self) -> list[float]:
        values = []
        for path in self._SYSFS_PATHS:
            with open(path, "r") as f:
                raw = int(f.read().strip())
                values.append(raw / 1000.0)
        return values
