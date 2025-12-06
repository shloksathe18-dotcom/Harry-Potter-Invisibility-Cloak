# 🧙‍♂️ Harry Potter Invisibility Cloak

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Ever wanted to disappear like Harry Potter? Now you can! ✨**

This project uses computer vision to create a real-time invisibility cloak effect. Wear something red, and watch yourself vanish into thin air!

[Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [How It Works](#-how-it-works)

</div>

---

## 🎬 Demo

Wrap yourself in a red cloth and become invisible in real-time! This project demonstrates the power of computer vision and color detection using OpenCV.

## ✨ Features

- 🎥 **Real-time Processing** - Instant invisibility effect with your webcam
- 🎨 **Smart Color Detection** - Advanced HSV color space detection for accurate red tracking
- 🔄 **Two Modes Available** - Static background or looping video background
- 🪄 **Smooth Masking** - Morphological operations for clean, professional results
- 🎯 **Easy to Use** - Just run and wear something red!

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/shloksathe18-dotcom/Harry-Potter-Invisibility-Cloak.git
cd Harry-Potter-Invisibility-Cloak

# Install required packages
pip install opencv-python numpy
```

### Usage

**Option 1: Auto Background Capture (Easiest)**
```bash
python invisibility_cloak.py
```
1. Run the script
2. Move away from camera for 3 seconds
3. Wear something RED
4. Watch the magic happen! ✨
5. Press 'q' to quit

**Option 2: Video Background**
```bash
# Step 1: Record your background
python record_background.py

# Step 2: Run the cloak effect
python invisibility_cloak_video.py
```

## 🔬 How It Works

This project uses computer vision techniques to create the invisibility effect:

1. **Background Capture** - Captures a clean background frame without you
2. **Color Detection** - Detects red color using HSV color space (better than RGB!)
3. **Mask Creation** - Creates a binary mask of the red regions
4. **Morphological Operations** - Cleans up noise and smooths the mask edges
5. **Image Segmentation** - Separates cloak area from the rest of the frame
6. **Background Replacement** - Replaces red regions with the background
7. **Real-time Display** - Shows the final result at 30+ FPS

### Why HSV Color Space?

HSV (Hue, Saturation, Value) is more robust than RGB for color detection because:
- Separates color information from lighting
- More intuitive for defining color ranges
- Better performance in varying lighting conditions

### The Magic Formula

```python
# Detect red color (wraps around in HSV)
lower_red1 = [0, 120, 70]    # Lower red range
upper_red1 = [10, 255, 255]
lower_red2 = [170, 120, 70]  # Upper red range
upper_red2 = [180, 255, 255]

# Combine masks
mask = mask1 + mask2

# Replace cloak with background
final = (background & mask) + (frame & ~mask)
```

## 🎓 Educational Purpose

This project is perfect for learning:
- **Computer Vision** - Real-world application of image processing
- **Color Spaces** - Understanding HSV vs RGB
- **Masking Techniques** - Binary masks and bitwise operations
- **Morphological Operations** - Erosion, dilation, opening, closing
- **Real-time Processing** - Optimizing for live video streams
- **OpenCV Library** - Practical hands-on experience

## 🎮 Fun Applications

- 🎪 Magic shows and performances
- 🎬 Video effects and content creation
- 🎓 Computer vision demonstrations
- 🎉 Party tricks and entertainment
- 📚 Educational workshops

## 💡 Tips for Best Results

- ✅ Use a **solid red cloth** (no patterns)
- ✅ Ensure **good, even lighting**
- ✅ Keep the **background static** during capture
- ✅ Avoid red objects in the background
- ✅ Try different red shades if detection fails

## 🛠️ Troubleshooting

**Cloak not detected?**
- Adjust HSV values in the code
- Ensure proper lighting
- Try a brighter/darker red cloth

**Flickering effect?**
- Increase morphological operation iterations
- Use a more uniform red cloth
- Improve lighting conditions

## 📁 Project Structure

```
Harry-Potter-Invisibility-Cloak/
├── invisibility_cloak.py          # Main program (auto background)
├── invisibility_cloak_video.py    # Video background version
├── record_background.py           # Background video recorder
└── README.md                      # You are here!
```

## 🔧 Requirements

- Python 3.7+
- OpenCV (cv2)
- NumPy
- Webcam

## 📝 License

This project is open source and available for educational and fun purposes.

## 👨‍💻 Author

**Shlok Sathe**

- GitHub: [@shloksathe18-dotcom](https://github.com/shloksathe18-dotcom)
- Project: [Harry Potter Invisibility Cloak](https://github.com/shloksathe18-dotcom/Harry-Potter-Invisibility-Cloak)

## 🌟 Show Your Support

If you found this project fun or educational, give it a ⭐️!

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📚 Learn More

Want to dive deeper into computer vision?
- [OpenCV Documentation](https://docs.opencv.org/)
- [Color Spaces in OpenCV](https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html)
- [Image Processing Basics](https://docs.opencv.org/master/d2/d96/tutorial_py_table_of_contents_imgproc.html)

---

<div align="center">

**Made with ❤️ for fun and education**

*Mischief Managed!* 🪄

</div>
