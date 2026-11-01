Real-Time QR Code Reader with Python and OpenCV

A simple real-time QR code reader developed using Python and OpenCV. The application uses a webcam to detect and decode QR codes, then displays the decoded information in the terminal.

About the Project

This project demonstrates how QR code detection and decoding can be implemented using Python and OpenCV.

The application captures live video from a webcam and continuously analyzes each frame using OpenCV's built-in QRCodeDetector.

When a QR code is detected, its content is decoded and printed in the terminal. A green rectangle is also drawn around the detected QR code.

The application runs continuously until the user presses the Q key.

Features
Real-time QR code detection.
QR code content decoding.
Webcam video processing.
Green rectangle around detected QR codes.
Duplicate detection output prevention.
Camera availability check.
Error handling.
Automatic camera resource cleanup.
Simple keyboard controls.
Technologies Used
Technology	Purpose
Python 3	Main programming language
OpenCV	Image processing and computer vision
QRCodeDetector	QR code detection and decoding
Webcam	Real-time video input
Requirements
Python 3.8 or newer
A working webcam
OpenCV library
Installation

Clone the repository:

bash
git clone https://github.com/Wotie1/qr-code-reader.git


Navigate to the project directory:

bash
cd qr-code-reader


Install the required library:

bash
pip install opencv-python

Usage

Run the application:

bash
python qr-reader.py


Show a QR code to your webcam.

When a QR code is detected, its decoded content will appear in the terminal.

To close the application, press Q.

How It Works
The application initializes the webcam.
OpenCV creates a QRCodeDetector object.
Video frames are captured continuously.
Each frame is analyzed for QR codes.
Detected QR codes are decoded.
The decoded information is printed in the terminal.
A green rectangle highlights the detected QR code.
The application exits when the user presses Q.
Limitations
Detection performance depends on camera quality and lighting.
Blurry or damaged QR codes may not be decoded correctly.
QR codes must be visible to the camera.
The application currently uses a single webcam.
QR code content is displayed as text and is not automatically validated.
Privacy and Security

The application processes camera frames locally.

It does not record or upload video footage.

QR code contents may include URLs or other sensitive information. Always verify decoded links before opening them.

Future Improvements

Possible future improvements include:

Support for multiple QR codes in one frame.
Saving decoded results to a text file.
Adding a graphical user interface.
Supporting image and video file input.
Displaying decoded content directly on the video window.
Adding QR code content validation.

These features are proposed improvements and are not necessarily included in the current version.

Contributing

Suggestions, bug reports, and improvements are welcome.

Feel free to open an issue or submit a pull request.

License

This project is intended to be released under the MIT License.

Include a LICENSE file in the repository before publishing under this license.

Author

YOUR NAME

GitHub: https://github.com/Wotie1