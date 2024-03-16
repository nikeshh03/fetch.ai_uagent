from uagents import Agent, Context

jarvis = Agent(name = 'Jarvis', seed = "alice recovery phrase")

@jarvis.on_interval(period= 2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f"Hello my name is {ctx.name}")
    
if __name__ == "__main__":
    jarvis.run()