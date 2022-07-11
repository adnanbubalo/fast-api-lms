from fastapi import FastAPI
from api import users, courses, sections

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    license_info={
        "name": "FIT",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
