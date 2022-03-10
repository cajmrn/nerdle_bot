import discord
import traceback
from src.utils import utils

class TestAgent(discord.Client):
    def __init__(self, orchestrator, *args, **kwargs):
        self._orchestrator = orchestrator
        super().__init__(*args, **kwargs)

    async def on_message(self, message) -> None: 
        if message.author == self.user:
            return
            
        if message.content.startswith('$nerdle wanna play'):
            game_id = self._orchestrator.generate_id()
            self._orchestrator._generator.set_id(game_id)
            self._orchestrator._generator._logger.set_id(game_id)
            self._orchestrator._evaluator.set_solution(self._orchestrator.generate())

            await message.channel.send(f'game_id: {game_id}, equation generated: {self._orchestrator._evaluator._solution}')

        if message.content.startswith('$cast'):
            print(utils.parse_guess(message.content, prefix='$cast'))
            _sum, _eval_set = self._orchestrator.evaluate(guess=utils.parse_guess(message.content, prefix='$cast'))
            print(f'_sum: {_sum}')
            print(f'_eval_set: {_eval_set}')  
            _transcribed_eval_set = self._orchestrator.transcribe(is_generator= False, evaluation_set = _eval_set)
            print(f'_transcribed set: {_transcribed_eval_set}')
            #await print(f'your content was: { message.content }')
            await message.channel.send(_transcribed_eval_set)