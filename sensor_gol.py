import json
import threading
from collections import deque
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
porta = 1883
topico = "fiap/sprint4/gols"

ultimos_gols = deque(maxlen=30)

def ao_receber(client, userdata, msg):
    try:
        dado = json.loads(msg.payload.decode())
        ultimos_gols.append(dado)
    except:
        pass

cliente = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
cliente.on_message = ao_receber
cliente.connect(broker, porta, 60)
cliente.subscribe(topico)
threading.Thread(target=cliente.loop_forever, daemon=True).start()

app = dash.Dash(__name__)
app.title = "Painel de Gols"

app.layout = html.Div(
    style={"backgroundColor": "#0d1117", "color": "#fff", "padding": "20px", "fontFamily": "Arial"},
    children=[
        html.H1("Painel de Gols", style={"textAlign": "center", "color": "#00CC96"}),
        html.Div(id="resumo", style={"textAlign": "center", "marginBottom": "20px"}),
        html.Div([
            html.Div(dcc.Graph(id="grafico_velocidades"), style={"width": "65%", "display": "inline-block", "verticalAlign": "top"}),
            html.Div(html.Div(id="lista_gols"), style={"width": "33%", "display": "inline-block", "paddingLeft": "20px"})
        ]),
        dcc.Interval(id="intervalo", interval=1000, n_intervals=0)
    ]
)

@app.callback(
    Output("grafico_velocidades", "figure"),
    Output("lista_gols", "children"),
    Output("resumo", "children"),
    Input("intervalo", "n_intervals")
)
def atualizar(_):
    if not ultimos_gols:
        fig = go.Figure()
        fig.update_layout(title="Velocidades dos últimos gols (aguardando eventos)", template="plotly_dark")
        return fig, html.Div("Nenhum gol recebido ainda"), "Aguardando gols..."
    dados = list(ultimos_gols)
    nomes = [d["jogadora"] for d in dados]
    velocidades = [float(d["velocidade"]) for d in dados]
    tempos = [d.get("timestamp", "") for d in dados]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=nomes, y=velocidades, marker_color="#00CC96"))
    fig.update_layout(title="Velocidade dos gols (km/h)", xaxis_title="Jogadora", yaxis_title="Velocidade", template="plotly_dark")

    itens = []
    for d in reversed(dados):
        text = f"{d['timestamp'][:19].replace('T',' ')} - {d['jogadora']} — {d['velocidade']} km/h"
        itens.append(html.Div(text, style={"padding":"6px","borderBottom":"1px solid #222"}))

    media = sum(velocidades)/len(velocidades)
    total = len(velocidades)
    resumo = f"Total de gols: {total}  |  Velocidade média: {media:.2f} km/h"
    return fig, html.Div(items=itens, style={"maxHeight":"600px","overflowY":"auto"}), resumo

if __name__ == "__main__":
    app.run(debug=False, port=8050)
