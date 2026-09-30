import streamlit as st
import requests
import uuid
import base64


API_URL = "http://127.0.0.1:8000"



st.set_page_config(
    page_title="RAGenius AI",
    page_icon="🚀",
    layout="wide"
)



# =========================
# Background
# =========================

def get_base64(file):

    with open(file, "rb") as f:

        return base64.b64encode(
            f.read()
        ).decode()



space = get_base64(
    "assets/space.jpg"
)




# =========================
# SPACE UI
# =========================

st.markdown(
f"""
<style>


/* =========================
   GLOBAL BACKGROUND
========================= */


html,
body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"] {{

    background:#020617 !important;

}}



.stApp {{

    background-image:

    linear-gradient(
        rgba(2,6,23,0.55),
        rgba(2,6,23,0.85)
    ),

    url("data:image/jpg;base64,{space}");

    background-size:cover;

    background-position:center;

    background-attachment:fixed;

}}





/* =========================
   REMOVE ALL WHITE AREAS
========================= */


[data-testid="stMain"] {{

    background:transparent !important;

}}



[data-testid="stMainBlockContainer"] {{

    background:transparent !important;

}}



.main {{

    background:transparent !important;

}}



.block-container {{

    background:transparent !important;

}}



[data-testid="stVerticalBlock"] {{

    background:transparent !important;

}}




/* =========================
   HEADER / TOP BAR
========================= */


[data-testid="stHeader"] {{

    background:

    rgba(2,6,23,0.95) !important;

}}



[data-testid="stToolbar"] {{

    background:transparent !important;

}}



[data-testid="stDecoration"] {{

    display:none !important;

}}





/* =========================
   SIDEBAR
========================= */


[data-testid="stSidebar"] {{

    background:

    rgba(2,6,23,0.92) !important;


    backdrop-filter:blur(20px);


    border-right:

    1px solid rgba(56,189,248,.35);

}}





/* =========================
   TEXT
========================= */


h1 {{

    color:#38bdf8 !important;


    text-shadow:

    0 0 25px #38bdf8;

}}



h2,
h3 {{

    color:#c084fc !important;

}}



p,
span,
label {{

    color:#e2e8f0 !important;

}}





/* =========================
   CHAT MESSAGES
========================= */


[data-testid="stChatMessage"] {{

    background:

    rgba(15,23,42,0.85) !important;


    border:

    1px solid rgba(56,189,248,.25);


    border-radius:20px;


    padding:18px;

}}






/* =========================
   CHAT INPUT
========================= */


[data-testid="stChatInput"] {{

    background:#020617 !important;


    border:

    1px solid #38bdf8 !important;


    border-radius:22px !important;


    box-shadow:

    0 0 25px rgba(56,189,248,.2);

}}



[data-testid="stChatInput"] > div {{

    background:#020617 !important;

}}



[data-testid="stChatInput"] textarea {{

    background:#020617 !important;


    color:white !important;

}}



[data-testid="stChatInput"] textarea::placeholder {{

    color:#94a3b8 !important;

}}





/* =========================
   UPLOAD BOX
========================= */


[data-testid="stFileUploader"] {{

    background:#020617 !important;


    border:

    1px solid rgba(56,189,248,.35);


    border-radius:18px;

}}



[data-testid="stFileUploader"] section {{

    background:#020617 !important;

}}



[data-testid="stFileUploader"] button {{

    background:

    linear-gradient(
        90deg,
        #06b6d4,
        #9333ea
    ) !important;


    color:white !important;


    border:none !important;

}}





/* =========================
   BUTTONS
========================= */


.stButton button {{

    background:

    linear-gradient(
        90deg,
        #06b6d4,
        #9333ea
    ) !important;


    color:white !important;


    border:none !important;


    border-radius:15px;

}}





/* =========================
   FOOTER
========================= */


footer {{

    background:#020617 !important;

}}



</style>
""",
unsafe_allow_html=True
)



# =========================
# SESSION
# =========================

if "session_id" not in st.session_state:

    st.session_state.session_id = str(uuid.uuid4())



if "messages" not in st.session_state:

    st.session_state.messages = []



if "pdf_name" not in st.session_state:

    st.session_state.pdf_name = None





# =========================
# SIDEBAR
# =========================

with st.sidebar:


    st.markdown(
        """
# 🧠 RAGenius AI

🚀 Space Document Intelligence
"""
    )



    st.divider()



    if st.button(
        "✨ New Chat"
    ):


        st.session_state.session_id = str(uuid.uuid4())

        st.session_state.messages = []

        st.rerun()




    st.divider()



    st.subheader(
        "🗂 Chat History"
    )



    try:

        result = requests.get(
            f"{API_URL}/sessions"
        )


        sessions = result.json()["sessions"]



        for s in sessions:


            if st.button(
                f"💬 {s[:10]}",
                key=s
            ):


                history = requests.get(
                    f"{API_URL}/history/{s}"
                ).json()



                st.session_state.session_id = s


                st.session_state.messages = history["messages"]


                st.rerun()


    except:

        st.caption(
            "No history"
        )



    st.divider()



    st.subheader(
        "📄 Documents"
    )



    pdf = st.file_uploader(
        "Upload PDF",
        type="pdf"
    )



    if pdf:


        if st.button(
            "🚀 Process PDF"
        ):


            files = {

                "file":
                (
                    pdf.name,
                    pdf.getvalue(),
                    "application/pdf"
                )

            }


            r = requests.post(
                f"{API_URL}/upload",
                files=files
            )



            if r.status_code == 200:


                st.success(
                    "Document Ready ✅"
                )


                st.session_state.pdf_name = pdf.name





# =========================
# HEADER
# =========================

st.markdown(
"""
# 🧠 RAGenius AI

### Your Intelligent Document Assistant

Powered by Gemini + RAG + FAISS 🚀

"""
)


st.divider()




# =========================
# CHAT DISPLAY
# =========================

for msg in st.session_state.messages:


    with st.chat_message(
        msg["role"]
    ):

        st.markdown(
            msg["content"]
        )





# =========================
# IMAGE UPLOAD
# =========================

image = st.file_uploader(

    "📎 Attach Image",

    type=[
        "png",
        "jpg",
        "jpeg"
    ]

)





# =========================
# IMAGE ANALYSIS
# =========================

if image:


    st.image(
        image,
        width=300
    )



    image_prompt = st.text_input(
        "Ask about image",
        "Analyze this image"
    )



    if st.button(
        "🔍 Analyze Image"
    ):



        files = {

            "file":
            (
                image.name,
                image.getvalue(),
                image.type
            )

        }



        response = requests.post(

            f"{API_URL}/vision",

            files=files,

            params={

                "prompt":image_prompt

            }

        )



        if response.status_code == 200:


            answer = response.json()["answer"]



            with st.chat_message(
                "assistant"
            ):

                st.markdown(
                    answer
                )


        else:

            st.error(
                response.text
            )






# =========================
# TEXT CHAT
# =========================

question = st.chat_input(
    "Ask your document anything... 🚀"
)



if question:


    st.session_state.messages.append(

        {
            "role":"user",
            "content":question
        }

    )



    with st.chat_message("user"):

        st.markdown(question)



    response = requests.post(

        f"{API_URL}/ask",

        json={

            "question":question,

            "session_id":
            st.session_state.session_id

        }

    )



    if response.status_code == 200:


        data = response.json()


        answer = data["answer"]["answer"]


        sources = data["answer"]["sources"]



        with st.chat_message(
            "assistant"
        ):


            st.markdown(
                answer
            )



            if sources:


                st.divider()


                st.markdown(
                    "📚 Sources"
                )


                for source in sources:

                    st.write(
                        source
                    )



        st.session_state.messages.append(

            {
                "role":"assistant",
                "content":answer
            }

        )