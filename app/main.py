from fastapi import FastAPI
from app.routes import home, users
from app.db import db
import databases
from app.core.config import settings

app = FastAPI()
database = databases.Database(settings.db_url)


@app.get("/")
async def read_root():
    return await db.User.objects.all()

# добавляем функцию, которая должна запускаться при запуске работы приложения
@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await db.User.objects.get_or_create(email="test@test.com")

# добавляем функцию, которая должна запускаться при завершении работы приложения
@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()




def get_application():
    _app = FastAPI(title="My project", version="1.0.0")
    # _app.add_event_handler("startup", tasks.create_start_app_handler(_app))
    # _app.add_event_handler("shutdown", tasks.create_stop_app_handler(_app))
    return _app


# Base.metadata.create_all(bind=engine)

app = get_application()

app.include_router(home.router)
app.include_router(users.router)

