import os

env = os.environ.get("MONITORAPP_ENV", "dev")
port = os.environ.get("PORT", 8080)

env_list = {
    "dev": {"port": port,
            "debug": True,
            "swagger-url": "/api/swagger",
            "signal_api_key": "sandbox",
            "signal_api_base_url": "https://postb.in/1571626913820-2904260861687"
            },
    "qa": {"port": port,
           "debug": True,
           "swagger-url": "/api/swagger",
           "signal_api_key": "sandbox",
           "signal_api_base_url": "https://postb.in/1571626913820-2904260861687"
           },
    "prod": {"port": port,
             "debug": False,
             "swagger-url": None,
             "signal_api_key": "sandbox",
             "signal_api_base_url": "https://postb.in/1571626913820-2904260861687"
             }
}

env_config = env_list[env]
