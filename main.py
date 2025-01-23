import requests
import json
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    'x-api-key': os.getenv('SUPADATA_API_KEY')
}

st.title("Translate YouTube subtitles into Persian")
youtube_address = st.text_input("Paste your YouTube video URL")
bt = st.button('Translate')

if youtube_address != "" and bt:
    rr = requests.get(f'https://api.supadata.ai/v1/youtube/transcript?url={youtube_address}&text=true', headers=headers)
    response_data = rr.json()
    if 'content' in response_data and response_data['content']:
        content = response_data['content']
        openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                    "Authorization": f"Bearer {openrouter_api_key}"
            },
            data=json.dumps({
                "model": "google/gemini-2.0-flash-thinking-exp-1219:free",
                "messages": [
                    {
                        'role': 'system',
                        'content': 'Please translate this content into fluent persian'
                    },
                    {
                        'role': 'user',
                        'content': content
                    }
                ]
            })
        )

        translated_content = response.json()['choices'][0]['message']['content']
        st.markdown(
            f"""
                   <div style="direction: rtl; text-align: right;">
                       {translated_content}
                   </div>
                   """,
            unsafe_allow_html=True
        )
        st.download_button(
            label="Download Text",
            data=translated_content,
            file_name='translated_subtitles.txt',
            mime='text/plain'
        )

    else:
        st.warning("This video has no subtitles.")
