import streamlit as st
import pandas as pd

st.title("就活企業スコアリングアプリ")

data = {
    "company": ["A社", "B社", "C社"],
    "salary": [700, 600, 800],
    "motivation": [80, 50, 90],
    "location_score": [85, 70, 90],
    "welfare_score": [75, 60, 88]
}

df = pd.DataFrame(data)

# 年収正規化
df["salary_score"] = (
    (df["salary"] - df["salary"].min()) /
    (df["salary"].max() - df["salary"].min())
) * 100

# 重みスライダー
salary_weight = st.slider("年収の重み", 0.0, 1.0, 0.5)

df["total_score"] = (
    df["salary_score"] * salary_weight +
    df["motivation"] * (1 - salary_weight)
)

st.write("総合スコア順")
st.dataframe(df.sort_values("total_score", ascending=False))
