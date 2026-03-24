# 🌺"Detecting Color in an Image" - Python Application

This is an interactive Python application that allows users to detect and identify colors within an image by clicking on a specific pixel.
It is designed to simplify the process of color identification for graphic designers, artists, and developers.

## 🛠️ Technologies Used
The project is built using Python and the following key libraries:
- **`Tkinter`**: The standard Python library for creating the Graphical User Interface (GUI), managing the main window, and handling click events.
- **`Pillow (PIL)`**: Used for image processing, allowing the application to open image files, convert them to RGB format, and extract pixel color data.

## 🚀 Features
- **Interactive Image Display**: The selected image is loaded and displayed on a Canvas widget at its original size.
- **Pixel Color Detection**: The application captures the coordinates of the mouse click and extracts the RGB values of that specific pixel.
- **Hexadecimal Conversion**: Automatically converts RGB color values into HEX format using string formatting.
- **Visual Feedback**: Opens a secondary "pop-up" window (Toplevel) that displays the selected color as its background and shows the corresponding HEX code.

## 📂 Code Logic
1. **Event Binding**: The `<Button-1>` event (left mouse click) is linked to the `show_color` function.
2. **Color Extraction**: The `getpixel` function from Pillow is used to retrieve RGB data.
3. **GUI Management**: `Toplevel` windows are generated dynamically to provide immediate visual results for each selection.

## 🎨 How to use
1. To run this application, you need to have Python installed on your computer along with the Pillow library. You can install the required library by opening your terminal or command prompt and typing `pip install Pillow`
2. Download the `proiect.py` file and the image you want to use (for example, `crin.jpg`) into the same folder. Open the Python script and ensure the image_path variable matches your filename.
3. Run the script and click on a pixel in the pop-up window.
