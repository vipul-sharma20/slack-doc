from typing import List, Dict

from slack.errors import SlackApiError
from slack import WebClient

from slack_doc import app_cache


# Get channel id from channel name
def get_channel_id(channel_name: str, client: WebClient) -> str:
    conversation_id = None
    try:
        result = client.conversations_list()
        for _ in result:
            if conversation_id is not None:
                break
            for channel in result["channels"]:
                if channel["name"] == channel_name:
                    return channel["id"]
        return None

    except SlackApiError as e:
        print(f"Error: {e}")


# Get conversation history for a parent message
def get_conversation_history(channel_id: str, parent_id: str, client: WebClient) -> List[Dict]:
    try:
        return client.conversations_replies(channel=channel_id, ts=parent_id)

    except SlackApiError as e:
        print(f"Error: {e}")


# Get user's name from id
def get_user_names_from_id(user_id: str, client: WebClient) -> str:
    if not app_cache.get(user_id):
        user_profile = client.users_profile_get(user=user_id)
        app_cache.set(user_id, user_profile["profile"]["real_name"])
    return app_cache.get(user_id)

