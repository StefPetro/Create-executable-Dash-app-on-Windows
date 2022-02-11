# Create executable Dash App on Windows

This repository shows how to create your Dash projects as an executable application that can be used on other devices without
Python being installed. 

It also shows how it is possible to wrap the app in a native GUI window. Although, the example in this repository is
for Windows. More information on how to potentially change it to other platforms are described below. 

The required libraries used in this project are found in `requirements.txt`.

## Download the Hooks

Download the `hooks` folder and place them in same directory as your Dash project.

## Create the executable file

To create the executable file, run the following command in the terminal:

`pyinstaller -F --add-data "assets;assets" --additional-hooks-dir=hooks main.py --clean --workpath temp --distpath executable`

Now a folder called `executable` will be created and the file will be called `main.exe`.
When you run the executable file you can access it at your localhost:Port (e.g. 127.0.0.1:PORT)

## (Optional) Wrap app in a webview component to display as native GUI window

It is possible to wrap the app in a native GUI window, so that app doesn't have to be accessed from a browser.

First, two new imports are required:
```
import webview
from threading import Thread
```

The first import is the [Pywebview package](https://pywebview.flowrl.com/), which allows us to build a native GUI window
for the app. The second package is native to Python.

Then to run the app in a GUI window, include the following code in the file your app is run from: 

```
if __name__ == '__main__':
    def run_app():
        app.run_server(host='0.0.0.0', debug=False, port=port)

    t = Thread(target=run_app)
    t.daemon = True
    t.start()

    webview.create_window('Dash app', url=f'http://127.0.0.1:{port}')
    webview.start(debug=True, gui='cef')  # gui=cef is Windows specific
```

Now the app should start directly in a native GUI window instead of a browser. 
It is also possible to create an executable file where the app opens in the GUI window. You just have to run the `pyinstaller` command again.

If you're using [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) it is important
that the `gui` variable is set to the correct setting. For Windows it should be `gui=cef`. More information regarding
the different platforms and web engines, is available on 
[Pywebviews documentaion](https://pywebview.flowrl.com/guide/renderer.html).
