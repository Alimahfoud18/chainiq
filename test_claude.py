from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Tu es Karima, agente supply chain IA. Présente-toi en 2 phrases."}
    ]
)

print(message.content[0].text)