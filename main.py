from flask import Flask, render_template_string, request, jsonify
from langchain_community.llms import Ollama
from PIL import Image
import base64
from io import BytesIO

llm = Ollama(model="llava:latest")

app = Flask(__name__)

# Load the HTML content from 'index.html'
with open('index.html', 'r') as f:
    html_content = f.read()

def convert_to_base64(pil_image: Image):
    """Convert a PIL image to a base64 string."""
    buffered = BytesIO()
    pil_image.save(buffered, format=pil_image.format)
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

@app.route('/')
def index():
    # Render the HTML page with empty instructions initially
    return render_template_string(html_content, instructions="")

@app.route('/generate', methods=['POST'])
def generate_instructions():
    # Get the user's message (context) from the form
    context = request.form.get('context', '')

    # Get the images from the form
    files = request.files.getlist('images')

    # Convert each image to a base64 string using PIL
    image_prompts = []
    for file in files:
        # Open the uploaded image file
        pil_image = Image.open(file)
        
        # Convert the image to base64
        image_b64 = convert_to_base64(pil_image)
        
        # Append the base64 image string to the list
        image_prompts.append(image_b64)

    # Combine the context and base64 images for the prompt
    full_prompt = f"You are an AI assistant that describes testing instructions for any digital product's features, based on the screenshot provided. \n \n The output should describe these follwoing fields: \n TEST CASE- \n Description: What the test case is about. \n Pre-conditions: What needs to be set up or ensured before testing. \n Testing Steps: Clear, step-by-step instructions on how to perform the test. \n Expected Result: What should happen if the feature works correctly. \n \n Context: {context}"

    # Invoke the LLaVA model with the base64-encoded images
    instructions = llm.invoke(full_prompt, images=image_prompts)

    # Return the result as JSON for the front-end to handle dynamically
    return jsonify({"response": instructions})

if __name__ == '__main__':
    app.run(debug=True)