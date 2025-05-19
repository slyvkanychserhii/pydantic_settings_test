from settings import Settings


settings = Settings()

print("settings:", settings.model_dump_json(indent=4), sep="\n")

print(f"tgbot.token: {settings.tgbot.token}")

print(f"db.url: {settings.db.url}")
