import dotenv
import os

dotenv.load_dotenv()

print(os.getenv("TRELLO_API_KEY"))
