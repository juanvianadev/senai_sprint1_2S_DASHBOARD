import pandas as pd
from dash import Dash, html, dcc, Output, Input
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("./projeto/vgsales.csv")
dfLimpo = df.drop(['Rank', 'Platform', 'Year', 'Genre', 'Publisher'], axis=1)

app.layout = html.Div(children=[
    html.H1(children='Vendas de Jogos por Regiao'),
    html.H2(children='Gráfico com as vendas de diversos jogos separados por região'),
    
    dcc.Dropdown(
        id='lista_jogos',
        options=[{'label': nome, 'value': nome} for nome in dfLimpo['Name'].unique()],
        value=dfLimpo['Name'].unique()[0]
    ),
    
    dcc.Graph(
        id='grafico_vendas_regiao'
    )
])

@app.callback(
    Output('grafico_vendas_regiao', 'figure'),
    Input('lista_jogos', 'value')
)
def atualizar_grafico(jogo_selecionado):
    df_filtrado = dfLimpo[dfLimpo['Name'] == jogo_selecionado]
    
    regioes = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
    vendas = [df_filtrado[regiao].values[0] for regiao in regioes]

    fig = px.pie(
        names=regioes,  
        values=vendas,  
        title=f'Vendas de {jogo_selecionado} por Região'
    )
    
    return fig

# Executar a aplicação
if __name__ == '__main__':
    app.run(debug=True)
