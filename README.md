# 🖼️ A PIC: Image Generation Using Diffusion Models

This project is a **Streamlit** application that generates images from text prompts using **Hugging Face's** powerful text-to-image models, such as Stable Diffusion. The app allows users to select different models, input text prompts, and customize inference parameters like the number of steps and guidance scale.

## 🚀 Features
- Generate images from text prompts using multiple models from Hugging Face.
- Customizable parameters including:
  - Number of inference steps.
  - Guidance scale.
- Easy-to-use interface powered by Streamlit.
- Supports multiple state-of-the-art image generation models, including Stable Diffusion.

## 🖥️ Demo

The app generates an image based on the user's input prompt. Here's an example:

```bash
A beautiful sunset over the ocean
```

The app will return an image based on the prompt using the selected model.

## 📦 Models Available

| Model Name                  | Hugging Face Path                              | Description |
|------------------------------|-----------------------------------------------|-------------|
| Stable Diffusion v1.5         | `runwayml/stable-diffusion-v1-5`              | A widely used model for high-quality image generation from text. |
| Stable Diffusion 2.1          | `stabilityai/stable-diffusion-2-1`            | An improved version of Stable Diffusion with better quality. |
| Stable Diffusion XL           | `stabilityai/stable-diffusion-xl-base-1.0`    | A larger and more powerful version of Stable Diffusion. |
| Kandinsky 2.2                 | `kandinsky-community/kandinsky-2-2-decoder`   | A high-quality model for artistic image generation. |
| Stable Diffusion v1.4         | `CompVis/stable-diffusion-v1-4`               | An earlier version of Stable Diffusion. |
| Nvidia NVLM-D-72B             | `nvidia/NVLM-D-72B`                           | **(Experimental)**: Nvidia's model, though not primarily designed for text-to-image tasks. |

## 🛠️ Setup and Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/tech-rakesh-ai/DiffusionGenPOC.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your Hugging Face API key in **Streamlit secrets**. In the `.streamlit/secrets.toml` file:
   ```toml
   [default]
   YOUR_HUGGING_FACE_API_TOKEN = "your_api_key_here"
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 🌟 Usage

1. Once the app is running, open the web browser to the local URL shown in your terminal.
2. Enter your text prompt in the provided input box.
3. Select the model you want to use from the dropdown.
4. Adjust the number of inference steps and guidance scale using the sliders.
5. Click **Generate Image** to start the process.
6. The generated image will be displayed, and you can download it in PNG format.

### Example Input:
- **Prompt**: `A futuristic cityscape with flying cars.`
- **Model**: `Stable Diffusion v1.5`
- **Inference Steps**: `50`
- **Guidance Scale**: `7.5`

### Example Output:
The app will display the generated image along with response time and a download button.

## 🔧 Parameters Explained

- **Model**: The text-to-image model from Hugging Face to be used for generation.
- **Prompt**: A textual description based on which the image will be generated.
- **Inference Steps**: Number of steps to use during the inference process. More steps may result in higher quality but take more time.
- **Guidance Scale**: A parameter to control how strongly the model follows the prompt. Higher values make the image more aligned with the prompt but may reduce creativity.

## 🛑 Canceling Image Generation

If the image generation takes too long or if you wish to cancel the process, you can click the **Cancel Generation** button in the app to stop the process.

## ⚠️ Troubleshooting

- If you encounter issues with a specific model, try switching to a different one.
- Make sure that your Hugging Face API key has sufficient access to the models you're using.
- For API errors, check the logs and ensure your token is valid.

## 🤝 Contributions

Feel free to fork this repository and create pull requests for any improvements or bug fixes. Suggestions are always welcome!

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
