# Multi-modal LLM Test-case Generator

## Overview

This project is a web application designed to generate test-case instructions using a Large Language Model (LLM). The application allows users to input context and upload images. The LLM processes the input and images to generate detailed test-case instructions, which are then displayed on the web interface.

## Project Structure

- `index.html`: The front-end HTML file that provides the user interface for interacting with the application.
- `main.py`: The back-end Flask application that handles user inputs, processes the images, invokes the LLM, and returns the generated instructions.

## Features

- **User Interface**: A clean and user-friendly chat interface that allows users to enter context and upload images.
- **Image Upload**: Supports image uploads with previews for single images.
- **LLM Integration**: Utilizes the LLaVA model to generate test-case instructions based on the provided context and images.
- **Dynamic Response Handling**: Displays the generated test-case instructions in a chat bubble format.

## Requirements

- Python 3.8 or higher
- Flask
- LangChain Community LLM
- PIL (Pillow)
- Other Python dependencies specified in `requirements.txt`

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Create a Virtual Environment**

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the dependencies**

    pip install -r requirements.txt

4.	**Download and set up the LLaVA model:**
Ensure that the LLaVA model is correctly set up and accessible by the application.
I am using ollama on my local computer and have LLaVA downloaded which is accessed using langchain.

## Running the Application 

1. **Start the Flask server**

    python main.py

2. Open your browser and go to http://127.0.0.1:5000 to access the web application.

Usage

	•	Enter the context for your test-case in the text input field.
	•	Upload images by clicking the “Upload” button. The selected images will be previewed.
	•	Click “Send” to submit the context and images.
	•	The application will display the generated test-case instructions as a chat bubble.

File Descriptions

	•	index.html: Contains the HTML and CSS for the user interface. It handles user interactions and displays the chat bubbles.
	•	main.py: Contains the Flask application logic. It processes user input, converts images to base64, interacts with the LLaVA model, and returns the response.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

	•	LangChain Community: For the LLaVA model integration.
	•	Pillow: For image processing.



