OpenAI Chat Model Web Interface
This is a simple web application built with Python and Streamlit to interact with an OpenAI chat model. It uses the langchain package to communicate with the OpenAI API. This application allows users to enter a message and receive a response from the chat model. It also provides the ability to upload text or PDF documents.

**Soon to add functionality to use embeddings / vector store to get better insights from uploaded documents.

Prerequisites
Before you begin, ensure you have met the following requirements:

You have installed Python 3.6 or later.
You have installed the necessary Python packages. You can install them with the following command:
bash
Copy code
pip install streamlit openai python-dotenv
You have an OpenAI API key. This should be placed in a .env file in the same directory as your app.py file, like this:
env
Copy code
OPENAI_API_KEY="your-api-key-here"
Replace "your-api-key-here" with your actual OpenAI API key.

Using the OpenAI Chat Model Web Interface
To use the web interface, follow these steps:

Run the Streamlit app with the following command:
bash
Copy code
streamlit run app.py
Open your web browser and go to http://localhost:8501. You should see the web interface.

Enter your message in the input box and click "Generate Response" to get a response from the OpenAI chat model.

To upload a document, click "Browse files" in the "Choose a document..." section. Select your document (text or PDF) and the content of the document will be displayed in the web interface.
