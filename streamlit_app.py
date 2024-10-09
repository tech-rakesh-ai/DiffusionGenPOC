""" This scripts of code will use Hugging face's api to generate the images based on prompts """

import streamlit as st
import requests
import io
import time
from PIL import Image
import threading

# API Key from secrets
api_key = st.secrets['YOUR_HUGGING_FACE_API_TOKEN']

# Available models
# Available models
MODELS = {
    "Stable Diffusion 2.1": "stabilityai/stable-diffusion-2-1",
    "Stable Diffusion v1.5": "runwayml/stable-diffusion-v1-5",
    "Stable Diffusion XL": "stabilityai/stable-diffusion-xl-base-1.0",
    "Kandinsky 2.2": "kandinsky-community/kandinsky-2-2-decoder",
    "Stable Diffusion v1.4": "CompVis/stable-diffusion-v1-4"
}


headers = {"Authorization": f"Bearer {api_key}"}

# Global variable to control the generation process
cancel_generation = threading.Event()

def generate_image(model, prompt, num_inference_steps, guidance_scale, max_retries=5, initial_wait=50):
    API_URL = f"https://api-inference.huggingface.co/models/{model}"
    payload = {
        "inputs": prompt,
        "parameters": {
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale
        }
    }
    
    start_time = time.time()
    for attempt in range(max_retries):
        if cancel_generation.is_set():
            raise Exception("Image generation cancelled by user.")
        
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            try:
                image = Image.open(io.BytesIO(response.content))
                end_time = time.time()
                return image, end_time - start_time
            except Exception as e:
                raise Exception(f"Failed to process the image: {str(e)}. Response content: {response.content[:500]}...")
        
        elif response.status_code == 503:
            error_data = response.json()
            if "estimated_time" in error_data:
                wait_time = min(error_data["estimated_time"], 60)  # Cap wait time at 60 seconds
            else:
                wait_time = initial_wait * (2 ** attempt)  # Exponential backoff
            
            st.warning(f"Model is loading. Retrying in {wait_time:.1f} seconds... (Attempt {attempt + 1}/{max_retries})")
            time.sleep(wait_time)
        
        elif response.status_code == 500 and "Model too busy" in response.text:
            st.warning(f"Model is busy. Retrying in 30 seconds... (Attempt {attempt + 1}/{max_retries})")
            time.sleep(30)
        
        else:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
    
    raise Exception("Max retries reached. Unable to generate image.")

# Streamlit app
st.set_page_config(page_title="🖼️ Image Generation with Hugging Face Models", layout="wide")

st.title("🖼️ Image Generation with Diffusion Models")

# Sidebar for model selection and inputs
st.sidebar.header("Model Settings")
selected_model = st.sidebar.selectbox("Select a model:", list(MODELS.keys()))

# User input in sidebar
prompt = st.text_input("Enter your prompt:", "A beautiful sunset over the ocean")
num_inference_steps = st.sidebar.slider("Number of inference steps:", min_value=1, max_value=100, value=50)
guidance_scale = st.sidebar.slider("Guidance scale:", min_value=1.0, max_value=20.0, value=7.5, step=0.1)

# Generate button and Cancel button in the sidebar
col1, col2 = st.columns(2)
generate_button = col1.button("🔄 Generate Image")
cancel_button = col2.button("🛑 Cancel Generation")

if cancel_button:
    cancel_generation.set()
    st.warning("Cancelling image generation...")

if generate_button:
    try:
        cancel_generation.clear()  # Reset the cancel flag
        with st.spinner("Generating image..."):
            image, response_time = generate_image(MODELS[selected_model], prompt, num_inference_steps, guidance_scale)
        
        st.success(f"Image generated successfully. Response time: {response_time:.2f} seconds")
        
        st.image(image, caption="Generated Image", width=600)
        
        # Convert PIL Image to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        # Provide download button
        st.download_button(
            label="⬇️ Download Image",
            data=img_byte_arr,
            file_name="generated_image.png",
            mime="image/png"
        )
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("If the problem persists, please try a different model or check your API key.")
        st.error(f"API URL: https://api-inference.huggingface.co/models/{MODELS[selected_model]}")
        st.error(f"Headers (with token masked): {{'Authorization': 'Bearer ****' + headers['Authorization'][-4:]}}")

st.markdown("---")

