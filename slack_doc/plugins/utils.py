from typing import List, Dict

from slack.errors import SlackApiError
from slack import WebClient


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
