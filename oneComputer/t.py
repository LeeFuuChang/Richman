from ursina import *
app = Ursina()
print("ppppppppppppppppppppppp", window.screen_resolution)
def update():
    if held_keys["g"]:
        window.borderless = window.fullscreen = True
    else:
        window.borderless = window.fullscreen = False

app.run()