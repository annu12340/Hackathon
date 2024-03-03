import base64
import os
import openai

def generate_new_image():
    print("hello") 
    openai.api_key = os.getenv("OPENAI_API_KEY")
    PROMPT = "Good morning message"

    # Make the API request
    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="256x256",
        response_format="b64_json",
    )


    image_data_b64 = response["data"][0]["b64_json"]
    # Decode base64-encoded image data
    image_data = base64.b64decode(image_data_b64)

    output_file_path = "output.png"

    with open(output_file_path, "wb") as f:
        f.write(image_data)

    print(f"Image saved to: {output_file_path}")
