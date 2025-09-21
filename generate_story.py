# ==============================================================================
# Hand Made - AI Artisan Story Generator
#
# Description:
# This script uses the Llava-1.5 vision-language model to generate a descriptive
# and heart-touching story about an artisan's work from an image.
# It's designed to help artisans who struggle with writing to create compelling
# blog content for their crafts.
#
# Author: Gemini (Google AI)
# Date: 21 September 2025
#
# To run this code:
# 1. Install the required libraries:
#    pip install transformers torch pillow requests accelerate bitsandbytes
#
# 2. Run the script from your terminal:
#    python generate_story.py
# ==============================================================================

import torch
import requests
from PIL import Image
from transformers import AutoProcessor, LlavaForConditionalGeneration
import os

def generate_artisan_story_from_image(image_source: str, prompt_text: str) -> str:
    """
    Generates a descriptive and heart-touching story for an artisan's work
    based on an image and a specific prompt.

    Args:
        image_source (str): The file path or URL to the image.
        prompt_text (str): The text prompt to guide the AI model.

    Returns:
        str: The generated text from the model, or an error message.
    """
    # --- 1. Load the AI Model and Processor ---
    # We use a 4-bit quantized version of Llava for memory efficiency.
    # This requires a compatible GPU (preferably NVIDIA with >8GB VRAM).
    model_id = "llava-hf/llava-1.5-7b-hf"
    
    print("Loading AI model... This may take a few moments.")
    try:
        model = LlavaForConditionalGeneration.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
            load_in_4bit=True,
        )
        processor = AutoProcessor.from_pretrained(model_id)
        print("✅ Model and processor loaded successfully.")
    except Exception as e:
        error_message = (
            f"❌ Error loading model: {e}\n"
            "This often happens if you don't have a compatible NVIDIA GPU or "
            "if the required drivers (CUDA) are not installed correctly. "
            "Consider running this on Google Colab."
        )
        print(error_message)
        return error_message

    # --- 2. Load and Prepare the Image ---
    try:
        if image_source.startswith(('http://', 'https://')):
            print(f"Downloading image from URL: {image_source}")
            raw_image = Image.open(requests.get(image_source, stream=True).raw).convert('RGB')
        elif os.path.exists(image_source):
            print(f"Loading image from local path: {image_source}")
            raw_image = Image.open(image_source).convert('RGB')
        else:
            raise FileNotFoundError("The specified local image path does not exist.")
    except Exception as e:
        error_message = f"❌ Error loading image: {e}"
        print(error_message)
        return error_message

    # --- 3. Prepare the Prompt for the Model ---
    # The Llava model expects a specific chat-like format.
    full_prompt = f"USER: <image>\n{prompt_text}\nASSISTANT:"
    print("\n📝 Preparing prompt for the AI...")

    # --- 4. Process Inputs and Generate Text ---
    # Move inputs to the GPU for processing.
    device = "cuda" if torch.cuda.is_available() else "cpu"
    inputs = processor(text=full_prompt, images=raw_image, return_tensors="pt").to(device)

    print("🧠 Generating story... Please wait.")
    
    try:
        # Generate text with parameters optimized for creative content.
        output = model.generate(
            **inputs,
            max_new_tokens=500,       # Max words to generate.
            do_sample=True,           # Enables more creative, less deterministic output.
            temperature=0.8,          # Controls creativity (higher is more random).
            top_p=0.9,                # Helps prevent nonsensical text.
        )
    except Exception as e:
        error_message = f"❌ Error during text generation: {e}"
        print(error_message)
        return error_message

    # --- 5. Decode and Clean the Result ---
    generated_text = processor.decode(output[0], skip_special_tokens=True)
    
    # Extract only the assistant's response from the full output.
    try:
        assistant_response = generated_text.split("ASSISTANT:")[-1].strip()
        return assistant_response
    except IndexError:
        return "Could not parse the model's response."

# ==============================================================================
# Main execution block
# This part of the script runs when you execute it directly.
# ==============================================================================
if __name__ == "__main__":
    
    # --- Your Custom Prompt ---
    # This guides the AI on what kind of text to generate.
    artisan_prompt = "generate descriptive texts that talk about the work of the artisans in detail and generate a heart touching story for the image"

    # --- Image Source ---
    # You can use a URL or a local file path.
    # An example URL is provided below. To use a local file, uncomment the second line
    # and replace "path/to/your/image.jpg" with the actual file path.
    image_source_url = "https://images.unsplash.com/photo-1542062700-94245c327248"
    # image_source_local = "path/to/your/image.jpg"
    
    # Generate the story using the URL.
    story = generate_artisan_story_from_image(image_source_url, artisan_prompt)

    # --- Print the Final Result ---
    if story:
        print("\n" + "="*50)
        print("✨ AI Generated Story ✨")
        print("="*50 + "\n")
        print(story)
        print("\n" + "="*50)