import pandas as pd
from dash import Dash, html, dcc, Output, Input
import plotly.express as px

app = Dash(__name__)
df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

opcoes = list(df['ID Loja'].unique())

opcoes.append("Todas as Lojas")

app.layout = html.Div(children=[
    html.H1(children = 'Faturamento das lojas'),
    html.H2(children = 'Grafico com o Faturamento de todos os produtos separados por loja'),
    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas'),
    
    dcc.Graph(
        id='grafico_quantidade_produto',
        figure=fig
    )
])

@app.callback(
    Output('grafico_quantidade_produto', 'figure'),
    Input('lista_lojas', 'value')
)

def update_output(value):
    if value == "Todas as Lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run(debug=True)