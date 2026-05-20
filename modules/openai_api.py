### Allgemeiner Import der API und des Keys:
import openai
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
import textwrap

load_dotenv()

class SubtopicsResponse(BaseModel):
    # This structure guarantees the API returns a structured array of items
    subtopics: list[str] = Field(
        description="A list containing exactly 5 distinct subtopics. Only short titles."
    )

class FactsResponse(BaseModel):
    facts: list[str] = Field(
        description=(
            "A list of exactly 5 mind-blowing and highly accurate facts. Each string MUST follow this exact multi-line template:\n"
            "💥 [ALL-CAPS HEADLINE]\n"
            "[The factual body of the text]\n"
        )
    )



def get_openai_client():
    API_KEY = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI(api_key=API_KEY)
    return client

"""!!!Use .subtopics[index] to access the subtopic items!!!"""
def generate_subtopics(wiki_content: str) -> SubtopicsResponse:
    """Feeds the wiki string to GPT-5 Nano and returns a validated Pydantic object."""
    system_instruction = (
        "You are a charismatic, witty storyteller and researcher. Look at raw text "
        "and extract 4 incredibly enticing, fitting and fascinating subtopics."
    )

    user_prompt = (
        "Analyze this Wikipedia data and give me exactly 4 distinct subtopics that are in the given wiki content.\n\n"
        f"--- WIKI CONTENT ---\n{wiki_content}\n--- END WIKI CONTENT ---"
    )

    client = get_openai_client()

    try:
        # Using the .beta client block for strict schema compliance enforcement
        response = client.beta.chat.completions.parse(
            model="gpt-5-nano",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_prompt},
            ],
            response_format=SubtopicsResponse,  # <- Enforces structure
            temperature=1,
        )
        # Returns the automatically parsed Pydantic object directly
        return response.choices[0].message.parsed.subtopics
    except Exception as e:
        print(f"🧬 Uh oh, API error while pulling topics: {e}")
        return None
"""!!!Use .subtopics[index] to access the subtopic items!!!"""


def get_fantastic5(information, subtopic, stick_to_article_only = True) -> list[str] | None:
    """ Tells GPT-5 Nano to generate 5 facts about the given information. In case there are no facts, it returns 'No facts found.'
    :param information: String containing the information about main topic
    :param subtopic: Subtopic that specifies what the output facts should be about
    :param stick_to_article_only: If True, the output facts will only be about the given information.
    :return: list of 5 facts as strings
    written by Linda
    """
    role_description = "You are a charismatic, witty storyteller and researcher."
    if stick_to_article_only:
        user_prompt = (f"Strictly use {information} to generate 5 facts about {subtopic}. "
                       f"Keep {information} and {subtopic} in correlation.")

    else:
        user_prompt = f"Generate 5 facts about {information} in relation to {subtopic}."

    client = get_openai_client()

    try:
        response = client.chat.completions.parse(
            model="gpt-5-nano",
            messages=[
                {"role": "system", "content": role_description},
                {"role": "user", "content": user_prompt},
            ],
            response_format=FactsResponse,
        )
    except Exception as e:
        print(f"Uh oh, seems I couldn't run your request: {e}")
        return None

    raw_facts_list = response.choices[0].message.parsed.facts
    stylized_facts_list = []

    # Verarbeitet und richtet die Textblöcke dynamisch aneinander aus
    for fact_string in raw_facts_list:
        wrapped_lines = []
        for line in fact_string.split('\n'):
            cleaned_line = line.strip()

            # Leere Zeilen überspringen
            if not cleaned_line:
                wrapped_lines.append("")
                continue

            if cleaned_line.startswith("💥"):
                # Überschrift: Bleibt linksbündig, Folgezeilen rücken 3 Leerzeichen ein
                wrapped = textwrap.fill(cleaned_line, width=80, subsequent_indent="   ")
            else:
                # Fließtext: Der gesamte Block rückt 3 Leerzeichen ein, damit alles sauber untereinander steht
                wrapped = textwrap.fill(cleaned_line, width=80, initial_indent="   ", subsequent_indent="   ")

            wrapped_lines.append(wrapped)

        stylized_facts_list.append("\n".join(wrapped_lines))

    # Gibt die flache Liste mit den perfekt formatierten Textblöcken zurück
    return stylized_facts_list