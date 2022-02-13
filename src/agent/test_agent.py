import discord
import traceback


class TestAgent(discord.Client):
    def __init__(self, evaluator, responder, *args, **kwargs):
        self._evaluator= evaluator
        self._responder = responder
        super().__init__(*args, **kwargs)

    def get_response(self) -> str:
        try:
           return 'Yo bitch, waddup?'
        except Exception as e:
            traceback.print_exc()

    def lets_play(self):
        try:
           return 'ok bitch, make a guess'
        except Exception as e:
            traceback.print_exc()

        

    async def on_message(self, message) -> None: 
        if message.author == self.user:
            return
            
        if message.content.startswith('$nerdle wanna play'):
            await message.channel.send(self.lets_play())

        if message.content.startswith('$cast'):
            await message.channel.send(f':green_square: :green_square: :black_large_square: :purple_square:')