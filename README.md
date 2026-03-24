# 🌺 ColorSelectApp in Python

Year 2 individual project: An intelligent image analysis & color palette generation tool in Python created to help out graphic designers and artists. Implemented K-Means Clustering via Scikit-Learn to perform image quantization, extracting the top 5 dominant colors from any visual asset. Integrated a custom OpenCV-based pixel picker for real-time HEX code retrieval and managed a dynamic UI using Tkinter and Pillow.

## Features
- Dynamic Palette Generation: Uses Scikit-Learn’s K-Means algorithm to find the most representative colors in any uploaded image.
- Precision Color Picker: Click any pixel on the canvas to get its exact HEX value and see a live preview.
- Visual Feedback: Opens a secondary "pop-up" window (Toplevel) that displays the selected color as its background and shows the corresponding HEX code.
- Interactive UI: Built with Tkinter, featuring image thumbnails and a responsive layout.
- Clipboard Integration: Click color code to copy them instantly for use in design projects

<img width="2395" height="1390" alt="image" src="https://github.com/user-attachments/assets/7f64998f-ebef-4965-9faf-a9bf94552047" />
<img width="2386" height="1387" alt="image" src="https://github.com/user-attachments/assets/b17d19e1-1f4d-480e-87b7-3911217f724c" />




\* The code was written and run in VSCode (Windows 11) after creating a virtual environment
