import discord
import traceback


class TestAgent(discord.Client):
    def __init__(self, orchestrator, *args, **kwargs):
        self._orchestrator = orchestrator
        super().__init__(*args, **kwargs)

    async def on_message(self, message) -> None: 
        if message.author == self.user:
            return
            
        if message.content.startswith('$nerdle wanna play'):
            self._orchestrator.generate()
            await message.channel.send(self.lets_play())

        if message.content.startswith('$cast'):
            await message.channel.send(f':green_square: :green_square: :black_large_square: :purple_square:')