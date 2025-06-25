
# 📡 LeakSense Simulator

Application that simulates environmental gas sensor readings, interprets air quality risk levels, logs data to a file, displays real-time status to the console, and triggers audio alerts for hazardous events.

---

## 🌍 Features

- 🔬 **Realistic Sensor Simulation**  
  MQ-2, MQ-3, and MQ-135 sensors simulate natural drift and random spikes in air quality levels.

- 🧠 **Risk Interpretation**  
  Values are evaluated using custom thresholds and classified as `CAUTION`, `HAZARDOUS`, or `CRITICAL`.

- 📝 **Structured Logging**  
  Logs are saved in a compact format ideal for long-term storage and easy parsing.

- 📺 **Real-Time Display**  
  Terminal output provides live sensor snapshots in a clean tabular view.

- 🔊 **Sound Alerts**  
  Plays specific sounds using `pygame` based on risk level (e.g., caution, hazardous, critical, spike).

---

## 📁 Project Structure

```
leaksense_simulator/
├── resources/
│   ├── log/
│   │   └── log.txt
│   └── sounds/
│       ├── caution_beep.mp3
│       ├── hazardous_beep.mp3
│       ├── critical_beep.mp3
│       └── spike_beep.mp3
├── main.py
├── sensor_sim.py
├── sensor_reader.py
├── sensor_parser.py
├── value_interpreter.py
├── display.py
├── log_handler.py
└── alarm_handler.py
```

---

## 🚀 Getting Started

### 1. Install dependencies

Make sure you have `pygame` installed:

```bash
pip install pygame
```

### 2. Run the simulator

```bash
python main.py
```

Sensor values will be simulated and:
- Displayed in the console
- Logged in `resources/log/log.txt`
- Trigger alerts via sound based on severity

---

## 📦 Requirements

- Python 3.7+
- `pygame` library
- OS that supports audio playback via `pygame`