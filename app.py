import app
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
            self.name = eval(dialog.text)
            

        self.overlays = []
        await render_update()

    def draw(self, ctx):
        clear_background(ctx)

        ctx.save()
        ctx.text_align = ctx.CENTER
        ctx.gray(1).move_to(0, 0).text(self.result)
        ctx.restore()

        self.draw_overlays(ctx)

__app_export__ = TextDemo