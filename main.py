from settings import Settings, get_settings


# settings = Settings()

settings = get_settings()

print("settings:", settings.model_dump_json(indent=4), sep="\n")

print(f"tgbot.token: {settings.tgbot.token}")

print(f"db.url: {settings.db.url}")


# get_settings.cache_clear()  # -> "Clear the function's cache manually"
