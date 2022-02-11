import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import webview
from threading import Thread

app = dash.Dash(__name__)
server = app.server
port = 1234


app.layout = html.Div(
    [
        html.H3("Input a number and get it's square!", style={'marginBottom': 10}),
        dbc.Input(
            id='num-input',
            value=0,
            type='number', min=0, max=1000, step=1,
            style={'marginBottom': 10}
        ),
        html.H5(id='output-text')

    ],
    style={'margin': '1vh'}
)


@app.callback(
    Output('output-text', 'children'),
    [Input('num-input', 'value')]
)
def update_text(num):
    return f'The square of {num} is: {num**2}'


if __name__ == '__main__':
    # define function to run app
    def run_app():
        app.run_server(host='0.0.0.0', debug=False, port=port)

    # start the app as a background process so that the window can be created
    t = Thread(target=run_app)
    t.daemon = True
    t.start()

    # Create the window. Use the local server port to create the window
    # You can use the server (defined above) as url or f'http://127.0.0.1:{port}'
    webview.create_window('Dash app', url=server)

    # Start the window. The GUI needs to be set in order to work with dash bootstrap components.
    # The value is set to 'cef', which works for windows and on chromium.
    # Remember to pip install cefpython3
    # See docs for more info on the web engine/renderer
    # https://pywebview.flowrl.com/guide/renderer.html
    webview.start(debug=True, gui='cef')
