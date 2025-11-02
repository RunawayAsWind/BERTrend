#  Copyright (c) 2024, RTE (https://www.rte-france.com)
#  See AUTHORS.txt
#  SPDX-License-Identifier: MPL-2.0
#  This file is part of BERTrend.
import pandas as pd
from bertopic import BERTopic
from loguru import logger

from bertrend import LLM_CONFIG
from bertrend.llm_utils.openai_client import OpenAI_Client
from bertrend.topic_analysis.data_structure import TopicDescription
from bertrend.topic_analysis.prompts import TOPIC_DESCRIPTION_PROMPT
from bertrend.AIModule.AIModelChatgpt import AIModelChatgpt
from bertrend.AIModule.AIModelDeepseek import AIModelDeepseek
import json
def get_topic_description(
    topic_representation: str,
    docs_text: str,
    language_code: str = "fr",
) -> TopicDescription | None:
    """Generates a LLM-based human-readable description of a topic composed of a title and a description (as a dict)"""
    # Prepare the prompt
    prompt = TOPIC_DESCRIPTION_PROMPT[language_code]
    try:
        # client = OpenAI_Client(
        #     api_key=LLM_CONFIG["api_key"],
        #     base_url=LLM_CONFIG["base_url"],
        #     model=LLM_CONFIG["model"],
        # )
        # answer = client.parse(
        #     response_format=TopicDescription,
        #     user_prompt=prompt.format(
        #         topic_representation=topic_representation,
        #         docs_text=docs_text,
        #     ),
        # )
        model = AIModelChatgpt(1.0)
        conversation_history = []
        userprompt = prompt.format(
            topic_representation=topic_representation,
            docs_text=docs_text,
        )
        bsuccess, reply = model.Chat(userprompt, conversation_history)
        print(model.DebugInfo(0))
        if bsuccess:
            print(reply)
            jsondata = json.loads(reply)
            if "title" in reply and "description" in jsondata:
                result = TopicDescription(
                    title=jsondata["title"],
                    description=jsondata["description"]
                )
                return result
        return None
    except Exception as e:
        logger.error(f"Error calling OpenAI API: {e}")
        return None


def generate_topic_description(
    topic_model: BERTopic,
    topic_number: int,
    filtered_docs: pd.DataFrame,
    language_code: str = "fr",
) -> TopicDescription | None:
    """Generates a LLM-based human-readable description of a topic composed of a title and a description (as a dict)"""
    topic_words = topic_model.get_topic(topic_number)
    if not topic_words:
        logger.warning(f"No words found for topic number {topic_number}")
        return None

    topic_representation = ", ".join(
        [word for word, _ in topic_words[:10]]
    )  # Get top 10 words

    # Prepare the documents text
    docs_text = "\n\n".join(
        [
            f"Document {i + 1}: {doc.text}..."
            for i, doc in filtered_docs.head(3).iterrows()
        ]
    )

    return get_topic_description(topic_representation, docs_text, language_code)
