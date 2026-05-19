### Allgemeiner Import der API und des Keys:
from openai import OpenAI
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

TEST_INPUT_WIKI_TEXT = ("The United States of America (USA), also known as the United States (U.S.) or America, "
                        "is a country primarily located in North America. It is a federal republic consisting of 50 states "
                        "and a federal capital district, Washington, D.C. The 48 contiguous states border Canada to the north "
                        "and Mexico to the south, with the semi-exclave of Alaska in the northwest and the archipelago of Hawaii "
                        "in the Pacific Ocean. The United States also asserts sovereignty over five major island territories and "
                        "various uninhabited islands in Oceania and the Caribbean.[j] It is a megadiverse country, with the world's "
                        "third-largest land area[c] and third-largest population, exceeding 341 million.[k] Paleo-Indians first migrated "
                        "from North Asia to North America at least 15,000 years ago, and formed various civilizations. European discovery "
                        "of the Americas began in 1492, and British colonization followed with the 1607 settlement of Virginia, the first "
                        "of the Thirteen Colonies. The American Enlightenment that spread throughout the colonies in the 18th century "
                        "valued republicanism and liberalism. Clashes with the British Crown over taxation without parliamentary "
                        "representation and the denial of other English rights evolved into the American Revolution, which led to "
                        "the Declaration of Independence on July 4, 1776. Victory in the 1775–1783 Revolutionary War brought "
                        "international recognition of the country's sovereignty. Rapid westward territorial expansion followed the "
                        "purchase, settlement, and conquest of European-held or Indigenous-controlled territory. As more states "
                        "were admitted into the Union, a North–South division over slavery led 11 Southern states to declare "
                        "secession and join as the Confederate States of America in order to preserve slavery there. These states "
                        "fought against the Union in the American Civil War of 1861–1865 but were defeated. With the United States' victory "
                        "and reunification, slavery was abolished nationally. By 1900, the country had established itself as a great power, "
                        "a status solidified after its involvement during World War I. Following Japan's attack on Pearl Harbor in 1941, "
                        "the U.S. entered World War II on the side of the Allies. Its aftermath left the U.S. and the Soviet Union as rival "
                        "superpowers, competing for ideological dominance and international influence during the Cold War. The Soviet Union's "
                        "collapse in 1991 left the U.S. the world's sole superpower. The U.S. federal government is a representative democracy "
                        "with a president and a constitution that creates a separation of powers among three branches: legislative, executive, "
                        "and judicial. The United States Congress is a bicameral national legislature composed of the House of Representatives "
                        "(a lower house based on population) and the Senate (an upper house based on equal representation for each state). "
                        "Federalism grants substantial autonomy to the 50 states. In addition, 574 Native American tribes have sovereignty rights, "
                        "and there are 326 Native American reservations. A developed country, the U.S. ranks high in economic competitiveness, "
                        "innovation, and higher education. Accounting for over a quarter of nominal global GDP, the U.S. economy has been the "
                        "world's largest since about 1890. It is the wealthiest country, with the highest disposable household income per capita "
                        "among OECD members, though its wealth inequality is highly pronounced. Shaped by centuries of immigration, the culture of "
                        "the U.S. is diverse and globally influential. Making up a third of global military spending, the country is widely "
                        "considered to have the most powerful armed forces in the world and was the first to develop and employ nuclear weapons. "
                        "A member of numerous international organizations including the United Nations Security Council, it plays a major role in "
                        "global political, cultural, economic, and military affairs.")

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)


class SubtopicItem(BaseModel):
    title: str = Field(
        description="A catchy, thrilling podcast-style title for the subtopic."
    )
    description: str = Field(
        description="A punchy, fun, and impossible-to-ignore summary."
    )


class SubtopicsResponse(BaseModel):
    # This structure guarantees the API returns a structured array of items
    subtopics: list[SubtopicItem] = Field(
        description="A list containing exactly 4 distinct, enticing subtopics."
    )


class FactsResponse(BaseModel):
    facts: list[str] = Field(
        description="Exactly 5 mind-blowing and highly accurate facts strictly tied to the topic."
    )


"""!!!Use .subtopics[index] to access the subtopic items!!!"""
def generate_subtopics(client, wiki_content: str) -> SubtopicsResponse:
    """Feeds the wiki string to GPT-5 Nano and returns a validated Pydantic object."""
    system_instruction = (
        "You are a charismatic, witty storyteller and researcher. Look at raw text "
        "and extract 4 incredibly enticing, fitting and fascinating subtopics."
    )

    user_prompt = (
        "Analyze this Wikipedia data and give me exactly 4 distinct subtopics.\n\n"
        f"--- WIKI CONTENT ---\n{wiki_content}\n--- END WIKI CONTENT ---"
    )

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
        return response.choices[0].message.parsed
    except Exception as e:
        print(f"🧬 Uh oh, API error while pulling topics: {e}")
        return None
"""!!!Use .subtopics[index] to access the subtopic items!!!"""


def get_fantastic5(information, subtopic) -> list[str]:
    """ Tells GPT-5 Nano to generate 5 facts about the given information. In case there are no facts, it returns 'No facts found.'
    :param information: String containing the information about main topic
    :param subtopic: Subtopic that specifies what the output facts should be about
    :return: list of 5 facts as strings
    written by Linda
    """
    role_description = "You are a charismatic, witty storyteller and researcher."
    user_prompt = (f"Generate 5 facts about {information} in the subtopic of {subtopic}. "
                   f"Stick to the given information. If there aren't any facts, return 'No facts found.'")
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
    return response.choices[0].message.parsed


test_output_5facts = get_fantastic5(TEST_INPUT_WIKI_TEXT, "Instrumental music")
print(test_output_5facts)