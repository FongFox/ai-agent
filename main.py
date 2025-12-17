import argparse
import os

from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key is None or api_key.strip() == "":
        raise ValueError(
            "GEMINI_API_KEY not found in environment variables or .env file"
        )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    user_prompt = args.user_prompt
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_prompt,
    )

    print(f"User prompt: {user_prompt}")
    if response is None or response.usage_metadata is None:
        print("Response is malformed")
        return
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n {response.text}")


if __name__ == "__main__":
    main()
