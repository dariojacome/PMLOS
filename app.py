from fastapi import FastAPI
import pandas as pd
app = FastAPI()
df_users= pd.read_csv('user_playtime1.csv')
df_users
df_reviews=pd.read_csv('review.csv')
df_reviews
df_items=pd.read_csv('juego.csv')
df_items


app = FastAPI()

@app.get("/datos_dataframe")
async def obtener_datos():
    return df_items.to_dict(orient="records")


