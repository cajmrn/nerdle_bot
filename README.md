# nerdle_bot
group nerdle. harder version.


# Token
- get your token
    - visit https://discord.com/developers/applications/941749459199615097/bot

# KeyRing implementation (Not working yet)
- create setup_env.py
    - It must be called setup_env.py so that the .gitignore keeps it on your system. It's where
    we are going to store your token for the bot.
    ```
    from src.agent.TokenProvider import TokenProvider
    import definitions as d

    if __name__ == '__main__':
    token = '<your token goes here>'
    tp = TokenProvider(d.Constansts.NAMESPACE,d.Constansts.ENTRY, token)
    tp.register()
    ```
    you can use the code above in setup_env.py to register the token into your env.

# .Env implementation
create a .env file at root and place the token in there as follows

```
NERDLE_TOKEN=<YOUR TOKEN GOES HERE>
```
they use python-dotenv to interact with the token.

# TODO currently
- [ ] create interfaces for a possible game orchestrator
    orchestrator needs to keep track of state of the game, guesses and responses.
- [ ] algorithm for generation of equation.
- [ ] aglorithm for sequencing / indexing / selection of responses.
- [ ] algorithm for comparison of guess with solution.
