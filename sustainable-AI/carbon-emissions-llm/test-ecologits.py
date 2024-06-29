from ecologits import EcoLogits
from mistralai.client import MistralClient

# Initialize EcoLogits
EcoLogits.init()

client = MistralClient(api_key="OdqjnU6Xi0CeuORn1wZBRgqbk2jU9nKb")

response = client.chat(
    messages=[
        {"role": "user", "content": "Tell me a funny joke!"}
    ],
    model="mistral-tiny"
)

# Get estimated environmental impacts of the inference
print(response.impacts)