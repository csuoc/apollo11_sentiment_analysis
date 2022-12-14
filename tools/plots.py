# Import box

import plotly.express as px
import plotly.graph_objects as go
from tools.call_speakers import armstrong_eagle as armeagle
from tools.call_speakers import aldrin_eagle as aldeagle
from tools.call_speakers import armstrong_eva as armeva
from tools.call_speakers import aldrin_eva as aldeva
from tools.call_speakers import armstrong_tran as armtran
from tools.call_speakers import president_nixon as nixon

# Aldrin vs Armstrong Descent

def descent_analysis():

    armstrong_eagle = armeagle()
    aldrin_eagle = aldeagle()
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


    fig4 = px.box(aldrin_descent, x="speaker", y="compound")
    fig4.update_traces(line_color='green', name="Aldrin")

    fig5 = px.box(armstrong_eagle, x="speaker", y="compound")
    fig5.update_traces(line_color='blue', name="Armstrong")

    fig6 = go.Figure(data=fig4.data + fig5.data,
            layout=go.Layout(
            title=go.layout.Title(text="Descriptive statistics")
                            ))
    fig6.update_xaxes(title_text="Speaker")
    fig6.update_yaxes(title_text="Compound")
    fig6.update_traces(showlegend=True)

    return fig3.show(), fig6.show()

# Aldrin vs Armstrong full moonwalk (3 hours)

def eva_analysis():

    armstrong_eva = armeva()
    aldrin_eva = aldeva()
    aldrin_eva = aldrin_eva.loc[(aldrin_eva["mission_time"] >= 393768) & (aldrin_eva["mission_time"] <= 401918) & (aldrin_eva["compound"] >= 0.5) | (aldrin_eva["compound"] <= -0.5)]
    armstrong_eva = armstrong_eva.loc[(armstrong_eva["mission_time"] >= 393768) & (armstrong_eva["mission_time"] <= 401918) & (armstrong_eva["compound"] >= 0.5) | (armstrong_eva["compound"] <= -0.5)]

    fig1 = px.line(aldrin_eva, x="mission_time", y="compound")
    fig1.update_traces(line_color='green', name="Aldrin")

    fig2 = px.line(armstrong_eva, x="mission_time", y="compound")
    fig2.update_traces(line_color='blue', name="Armstrong")

    fig3 = go.Figure(data=fig1.data + fig2.data,
            layout=go.Layout(
            title=go.layout.Title(text="Compound analysis of the complete moonwalk of Armstrong and Aldrin on the Moon")
                            ))

    fig3.update_xaxes(title_text="Mission time(s) - Total time 3 hours")
    fig3.update_yaxes(title_text="Compound >0.5 or < -0.5")
    fig3.update_traces(showlegend=True)

    fig4 = px.box(aldrin_eva, x="speaker", y="compound")
    fig4.update_traces(line_color='green', name="Aldrin")

    fig5 = px.box(armstrong_eva, x="speaker", y="compound")
    fig5.update_traces(line_color='blue', name="Armstrong")

    fig6 = go.Figure(data=fig4.data + fig5.data,
            layout=go.Layout(
            title=go.layout.Title(text="Descriptive statistics")
                            ))
    fig6.update_xaxes(title_text="Speaker")
    fig6.update_yaxes(title_text="Compound")
    fig6.update_traces(showlegend=True)

    return fig3.show(), fig6.show()

# The sentence

def onesmallstep_analysis():

    armstrong_tran = armtran()
    armstrong_tran = armstrong_tran.loc[armstrong_tran["mission_time"] == 393888]

    return armstrong_tran

# Nixon speech

def nixon_analysis():

    nixon_speech = nixon()
    fig1 = px.line(nixon_speech, x="mission_time", y="compound", title="Compound analysis of Nixon speech")
    fig1.update_traces(line_color='greenyellow', name="President Nixon")

    fig1.update_xaxes(title_text="President Nixon speech")
    fig1.update_yaxes(title_text="Compound")
    fig1.update_traces(showlegend=True)

    return fig1.show()