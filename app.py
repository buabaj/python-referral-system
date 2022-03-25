import uvicorn
from fastapi import FastAPI
from routers.registerUser import router as registerUserRouter
from routers.redeemCode import router as redeemCodeRouter
from routers.getCode import router as getCodeRouter
from routers.checkReferralCode import router as checkReferralCodeRouter

app = FastAPI()

app.include_router(registerUserRouter)
app.include_router(redeemCodeRouter)
app.include_router(getCodeRouter)
app.include_router(checkReferralCodeRouter)


# create hello world endpoint
@app.get('/')
async def root():
    return {'message': 'Hello world'}


if __name__ == "__main__":
    uvicorn.run(app)
