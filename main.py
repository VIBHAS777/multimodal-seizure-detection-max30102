import numpy as np
from src.fusion_engine import PhysiologicalThresholdFusion

def main():
    print("=" * 70)
    print("  Multimodal Seizure Detection: MAX30102 + Accelerometer Fusion")
    print("  Publication: ICACS 2026")
    print("=" * 70)

    engine = PhysiologicalThresholdFusion(accel_var_thresh=3.2, hr_surge_thresh=115.0)

    print("[*] Evaluating multimodal signal fusion on simulated patient telemetry scenarios:\n")

    # Scenario 1: Normal Resting State
    accel_normal = np.random.normal(1.0, 0.2, 50) # Gravity ~ 1.0g with minimal jitter
    hr_normal = np.random.normal(74.0, 3.0, 50)
    res_1 = engine.detect_seizure(accel_normal, hr_normal)
    print(f"  [1] Resting State      : Var={res_1['accel_var_thresh'] if 'accel_var_thresh' in res_1 else res_1['accel_variance']:<4} | HR={res_1['mean_hr_bpm']:>5.1f} BPM -> {res_1['status']}")

    # Scenario 2: Physical Exercise (Vigorous arm gestures without autonomic ictal pattern)
    accel_exercise = np.random.normal(2.5, 2.1, 50) # High variance
    hr_exercise = np.random.normal(95.0, 4.0, 50)    # Sub-threshold HR
    res_2 = engine.detect_seizure(accel_exercise, hr_exercise)
    print(f"  [2] Physical Gesturing : Var={res_2['accel_variance']:<4} | HR={res_2['mean_hr_bpm']:>5.1f} BPM -> {res_2['status']}")

    # Scenario 3: Real Tonic-Clonic Epileptic Seizure
    accel_ictal = np.random.normal(3.5, 2.6, 50)     # High frequency violent jerking
    hr_ictal = np.random.normal(138.0, 6.0, 50)      # Ictal tachycardia surge
    res_3 = engine.detect_seizure(accel_ictal, hr_ictal)
    print(f"  [3] Epileptic Episode  : Var={res_3['accel_variance']:<4} | HR={res_3['mean_hr_bpm']:>5.1f} BPM -> {res_3['status']}")

    print("\n" + "=" * 70)
    print("  HARDWARE PERFORMANCE SUMMARY (From Published Paper)")
    print("=" * 70)
    print("  Sensor Sampling Rate     : 20 Hz (Low Power Continuous Mode)")
    print("  Seizure Detection Latency: < 1.8 seconds from spasm onset")
    print("  False Positive Reduction : 91.3% reduction over accelerometer-only detectors")
    print("  Total Hardware BoM Cost  : Under $25 USD (Arduino Uno + MPU6050 + MAX30102)")
    print("=" * 70)

if __name__ == "__main__":
    main()
