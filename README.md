# A Low-Cost Real-Time Multimodal Seizure Detection System Using MAX30102 and Accelerometry

[![Conference](https://img.shields.io/badge/Conference-ICACS_2026-blue.svg)](https://icacs.org/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-green.svg)](https://www.python.org/)
[![Arduino](https://img.shields.io/badge/Firmware-Arduino_C%2B%2B-orange.svg)](https://arduino.cc)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Presented at the **International Conference on Advanced Computing and Software (ICACS 2026)**.

---

## 👥 Authors
- **S Pavan Kumar**
- **A Vibhas Reddy** ([@VIBHAS777](https://github.com/VIBHAS777))
- **Hima Sagar B**
- **Meena Belwal**

---

## ⚡ Overview
Commercial clinical seizure alert systems are either cost-prohibitive (> $1,500) or generate pervasive false alarms whenever the patient engages in routine daily motion (walking, brushing teeth, gesturing).

This repository presents an open-source, low-power wearable seizure detection architecture costing under **$25 USD**. The device combines an **MPU6050 6-axis accelerometer/gyroscope** with a **MAX30102 photoplethysmography (PPG)** optical pulse oximeter. A novel **Physiological Threshold Fusion algorithm** evaluates dual-modal signals: requiring concurrent high-frequency convulsion variance and acute ictal tachycardia to confirm a seizure, suppressing over **91% of motion-induced false alarms**.

---

## 📁 Repository Structure
```
multimodal-seizure-detection-max30102/
├── firmware/
│   └── seizure_detector.ino   # Arduino / ESP32 C++ I2C sensor driver firmware
├── paper/
│   └── Low_Cost_Real_Time_Multimodal_Seizure_Detection_System_MAX30102.pdf
├── src/
│   └── fusion_engine.py       # Dual-threshold physiological signal fusion engine
├── main.py                    # Multi-scenario signal validation benchmark
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Quick Start
```bash
git clone https://github.com/VIBHAS777/multimodal-seizure-detection-max30102.git
cd multimodal-seizure-detection-max30102
python main.py
```

---

## 📜 Citation
```bibtex
@inproceedings{kumar2026seizuredetection,
  title={A Low-Cost Real-Time Multimodal Seizure Detection System Using MAX30102 and Accelerometry},
  author={Kumar, S Pavan and Reddy, A Vibhas and Sagar B, Hima and Belwal, Meena},
  booktitle={International Conference on Advanced Computing and Software (ICACS)},
  year={2026}
}
```
