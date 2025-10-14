# Thirdparty libraries
from fastapi import FastAPI
# Moduls
from app.users.routes import users_api


app = FastAPI(
    title="Web template",
    contact={"Developer": "Zamurakin Andrew (rs-milano)", "telegram": " https://t.me/rs_Milano"},
    version="0.1.0",
    license_info={"name": "Apache 2.0", "url": "https://www.apache.org/licenses/LICENSE-2.0.html"}
)

app.include_router(users_api, prefix=f"users")
