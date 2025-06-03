# NEURAL-STYLE-TRANSFER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: REUBEN THOMAS JOHN

*INTERN ID*:CTO4DN1267

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEEKS

*MENTOR*: NEELA SANTOSH


---

## Project Description

This project is a simple yet visually powerful demonstration of applying artistic style to images using a technique called Neural Style Transfer. The goal is to combine the content of one image with the style of another, producing a unique stylized output.

The script uses pre-trained models from TensorFlow Hub to apply artistic filters to input images. It works by separating and recombining content and style representations of images using deep neural networks. This technique is fast, efficient, and easy to implement using Python libraries.

The script was developed as part of an internship at CodTech IT Solutions, and it serves as Task 3 in the internship’s deliverables.

---

## Technologies & Tools Used

Python 3.x

TensorFlow 2.x – for model loading and style transfer

TensorFlow Hub – for pre-trained neural style models

Matplotlib – for displaying and saving output images

Pillow – for image preprocessing

VS Code / Any Python IDE

Command Line Interface (CLI) – for running the script

PNG / JPEG Images – for input and output

---

## File Structure

Codtech IT Solutions/

│

├── Task-3/

│ ├── style_transfer.py # Main Python script

│ ├── content.jpg # Content image file

│ ├── style.jpg # Style image file

│ ├── output.png # Stylized output image

│ └── README.md # Project documentation (this file)

---

## How It Works

Input: The script reads content.jpg and style.jpg from the local directory.

Model Loading: A pre-trained TensorFlow Hub model is loaded for fast style transfer.

Processing: Both images are resized, converted to tensors, and passed into the model.

Style Transfer: The model generates a new image combining the content and style.

Output: The final image is saved as output.png and displayed using matplotlib.

---

## What I Did

Installed TensorFlow and TensorFlow Hub using pip.

Loaded content and style images using Pillow and preprocessed them.

Loaded and used the magenta/arbitrary-image-stylization-v1-256 model from TensorFlow Hub.

Wrote functions to handle image transformation and output generation.

Saved and viewed the styled image using matplotlib.

Verified the output by running the script in a virtual environment.

---

## What I Didn't Do (Yet)

No user input for image selection (file names are hard-coded).

No GUI or web interface (runs only on CLI).

Didn't use GPU acceleration for faster inference.

No batch processing or multi-style blending implemented.

---

## What I Learned

How to use TensorFlow Hub models for computer vision tasks.

Preprocessing and transforming images using TensorFlow and Pillow.

Working with neural networks for visual applications.

File handling and image saving with matplotlib.

Managing Python virtual environments and dependencies.

---

## Acknowledgments

Special thanks to CodTech IT Solutions for providing this opportunity. This project helped me understand the intersection of art and deep learning, and gave me hands-on experience with TensorFlow-based style transfer.

## OUTPUT

