import discord
import traceback


class TestAgent(discord.Client):
    def __init__(self, evaluator, responder):
        self._evaluator= evaluator
        self._responder = responder

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
            _tokenized = message.content.split()
            await message.channel.send('you replied: ', _tokenized[1:])