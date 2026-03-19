import plotly.express as px
import pandas as pd

df_model = pd.DataFrame({
    "model": ["ModelA", "ModelB", "ModelC"],
    "accuracy": [0.85, 0.90, 0.88]
})

fig = px.bar(
    df_model,
    x="model",
    y="accuracy",
    title="Model Accuracy Comparison"
)

fig.show()