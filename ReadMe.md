To start testing with this code, you need an OpenAI paid subscription.

Follow these steps to configure and run the application.
1. Make sure you have Python 3 installed. Project has been tested with Python 3.12.
2. [Create new OpenAI project](https://help.openai.com/en/articles/9186755-managing-projects-in-the-api-platform)
3. [Create API Key](https://help.openai.com/en/articles/8867743-assign-api-key-permissions)
4. Install [Visual Studio 2022 Community](https://visualstudio.microsoft.com/vs/community/) with Python development component.
5. Open the `RealTimeVoice.sln` found in the root of the Git repo.
6. Regenerate `main-env` using the GUI or command `python -m venv main-env`.
7. Reload project if `main-env` was regenerated from command line.
8. Agree to install missing Python packages found in `requirements.txt`.
9. Copy and rename `config.py` to `config_dev.py`.
10. Fill in the OpenAI API Key obtained at step 2.
11. Ensure your system can output and record audio.
12. Start the application from Visual Studio by pressing the play button in the top-middle.
13. Navigate to http://localhost:49555/realtime-voice
14. Disable JavaScript blockers or add exception for current tab.

Alternatively, you can start the project from the command line:
1. Install requriements with `pip install -r requirements.txt`.
2. Run the Flask application with `python runserver.py`.
3. Open `http://localhost:5555` in your browser.

Some notes about the current version:
* The AI is configured to hold an English conversation.
* Transcription is written automatically for both user and AI assistant.
* To clear the text, click on the address bar and press Enter.
* This is a minimal implementation in Python using Flask.
* Project can be built using other IDE or command line.

### TODO
* Fix Python not retrieving environment variable added after creating Python venv.