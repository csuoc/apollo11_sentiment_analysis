import plotly.express as px
import plotly.graph_objects as go
from tools.call_speakers import armstrong_eagle as ae
from tools.call_speakers import aldrin_eagle as aa

# Aldrin vs Armstrong Descent

def descent_analysis():

    armstrong_eagle = ae()
    aldrin_eagle = aa()
    aldrin_descent = aldrin_eagle.loc[(aldrin_eagle["mission_time"] >= 369064) & (aldrin_eagle["mission_time"] <= 369952)]
    armstrong_descent = armstrong_eagle.loc[(armstrong_eagle["mission_time"] >= 369064) & (armstrong_eagle["mission_time"] <= 369952)]

    fig1 = px.line(aldrin_descent, x="mission_time", y="compound")
    fig1.update_traces(line_color='green', name="Aldrin")

    fig2 = px.line(armstrong_descent, x="mission_time", y="compound")
    fig2.update_traces(line_color='blue', name="Armstrong")

    fig3 = go.Figure(data=fig1.data + fig2.data,
            layout=go.Layout(
            title=go.layout.Title(text="Compound analysis of the last 13 minutes before landing on the Moon")
                            ))

    fig3.update_xaxes(title_text="Mission time(s)")
    fig3.update_yaxes(title_text="Compound")
    fig3.update_traces(showlegend=True)

    return fig3.show()