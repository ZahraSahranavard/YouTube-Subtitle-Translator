# YouTube Subtitle Translator

## Overview
This application translates subtitles of YouTube videos into Persian. By utilizing external APIs, it retrieves subtitles from a given YouTube video URL and translates them into fluent Persian, providing users with an easy way to access the translated content. The application uses the free Gemini 2.0 Flash model for translation. Depending on your needs and the number of requests per month, you can opt for other free or paid models as well.

![demo](Images/photo2.png)


## Features
- **Fetches Subtitles**: Retrieves subtitles from YouTube videos using the Supadata API.
- **Translation**: Translates the fetched subtitles into Persian using the OpenRouter AI API.
- **User-Friendly Interface**: Built with Streamlit, allowing for an intuitive user experience.
- **Downloadable Output**: Users can download the translated subtitles as a text file.

## Dependencies

To run this program, you need the following libraries:

- `requests`: For sending HTTP requests to APIs.
- `streamlit`: For creating a web user interface.
- `python-dotenv`: For loading environment variables from a `.env` file.
- `json`: For processing JSON data.

You can install these libraries using the following command:

```bash
pip install requests streamlit python-dotenv 
```

### Notes:
- Make sure to set the API keys correctly in your `.env` file.
- This program is designed to support RTL (right-to-left) text for compatibility with the Persian language.
