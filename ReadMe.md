To start testing with this code, you need an OpenAI paid subscription.

Follow these steps to configure and run the application.
1. Make sure you have Python 3 installed. Project has been tested with Python 3.12.
2. [Create new OpenAI project](https://help.openai.com/en/articles/9186755-managing-projects-in-the-api-platform)
3. [Create API Key](https://help.openai.com/en/articles/8867743-assign-api-key-permissions)
4. Install [Visual Studio 2022 Community](https://visualstudio.microsoft.com/vs/community/) with Python development component.
5. Open the `RealTimeVoice.sln` found in the root of the Git repo.
6. Agree to install missing Python packages found in `requirements.txt`.
7. Copy and rename `config.py` to `config_dev.py`.
8. Fill in the OpenAI API Key obtained at step 2.
9. Ensure your system can output and record audio.
10. Start the application from Visual Studio by pressing the play button in the top-middle.
11. Navigate to https://localhost:49555/realtime-voice
12. Disable JavaScript blockers or add exception for current tab.

Some notes about the current version:
* The AI is configured to hold an English conversation.
* Transcription is written automatically for both user and AI assistant.
* To clear the text, click on the address bar and press Enter.
* This is a minimal implementation in Python using Flask.
* Project can be build using other IDE or command line.
