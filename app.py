import app
from app_components import TextDialog, clear_background
import asyncio


class Repl(app.App):
    def __init__(self):
        super().__init__()
        self.message = None
        self.dialog = None

    async def run(self, render_update):
        # Show initial guidance
        self.message = "Use ? for results"
        await render_update()
        await asyncio.sleep(2)

        while True:
            # Clear message and show input dialog
            self.message = None
            await render_update()

            dialog = TextDialog(">", self)
            self.overlays = [dialog]

            if await dialog.run(render_update):
                if dialog.text.startswith('?'):
                    try:
                        result = eval(dialog.text[1:].lstrip())
                        self.message = str(result)
                    except Exception as e:
                        self.message = str(e)
                else:
                    try:
                        exec(dialog.text.lstrip())
                    except Exception as e:
                        self.message = str(e)

                # Show result before next input
                self.overlays = []
                await render_update()
                await asyncio.sleep(1)

    def draw(self, ctx):
        clear_background(ctx)

        # Draw message centered and scaled for circular screen
        if self.message:
            ctx.save()
            ctx.text_align = ctx.CENTER
            ctx.font_size = 10
            ctx.gray(1).move_to(0, 0).text(self.message)
            ctx.restore()
        else:
            # Only draw dialog when no message showing
            self.draw_overlays(ctx)

    def update(self, delta):
        pass

__app_export__ = Repl
