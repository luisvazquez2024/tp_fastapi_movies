from fastapi import FastAPI

from app.controllers import movies_router


app=FastAPI(
	title='Aprendiendo FastApi',
 description='Api primeros pasos',
 version='0.0.1'
)


app.include_router(router=movies_router, prefix=f'/api/v1')


