# Simple Face Recognition Desktop App

A simple desktop application for face recognition using Python. This app utilizes popular libraries such as `dlib` and `face_recognition` to detect and recognize faces in images.

## Technologies

- **Python**: The programming language used for the application.
- **dlib**: A toolkit for machine learning and computer vision tasks, used for face detection and recognition.
- **OpenCV**: A library for computer vision tasks, utilized here for image processing.
- **Pillow**: A Python Imaging Library (PIL) fork, used for opening, manipulating, and saving image files.
- **face_recognition**: A library built on `dlib` for face recognition.

## Setup Requirements

To set up the project, you need to install the following dependencies:

- `cmake==3.17.2`
- `dlib==19.18.0`
- `opencv-python==4.6.0.66`
- `Pillow==9.2.0`
- `face_recognition==1.3.0`

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/....
   cd ....
   ```

2. **Set up a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   Create a `requirements.txt` file with the following content:

   ```
   dlib==19.18.0
   opencv-python==4.6.0.66
   Pillow==9.2.0
   face_recognition==1.3.0
   ```

   Ensure `cmake` is installed on your system. You can download it from [CMake's official website](https://cmake.org/download/).

4. **Run the application**:

   ```bash
   python main.py
   ```

## Usage

1. **Load an image**: The app will prompt you to select an image file for processing.

2. **Face recognition**: The app will detect and recognize faces in the image and display the results.

3. **Save results**: Optionally, save the processed image with recognized faces annotated.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. Please make sure to follow the code style and include tests for new features.
