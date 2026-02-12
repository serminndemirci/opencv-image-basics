# Image Processing Basics OpenCV
## Overview
This project demonstrates fundamental image processing operations using Python and OpenCV.  
It includes basic transformations such as resizing, cropping, pixel manipulation, and mirroring.The goal of this project is to understand how images are represented as matrices and how pixel-level operations work. 

### Project Structure

opencv-image-basics/

├── wall-e.py 

├── README.md



### Features
- Resize an image
- Crop using mouse selection (ROI)
- Center crop
- Pixel color modification
- Horizontal mirroring (flip)
- Add grayscale conversion
- Add edge detection (Canny)
- Add image filtering techniques
  
### Technologies Used
- Python
- OpenCV
- NumPy
  
## MiniProject Steps 
### Environment Setup (Anaconda Prompt)
1. Create a new conda environment:
   conda create -n wall-e python=3.10
2. Activate the environment:
   conda activate wall-e
3. Install required libraries:
   pip install opencv-python numpy
4. (Optional) Verify installation:
   python -c "import cv2; print(cv2.__version__)"
   
### Core Concepts

#### Image Representation
The image is downloaded dynamically from a URL when the script runs. ( using urllib.request )  
Digital images are stored as NumPy arrays.  
Each pixel contains intensity values in BGR (Blue, Green, Red) format.

---

#### Resizing
Resizing changes the spatial resolution of the image using interpolation techniques.Interpolation is a mathematical technique used to estimate new pixel values when resizing an image.

- Interpolation type significantly affects image quality.
- Interpolation types:

  - **INTER_NEAREST**
    - This is the fastest method
    - But it causes the pixelated photo
    - Detail loss is high

  - **INTER_LINEAR**
    - Balanced quality
    - Moderate speed
    - Most of the time is sufficient

  - **INTER_CUBIC**
    - More qualified
    - Smoother transitions
    - Slower

  - **INTER_AREA**
    - INTER_AREA is preferred for downscaling.
    - INTER_CUBIC provides smoother results for upscaling but is computationally heavier.

- Changing aspect ratio may distort object geometry.  
- Extreme resizing results in irreversible information loss.
- Interpolation make guess (doesn't add any real information)
  So;
  Expanding small picture doesn't mean making higher quality.

---

### Cropping (Region of Interest - ROI)  
Cropping extracts a selected region of the image using matrix slicing operations.    
ROI slicing follows NumPy indexing format (img[y1:y2, x1:x2]).    
Note that slicing order is (row, column) → (y, x).    
ROI slicing returns a view of the original image. Use .copy() if independent modification is required.  

---

### Pixel Manipulation
Pixel values can be directly modified by accessing specific matrix indices.

In OpenCV, images are stored as NumPy arrays in (height, width, channels) format. As I said in the previous part.   
Pixel indexing follows the order img[y, x], not img[x, y].  

Each pixel in a color image contains three values in BGR format (Blue, Green, Red), ranging from 0 to 255.  

Direct pixel manipulation is useful for:
- Region highlighting
- Mask creation
- Noise simulation
- Data augmentation experiments  

When modifying larger regions, slicing operations such as img[y1:y2, x1:x2] are more efficient than single-pixel updates.

---

### Image Flipping
Flipping mirrors the image along a specified axis (horizontal or vertical).

OpenCV provides the function:

cv2.flip(img, flipCode)

Where:
- flipCode = 0 → Vertical flip
- flipCode = 1 → Horizontal flip
- flipCode = -1 → Both axes

Flipping does not change the image resolution or aspect ratio.  
It only transforms spatial orientation.

This operation is commonly used for:
- Data augmentation in deep learning
- Symmetry analysis
- Visual transformations

---

### Grayscale Conversion
Converts a 3-channel color image into a single-channel intensity image.

This is done using:

cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

Grayscale conversion is not a simple average of RGB values.  
It uses a weighted transformation based on human visual perception:

Y = 0.299R + 0.587G + 0.114B

After conversion, the image shape changes from:
(height, width, 3)

to:
(height, width)

Grayscale images:
- Reduce computational cost
- Simplify feature extraction
- Are commonly used before edge detection or object detection

---

### Edge Detection (Canny)
Detects strong intensity gradients to highlight object boundaries.

Canny edge detection is applied as:

cv2.Canny(image, threshold1, threshold2)

The algorithm consists of multiple stages:
- Noise reduction (Gaussian blur)
- Gradient calculation
- Non-maximum suppression
- Double thresholding
- Edge tracking by hysteresis

Threshold parameters determine edge sensitivity:
- Lower values detect more edges (including noise)
- Higher values detect only strong edges

Canny edge detection is widely used in:
- Contour detection
- Shape analysis
- Object boundary extraction
- Classical computer vision pipelines
