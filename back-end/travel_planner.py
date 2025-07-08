import os
from dotenv import load_dotenv
from autogen import ConversableAgent, GroupChat, GroupChatManager

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

llm_config = {
    "config_list": [
        {
            "model": "gpt-4o-mini",
            "api_key": os.getenv("OPENAI_API_KEY"),
        }
    ]
}

user_proxy = ConversableAgent(
    name="User_Proxy_Agent",
    system_message="You are a user proxy agent.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

destination_expert = ConversableAgent(
    name="Destination_Expert_Agent",
    system_message="""
    You are the Destination Expert. Suggest one destination.
    Provide attractions, best time to visit, and customs.
    Format with a "DESTINATION SUMMARY" heading.
    """,
    llm_config=llm_config,
    human_input_mode="NEVER",
)

itinerary_creator = ConversableAgent(
    name="Itinerary_Creator_Agent",
    system_message="""
    Create a day-by-day itinerary. Format with "ITINERARY" heading.
    Include activities, accommodations, and meal suggestions.
    """,
    llm_config=llm_config,
    human_input_mode="NEVER",
)

budget_analyst = ConversableAgent(
    name="Budget_Analyst_Agent",
    system_message="""
    Estimate costs: transport, stay, food. Give budget tips.
    Format with "BUDGET" heading.
    """,
    llm_config=llm_config,
    human_input_mode="NEVER",
)

report_writer = ConversableAgent(
    name="Report_Writer_Agent",
    system_message="""
    Compile a full travel report based on outputs.
    Format with sections: Introduction, Destination Summary, Cultural Tips,
    Itinerary, Transportation, Budget Breakdown, Packing List, Conclusion.
    """,
    llm_config=llm_config,
    human_input_mode="NEVER",
)

allowed_transitions = {
    user_proxy: [destination_expert, user_proxy],
    destination_expert: [itinerary_creator, user_proxy],
    itinerary_creator: [budget_analyst, user_proxy],
    budget_analyst: [report_writer, user_proxy],
    report_writer: [user_proxy],
}

group_chat = GroupChat(
    agents=[
        user_proxy,
        destination_expert,
        itinerary_creator,
        budget_analyst,
        report_writer,
    ],
    allowed_or_disallowed_speaker_transitions=allowed_transitions,
    speaker_transitions_type="allowed",
    messages=[],
    max_round=6,
)

travel_planner_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)
