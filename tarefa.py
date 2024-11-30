import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc

def cria_graficos(df):
    # histograma
    fig1 = px.histogram(df, x='Preço')
    fig1.update_layout(
        title='Distribuição do preço dos produtos', 
        xaxis_title='Preço', 
        yaxis_title='Frequência')

    # gráfico de dispersão
    fig2 = px.scatter(df, x='Preço', y='Gênero')
    fig2.update_layout(
        title='Dispersão - Preço e Gênero', 
        xaxis_title='Preço', 
        yaxis_title='Gêneros')
    

    # gráfico de barras
    fig3 = px.bar(df, x='Gênero')
    fig3.update_layout(
        title='Divisão por gênero',
        xaxis_title='Gênero',
        yaxis_title='Quantidade')


    # gráfico de pizza
    fig4 = px.pie(df, names='Gênero', color='Gênero')
    fig4.update_layout(
        title='Distribuição de gênero'
    )

    # gráfico de densidade
    fig5 = px.density_contour(df, x='Preço')
    fig5.update_layout(
        title='Densidade de preços'
    )
    return fig1, fig2, fig3, fig4, fig5

def cria_app(df):
    #cria app
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5 = cria_graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5)
    ])
    return app

df = pd.read_csv(r'F:/ecommerce_estatistica.csv')

if __name__ == '__main__':
    app = cria_app(df)
    # executa app
    app.run_server(debug=True, port=8050) # porta padrão