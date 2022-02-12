#from src.agent.interfaces.IAgent import IAgent
import discord
import traceback


class NerdleAgent(discord.Client):

    def get_response(self) -> str:
        try:
           return 'Yo bitch, waddup?'
        except Exception as e:
            traceback.print_exc()

    async def on_message(self, message) -> None: 
        if message.author == self.user:
            return
            
        if message.content.startswith('$nerdle'):
            await message.channel.send(self.get_response())

    