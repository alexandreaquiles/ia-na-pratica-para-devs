
import base64
import time
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """
Generate a Dragon Ball Z style version of the photo attached.
"""

result = client.images.edit(
    model="gpt-image-1",
    image=open("eu-gleice-cachoeira.jpg", "rb"),
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open(f"dragonball-{time.time_ns()}.png", "wb") as f:
    f.write(image_bytes)