import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import random
import plotly.graph_objs as go

# Jogadoras
jogadoras = [
    {"nome": "Ana Souza", "posicao": "Atacante"},
    {"nome": "Beatriz Lima", "posicao": "Meio-campo"},
    {"nome": "Carla Mendes", "posicao": "Zagueira"},
    {"nome": "Daniela Rocha", "posicao": "Goleira"},
    {"nome": "Fernanda Alves", "posicao": "Lateral"},
]

def gerar_dados():
    for j in jogadoras:
        j["velocidade"] = random.randint(15, 35)
        j["energia"] = random.randint(50, 100)
    return jogadoras

app = dash.Dash(__name__)
app.title = "Dashboard das Jogadoras"


app.layout = html.Div(
    style={
        "backgroundColor": "#0e1117",
        "color": "#FFFFFF",
        "fontFamily": "Arial, sans-serif",
        "padding": "20px",
    },
    children=[
        html.H1("Monitoramento das Jogadoras", style={"textAlign": "center", "color": "#00CC96"}),

        html.Div(id="cards-jogadoras", style={"display": "flex", "flexWrap": "wrap", "justifyContent": "center"}),

        html.Hr(),

        dcc.Graph(id="grafico-velocidade"),

        dcc.Interval(id="atualiza-dados", interval=3000, n_intervals=0)
    ]
)

@app.callback(
    [Output("cards-jogadoras", "children"),
     Output("grafico-velocidade", "figure")],
    [Input("atualiza-dados", "n_intervals")]
)
def atualizar_dados(_):
    dados = gerar_dados()

    cards = []
    for j in dados:
        cor = "#00CC96" if j["energia"] > 70 else "#FF6347"
        cards.append(
            html.Div(
                style={
                    "backgroundColor": "#1f2630",
                    "borderRadius": "15px",
                    "padding": "20px",
                    "margin": "10px",
                    "width": "200px",
                    "boxShadow": "0 0 10px rgba(0,0,0,0.5)",
                    "textAlign": "center",
                    "transition": "0.3s",
                },
                children=[
                    html.H3(j["nome"], style={"color": "#00CC96"}),
                    html.P(j["posicao"]),
                    html.P(f"Velocidade: {j['velocidade']} km/h"),
                    html.P(f"Energia: {j['energia']}%", style={"color": cor, "fontWeight": "bold"})
                ],
            )
        )

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=[j["nome"] for j in dados],
        y=[j["velocidade"] for j in dados],
        marker_color="#00CC96"
    ))

    fig.update_layout(
        title="Velocidade Atual das Jogadoras (km/h)",
        xaxis_title="Jogadora",
        yaxis_title="Velocidade",
        template="plotly_dark",
        paper_bgcolor="#0e1117",
        plot_bgcolor="#0e1117",
    )

    return cards, fig

if __name__ == "__main__":
    app.run(port=8050)
