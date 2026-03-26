import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "epoch": range(1, 8), 
    "loss": [0.9, 0.8, 0.75, 0.7, 0.65, 0.6, 0.58] 
})

fig = px.line(
    df,
    x="epoch",
    y="loss",
    title = "Training Loss Over Epochs",
    markers = True
)

fig.add_annotation(
    x=5, 
    y=0.65, 
    text= "Loss stabilizing", 
    showarrow=True, 
    arrowhead=4 

)

fig.show()