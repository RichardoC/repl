import app, time
from app_components import TextDialog, clear_background


class TextDemo(app.App):
    def __init__(self):
        super().__init__()
        self.result = ""

    async def run(self, render_update):
        await render_update()

        dialog = TextDialog(">", self)
        self.overlays = [dialog]

        if await dialog.run(render_update):
            if dialog.text.startswith('?'):
                try: 
                    self.result = eval(dialog.text[1:].lstrip())
                except Exception as e :
                    self.result = e
            else:
                try: 
                    self.result = exec(dialog.text.lstrip())
                except Exception as e :
                    self.result = e
            
        self.overlays = []
        await render_update()

    def draw(self, ctx):
        clear_background(ctx)

        ctx.save()
        ctx.text_align = ctx.CENTER
        ctx.gray(1).move_to(0, 0).text(str(self.result))
        self.result = ""
        ctx.restore()

        self.draw_overlays(ctx)
        # time.sleep(1)

__app_export__ = TextDemo