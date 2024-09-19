# layout tudo que vai see visualizado
# callback funcionlidades que voce tera do dash

from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel("Dashboard.xlsx")
# esta linha le o arquivo execel e armazena os dados em uma variavel

fig = px.bar(df, x="PRODUTO", y="QUANTIDADE", color="ID", barmode="group")

opcoes = list(df["ID"].unique())

opcoes.append("Todas as Lojas")


app.layout = html.Div(children=[
    html.H1(children="Bourbon Shopping SP"),
    html.H2(children="Grafico com faturamento de todos os produtos separados por loja"),
    dcc.Dropdown(opcoes, value="Todas as Loja", id="lista_lojas"),
    dcc.Graph(
        id="grafico_quantidade_produto",
        figure=fig
    )
                      
])

@app.callback(
    Output("grafico_quantidade_produto", "figure"),
    Input("lista_lojas", "value")
)


def update_output(value):
    if value == "Todas as Lojas":

        fig = px.bar(df, df, x="PRODUTO", y="QUANTIDADE", color="ID", barmode="group")
    else:
        tabela_filtrada = df.loc[df["ID Loja"] == value, :]
        fig = px.bar(tabela_filtrada, x="PRODUTO", y="QUANTIDADE", color="ID", barmode="group")

    return fig
    
if __name__ == "__main__":
    app.run(debug=True)