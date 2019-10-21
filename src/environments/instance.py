import os

env = os.environ.get("MONITORAPP_ENV", "dev")
port = os.environ.get("PORT", 8080)

env_list = {
    "dev": {"port": port,
            "debug": True,
            "swagger-url": "/api/swagger",
            "signalfx_api_key": "sandbox",
            "signalfx_api_base_url": "https://postb.in/1571626913820-2904260861687"
            },
    "qa": {"port": port,
           "debug": True,
           "swagger-url": "/api/swagger",
           "signalfx_api_key": "sandbox",
           "signalfx_api_base_url": "https://ingest.us0.signalfx.com/v2/event"
           },
    "prod": {"port": port,
             "debug": False,
             "swagger-url": None,
             "signalfx_api_key": "sandbox",
             "signalfx_api_base_url": "https://ingest.us0.signalfx.com/v2/event"
             }
}

env_config = env_list[env]
