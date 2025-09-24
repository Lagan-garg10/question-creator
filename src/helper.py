import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from src.prompt import *

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

def file_processing(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()

    data_full = ""
    for page in data:
        data_full+=page.page_content

    splitter1 = TokenTextSplitter(
        model_name="gpt-3.5-turbo",
        chunk_size=10000,
        chunk_overlap=200
    )

    data_full_chunk = splitter1.split_text(data_full)

    document_data = [Document(page_content=t) for t in data_full_chunk]

    splitter2 = TokenTextSplitter(
        model_name="gpt-3.5-turbo",
        chunk_size=1000,
        chunk_overlap=100
    )

    document_data2 = splitter2.split_documents(document_data)

    return document_data, document_data2

def llm_pipeline(file_path):
    document_data, document_data2 = file_processing(file_path)

    llm_ques_gen_pipeline = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=api_key
    )

    PROMPT_QUESTIONS  = PromptTemplate(template=prompt_template, input_variables=["text"])

    REFINE_PROMPT_QUESTIONS = PromptTemplate(
        input_variables=["existing_answer", "text"],
        template=refine_template,
    )


    ques_gen_chain = load_summarize_chain(llm = llm_ques_gen_pipeline, 
                                            chain_type = "refine", 
                                            verbose = True, 
                                            question_prompt=PROMPT_QUESTIONS, 
                                            refine_prompt=REFINE_PROMPT_QUESTIONS)   

    ques = ques_gen_chain.run(document_data)

    embeddings = download_hugging_face_embeddings()
    vector_db = FAISS.from_documents(document_data2, embeddings)

    llm_ans_gen_pipeline = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=api_key
    )

    answer_generation_chain = RetrievalQA.from_chain_type(
        llm=llm_ans_gen_pipeline,
        chain_type="stuff",
        retriever=vector_db.as_retriever()
    )

    ques_list = ques.split("\n")
    new_ques_list = []
    for i in range(0,len(ques_list),2):
        new_ques_list.append(ques_list[i])
    new_ques_list
    print("ques list",ques_list)

    return answer_generation_chain, new_ques_list

def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings