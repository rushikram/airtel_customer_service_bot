# Airtel Customer Service Chatbot--Using RAG 

![image](https://github.com/user-attachments/assets/1e66853c-f1e3-487c-9f2a-7d12301215cb)



An AI-powered customer service chatbot for Airtel telecommunications.

## Interface :
![Screenshot 2025-06-06 224240](https://github.com/user-attachments/assets/86e2aeb8-9a98-42f6-b96c-b54f71baa299)


## AFTER CHAT:




https://github.com/user-attachments/assets/30bd9c67-e679-4b20-b4bb-4aba22773295




## Features

- Natural language processing for customer inquiries
- Knowledge base retrieval for accurate responses
- Conversation history and context maintenance
- Clean, user-friendly interface
- Easy deployment with Streamlit

## Technologies Used

- Python
- Streamlit (UI)
- LangChain (RAG)
- Groq API with LLaMA3-70b (LLM)
- FAISS (vector database)
- HuggingFace embeddings

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/airtel-chatbot.git
   cd airtel-chatbot
   
2. **Set up environment**
   ```bash
   GROQ_API_KEY=your_api_key_here
   
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Prepare knowledge base**
   ```bash
   Add your Airtel knowledge content to airtel_knowledge.txt
   
5. **Run the application**
   ```bash
   streamlit run app.py
   
6. **File-Structure**
   ```bash
   airtel-chatbot/
   ├── app.py                # Streamlit application
   ├── main.py               # Core chatbot logic
   ├── airtel_knowledge.txt  # Knowledge base content
   ├── requirements.txt      # Python dependencies
   └── .env                  # Environment variables

## Customization

To modify the chatbot's behavior:

- Edit airtel_knowledge.txt to update the knowledge base

- Adjust the prompt templates in main.py

- Modify the UI in app.py

## Deployment

The application can be deployed on any platform that supports Streamlit, such as:

- Streamlit Community Cloud

- AWS/Azure/GCP

- Heroku

- Docker container





 

