from discord.ext import commands
from discord import app_commands, Interaction

from openai import OpenAI, OpenAIError


class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = OpenAI()

    @app_commands.command(name="ai", description="Ask AI a question")
    @app_commands.describe(question="Question you want to ask to AI")
    async def ai_help(self, interaction: Interaction, question: str):
        try:
            response = self.client.responses.create(model="gpt-5.4", input=question)
            answer = response.output_text

            await interaction.response.send_message(answer)

        except OpenAIError:
            print("Openai API keys are not in env")
            await interaction.response.send_message(
                "API Keys not found in env. Please try again!"
            )

        except Exception as e:
            response = f"Unexpected error happened while trying to get AI response. \n Unexpected error - {e}"
            print(response)
            await interaction.response.send_message(response)


async def setup(bot):
    await bot.add_cog(AI(bot=bot))
