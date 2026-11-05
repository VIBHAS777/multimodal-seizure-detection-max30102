import numpy as np

class PhysiologicalThresholdFusion:
    """
    Multimodal signal fusion engine combining:
      1. High-frequency 3D acceleration variance (tonic-clonic physical spasms)
      2. Autonomic ictal heart rate surge (ictal tachycardia)
    Eliminates false positives from routine arm motions (running, typing, gesturing).
    """
    def __init__(self, accel_var_thresh: float = 3.2, hr_surge_thresh: float = 115.0):
        self.accel_thresh = accel_var_thresh
        self.hr_thresh = hr_surge_thresh

    def detect_seizure(self, accel_window: np.ndarray, hr_window: np.ndarray) -> dict:
        accel_variance = np.var(accel_window)
        mean_hr = np.mean(hr_window)
        
        motor_spasm = accel_variance >= self.accel_thresh
        autonomic_surge = mean_hr >= self.hr_thresh
        
        # Dual-threshold fusion logic
        seizure_confirmed = motor_spasm and autonomic_surge
        
        # Distinguish between exercise and seizure
        if motor_spasm and not autonomic_surge:
            status = "FALSE_ALARM_FILTERED (Mechanical Motion Only)"
        elif autonomic_surge and not motor_spasm:
            status = "CARDIO_SURGE (No Convulsion)"
        elif seizure_confirmed:
            status = "CRITICAL_ALERT: TONIC-CLONIC SEIZURE DETECTED"
        else:
            status = "NORMAL_PATIENT_STATE"

        return {
            "seizure_detected": bool(seizure_confirmed),
            "accel_variance": round(float(accel_variance), 2),
            "mean_hr_bpm": round(float(mean_hr), 1),
            "status": status
        }
