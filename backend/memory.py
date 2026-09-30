chat_history = {}


def get_history(session_id):

    if session_id not in chat_history:
        chat_history[session_id] = []

    return chat_history[session_id]



def add_message(session_id, role, content):

    if session_id not in chat_history:
        chat_history[session_id] = []


    chat_history[session_id].append(
        {
            "role": role,
            "content": content
        }
    )