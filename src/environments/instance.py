import os

env = os.environ.get("MONITOR_ENV", "dev")
port = os.environ.get("PORT", 8080)

env_list = {
    "dev": { "port": 5000, "debug": True, "swagger-url": "/api/swagger" },
    "qa": { "port": 5000, "debug": True, "swagger-url": "/api/swagger" },
    "prod": { "port": port, "debug": False, "swagger-url": None  }
}

env_config = env_list[env]