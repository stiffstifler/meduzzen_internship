from fastapi import FastAPI
from app.routes import home, users
from app.db import database, User
# from app.database.session import engine
# from app.database.db import Base




def get_application():
    _app = FastAPI(title="My project", version="1.0.0")
    # _app.add_event_handler("startup", tasks.create_start_app_handler(_app))
    # _app.add_event_handler("shutdown", tasks.create_stop_app_handler(_app))

    return _app


# Base.metadata.create_all(bind=engine)

app = get_application()

app.include_router(home.router)
app.include_router(users.router)

