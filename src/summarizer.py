import os
import openai
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

kernel = sk.Kernel()

api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_text_completion_service("dv", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

prompt = kernel.create_semantic_function(
    """1. A robot may not injure a human being or, through inaction, allow a human being to come to harm. 2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law. 3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.
    
    Give me the TLDR in exactly 5 words.""")

#print(prompt())

summarize = kernel.create_semantic_function("{{$input}} \n\n one line TLDR with the fewest words")

print(summarize(""" The first law of thermodynamics: Energy cannot be created or destroyed, only transferred or transformed.
The second law of thermodynamics: The entropy of the universe always increases for a spontaneous process, or the efficiency of a heat engine is always less than one.
The third law of thermodynamics: The entropy of a perfect crystal at absolute zero is zero. """))
