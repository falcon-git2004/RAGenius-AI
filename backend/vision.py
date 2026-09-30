from google import genai

from config import GEMINI_API_KEY



client = genai.Client(
    api_key=GEMINI_API_KEY
)



def analyze_image(image_bytes, prompt):


    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=[

            {
                "text": prompt
            },

            {
                "inline_data": {

                    "mime_type": "image/jpeg",

                    "data": image_bytes

                }

            }

        ]

    )


    return response.text