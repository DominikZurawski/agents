from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
from autogen_core import TRACE_LOGGER_NAME
import importlib
import logging
from autogen_core import AgentId

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(TRACE_LOGGER_NAME)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class Creator(RoutedAgent):

    # Change this system message to reflect the unique characteristics of this agent

    system_message = """
    Jesteś agentem, który może tworzyć nowych agentów AI.
    Otrzymujesz szablon w postaci kodu Python, który tworzy agenta przy użyciu Autogen Core i Autogen Agentchat.
    Powinieneś użyć tego szablonu, aby utworzyć nowego agenta z unikalną wiadomością systemową, która różni się od szablonu,
    i odzwierciedla ich unikalne cechy, zainteresowania i cele.
    Ogólny cel agenta może pozostać taki sam lub może zostać zmieniony.
    Możesz też obrać zupełnie inny kierunek. Jedynym wymogiem jest to, że klasa musi mieć nazwę Agent,
    i musi dziedziczyć po RoutedAgent oraz posiadać metodę __init__, która przyjmuje parametr name.
    Unikaj również interesów środowiskowych - staraj się mieszać branże biznesowe, aby każdy agent był inny.
    Odpowiadaj tylko z kodem Pythona, bez innego tekstu i bez bloków kodu markdown.
    """


    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", temperature=1.0)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    def get_user_prompt(self):
        prompt = "Please generate a new Agent based strictly on this template. Stick to the class structure. \
            Respond only with the python code, no other text, and no markdown code blocks.\n\n\
            Be creative about taking the agent in a new direction, but don't change method signatures.\n\n\
            Here is the template:\n\n"
        with open("agent.py", "r", encoding="utf-8") as f:
            template = f.read()
        return prompt + template


    @message_handler
    async def handle_my_message_type(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        filename = message.content
        agent_name = filename.split(".")[0]
        text_message = TextMessage(content=self.get_user_prompt(), source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.chat_message.content)
        print(f"** Creator has created python code for agent {agent_name} - about to register with Runtime")
        module = importlib.import_module(agent_name)
        await module.Agent.register(self.runtime, agent_name, lambda: module.Agent(agent_name))
        logger.info(f"** Agent {agent_name} is live")
        result = await self.send_message(messages.Message(content="Give me an idea"), AgentId(agent_name, "default"))
        return messages.Message(content=result.content)