"""
Serial Telemetry Stream Reader and Real-Time Seizure Monitor.
Connects to ESP32 / Arduino hardware via USB Serial COM port or virtual PTY.
"""

import json
import time
from typing import Optional, Callable
import numpy as np

from .fusion_engine import PhysiologicalThresholdFusion

class RealTimeSeizureMonitor:
    def __init__(
        self,
        port: Optional[str] = None,
        baudrate: int = 115200,
        window_size: int = 60,
        alert_callback: Optional[Callable[[dict], None]] = None
    ):
        self.port = port
        self.baudrate = baudrate
        self.window_size = window_size
        self.alert_callback = alert_callback
        self.fusion = PhysiologicalThresholdFusion(accel_var_thresh=3.2, hr_surge_thresh=115.0)

        self.accel_buffer = []
        self.hr_buffer = []

    def process_telemetry_packet(self, accel_mag: float, hr_bpm: float, spo2: float) -> dict:
        """
        Pushes latest physiological sample into sliding window buffer and evaluates fusion state.
        """
        self.accel_buffer.append(accel_mag)
        self.hr_buffer.append(hr_bpm)

        if len(self.accel_buffer) > self.window_size:
            self.accel_buffer.pop(0)
            self.hr_buffer.pop(0)

        result = self.fusion.detect_seizure(
            np.array(self.accel_buffer),
            np.array(self.hr_buffer)
        )
        result["current_spo2"] = spo2
        result["current_hr"] = hr_bpm
        result["current_accel"] = accel_mag

        if result["seizure_detected"] and self.alert_callback:
            self.alert_callback(result)

        return result
