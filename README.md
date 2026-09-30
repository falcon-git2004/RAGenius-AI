\# 🧠 RAGenius AI



\## 🚀 Intelligent Document Assistant powered by RAG + Gemini



RAGenius AI is an AI-powered document assistant that allows users to upload documents, ask questions, analyze images, and receive intelligent answers using Retrieval-Augmented Generation (RAG) with Google's Gemini models.



\---



\# ✨ Features



\## 📄 Document Intelligence

\- Upload PDF documents

\- Extract and process document content

\- Ask questions about uploaded files

\- Retrieve relevant information using vector search



\## 🧠 RAG Pipeline

\- Document chunking

\- Text embeddings

\- FAISS vector database

\- Context-aware answers



\## 🤖 Gemini Integration

\- Powered by Google Gemini

\- Natural language responses

\- Image understanding with Gemini Vision



\## 🖼️ Image Analysis

\- Upload images

\- Ask questions about images

\- AI-powered visual understanding



\## 💬 Chat Experience

\- Conversation history

\- Multiple chat sessions

\- Persistent memory using SQLite



\---



\# 🏗️ Architecture

&#x20;            User

&#x20;             |

&#x20;             |

&#x20;     Streamlit Interface

&#x20;             |

&#x20;             |

&#x20;        FastAPI Backend

&#x20;             |

&#x20;   ---------------------

&#x20;   |                   |

&#x20;RAG Pipeline       Vision API

&#x20;   |                   |

&#x20;FAISS DB          Gemini Vision

&#x20;   |









\---



\# 🛠️ Tech Stack



\## Frontend

\- Streamlit



\## Backend

\- FastAPI

\- Python



\## AI

\- Google Gemini API

\- Retrieval Augmented Generation (RAG)



\## Vector Database

\- FAISS



\## Storage

\- SQLite



\---



\# 📂 Project Structure







RAGenius-AI/

│

├── app.py                 # Streamlit UI

│

├── backend/

│   ├── main.py            # FastAPI API

│   ├── rag.py             # RAG pipeline

│   ├── vision.py          # Gemini Vision

│   ├── database.py        # Chat storage

│   ├── memory.py          # Conversation memory

│   └── config.py          # Configuration

│

├── assets/

│   └── space.jpg          # UI background

│

├── data/

│

├── requirements.txt

│

└── README.md











\---



\# ⚙️ Installation



Clone the repository:



```bash

git clone https://github.com/falcon-git2004/RAGenius-AI.git



cd RAGenius-AI







\# ▶️ Running the Application



http://127.0.0.1:8000



\## Backend



Open terminal:



```bash

cd backend



uvicorn main:app --reload







Frontend

Open another terminal:



streamlit run app.py











🔮 Future Improvements

\- Multi-document support

\- Voice interaction

\- Advanced document search

\- Cloud deployment

\- User authentication

\- Better chat management





