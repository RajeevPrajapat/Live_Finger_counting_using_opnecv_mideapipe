# 🖐️ Real-Time Finger Counting with OpenCV and MediaPipe

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green) ![MediaPipe](https://img.shields.io/badge/MediaPipe-0.9%2B-orange)

## files
- ✅ Shows the **total finger count** in first cell, **decation of the finger name , count**  in cell second both in **code.ipynb**- 
- ✅ Shows the **decation of the finger name , count** in **finger_count_code.py**
- TO run the code **python finger_count_code.py** ,In the **Terminal** 
- To stop press key **q**

## 🚀 Project Overview
This project uses **OpenCV** and **MediaPipe** to detect and count fingers in real-time. It supports:
- 🎯 **Both-hand detection** with finger counting.
- ✋ **Accurate individual and total finger count**.
---

## ⚙️ Features
✅ Real-time hand tracking with accurate finger counting.  
✅ Displays individual finger count for **left** and **right** hands.  
✅ Shows the **total finger count**, **Name of the finder decation**   

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries:**  
  - `OpenCV` → For real-time video processing.  
  - `MediaPipe` → For hand detection and finger tracking.  


---

## 📝 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Armanlaliwala/Real-Time-Finger-Counting-with-OpenCV-and-MediaPipe.git
cd Real-Time-Finger-Counting-with-OpenCV-and-MediaPipe
```

### 2. Create a virtual environment
#### Windows:
**python version must between 3.8 TO 3.10 because the mideapipe support by this version**
"For python version check **python --version** " 
```bash
python -m venv env
env\Scripts\activate
```
#### Linux/Mac:
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---


---

## 🔥 Code Explanation

### 🛠️ Finger Counting Logic
**Thumb Detection:**
- For **left hand**, thumb is open when `tip_x > base_x`.
- For **right hand**, thumb is open when `tip_x < base_x`.




## 📸 Demo
✅ Real-time finger counting with both hands:

---

## 🙌 Acknowledgments
- **OpenCV** → For real-time video processing.
- **MediaPipe** → For hand and finger landmark detection.

---

🔥 This README is clean, well-structured, and GitHub-ready! 🚀 Let me know if you want any modifications. 🎯

