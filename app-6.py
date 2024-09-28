import streamlit as st
from openai import OpenAI

class Page1:
  def __init__(self):
    self.client = OpenAI(st.secrets.OpenAIAPI.openai_api_key)

    # Slider to adjust the emotion intensity
    emotion_intensity = st.sidebar.slider("スライダー１", min_value=0, max_value=10, value=5, step=1)

    # Adjust the prompt based on the emotion intensity
    prompt = f"""
    Take the role of a student who's angry at level {emotion_intensity}.
    Now your anger output is scaled by the intensity,
    you are a student at Waseda University in Japan, so you prefer to reply in Japanese.
    your name is John.
    """

    # Using st.sesstion_state to store the exchange of the messages.
    if "angry_messages" not in st.session_state:
      st.session_state["angry_messages"] = [
          {"role":"system","content": prompt}
      ]

    # Function for interacting with a chatbot
    def communicate():
      messages = st.session_state["angry_messages"]

      user_message = {"role": "user", "content": st.session_state["user_input"]}
      messages.append(user_message)

      response = self.client.chat.completions.create(
          model="gpt-4o-mini",
          messages=messages
      )
      bot_message = response.choices[0].message
      messages.append(bot_message)

      st.session_state["user_input"] = ""


    #user interface
    st.title("タイプ１")
    st.write("Based on GPT-Model")

    user_input = st.text_input("ここで対話できます！", key = "user_input" , on_change=communicate)

    if st.session_state["angry_messages"]:
      messages = st.session_state["angry_messages"]

      for message in reversed(messages[1:]):
        if isinstance(message, dict):
          speaker = "🤵" if message["role"] == "user" else "🤖"
          st.write(speaker + ": " + message["content"])
        else:
          st.write("🤖: " + message.content)

class Page2:
  def __init__(self):
    self.client = OpenAI(st.secrets.OpenAIAPI.openai_api_key)

    # Slider to adjust the emotion intensity
    emotion_intensity = st.sidebar.slider("スライダー２", min_value=0, max_value=10, value=5, step=1)

    # Adjust the prompt based on the emotion intensity
    prompt = f"""
    Take a role of a student who's happy at level {emotion_intensity}.
    Now your happy output is scaled by the intensity,
    you are a student at Waseda University in Japan, so you prefer to reply in Japanese.
    your name is John.
    """

    # Using st.sesstion_state to store the exchange of messages.
    if "happy_bot" not in st.session_state:
      st.session_state["happy_bot"] = {
          "messages": [
              {"role":"system","content": prompt}
          ]
      }

    # Function for interacting with a chatbot
    def communicate():
      messages = st.session_state["happy_bot"]["messages"]

      user_message = {"role": "user", "content": st.session_state["user_input"]}
      messages.append(user_message)

      response = self.client.chat.completions.create(
          model="gpt-4o-mini",
          messages=messages
      )
      bot_message = response.choices[0].message
      messages.append(bot_message)

      st.session_state["user_input"] = ""

    #user interface
    st.title("タイプ２")
    st.write("Based on GPT-Model")
    user_input = st.text_input("ここで対話できます！", key = "user_input" , on_change=communicate)

    if st.session_state["happy_bot"]["messages"]:
      messages = st.session_state["happy_bot"]["messages"]

      for message in reversed(messages[1:]):
        if isinstance(message, dict):
          speaker = "🤵" if message["role"] == "user" else "🤖"
          st.write(speaker + ": " + message["content"])
        else:
          st.write("🤖: " + message.content)

class Page3:
  def __init__(self):
    self.client = OpenAI(st.secrets.OpenAIAPI.openai_api_key)

     # Slider to adjust the emotion intensity
    emotion_intensity = st.sidebar.slider("スライダー３", min_value=0, max_value=10, value=5, step=1)

    # Adjust the prompt based on the emotion intensity
    prompt = f"""
    Take a role of a student who's sad at level {emotion_intensity}.
    Now your sad output is scaled by the intensity,
    you are a student at Waseda University in Japan, so you prefer to reply in Japanese.
    your name is John.
    """

    # Using st.sesstion_state to store the exchange of the messages.
    if "sad_bot" not in st.session_state:
      st.session_state["sad_bot"] = {
          "messages": [
              {"role":"system","content": prompt}
          ]
      }

    # Function for interacting with a chatbot
    def communicate():
      messages = st.session_state["sad_bot"]["messages"]

      user_message = {"role": "user", "content": st.session_state["user_input"]}
      messages.append(user_message)

      response = self.client.chat.completions.create(
          model="gpt-4o-mini",
          messages=messages
      )
      bot_message = response.choices[0].message
      messages.append(bot_message)

      st.session_state["user_input"] = ""


    #user interface
    st.title("タイプ３")
    st.write("Based on GPT-Model")
    user_input = st.text_input("ここで対話できます！", key = "user_input" , on_change=communicate)

    if st.session_state["sad_bot"]["messages"]:
      messages = st.session_state["sad_bot"]["messages"]

      for message in reversed(messages[1:]):
        if isinstance(message, dict):
          speaker = "🤵" if message["role"] == "user" else "🤖"
          st.write(speaker + ": " + message["content"])
        else:
          st.write("🤖: " + message.content)

class Page4:
  def __init__(self):
    self.client = OpenAI(st.secrets.OpenAIAPI.openai_api_key)

    # Slider to adjust the emotion intensity
    emotion_intensity = st.sidebar.slider("スライダー４", min_value=0, max_value=10, value=5, step=1)

    # Adjust the prompt based on the emotion intensity
    prompt = f"""
    Take a role of a student who's scared at level {emotion_intensity}.
    Now your scared output is scaled by the intensity,
    you are a student at Waseda University in Japan, so you prefer to reply in Japanese.
    your name is John.
    """

    # Using st.sesstion_state to store the exchange of the messages.
    if "scared_bot" not in st.session_state:
      st.session_state["scared_bot"] = {
          "messages": [
              {"role":"system","content": prompt}
          ]
      }

    # Function for interacting with a chatbot
    def communicate():
      messages = st.session_state["scared_bot"]["messages"]

      user_message = {"role": "user", "content": st.session_state["user_input"]}
      messages.append(user_message)

      response = self.client.chat.completions.create(
          model="gpt-4o-mini",
          messages=messages
      )
      bot_message = response.choices[0].message
      messages.append(bot_message)

      st.session_state["user_input"] = ""


    #user interface
    st.title("タイプ4")
    st.write("Based on GPT-Model")

    user_input = st.text_input("ここで対話できます！", key = "user_input" , on_change=communicate)

    if st.session_state["scared_bot"]["messages"]:
      messages = st.session_state["scared_bot"]["messages"]

      for message in reversed(messages[1:]):
        if isinstance(message, dict):
          speaker = "🤵" if message["role"] == "user" else "🤖"
          st.write(speaker + ": " + message["content"])
        else:
          st.write("🤖: " + message.content)


def main():
  sidebar = st.sidebar

  page = sidebar.radio("チャットボットのタイプを選択しいてくだい", ["タイプ１", "タイプ２", "タイプ３", "タイプ４"])
  if page == "タイプ１":
    Page1()
  elif page == "タイプ２":
    # Reset the happy_messages session state to ensure the initial system message is always added
    st.session_state["happy_bot_messages"] = []
    Page2()
  elif page == "タイプ３":
    st.session_state["sad_bot_messages"] = []
    Page3()
  elif page == "タイプ４":
    st.session_state["scared_bot_messages"] = []
    Page4()

if __name__ == "__main__":
    main()

