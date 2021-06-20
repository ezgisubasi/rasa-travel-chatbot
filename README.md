# rasa-travel-chatbot

Here is my Senior Design Project that I implemented to graduate from Computer Engineering. It is a chatbot made in RASA and helps the user to plan their vacation in the Turkish language. In order to plan the user's vacation, it provides reservations by asking various questions for hotel, flight, or event. 

# How to Run the Project?

1. Create a virtual environment of python 3.6 or greater.
2. Navigate to the rasa directory. Run the command:
       *rasa train*
3. After the model is trained, launch the rasa core server:
       *rasa run -m models --enable-api*
4. Launch the rasa actions server in another terminal:
       *rasa run actions*
5. Navigate to the chatbot/backend. Run the command:
       *python route.py*
6. Launch the frontend on the local python http server under the interface directory:
       *python -m http.server*


# Interface

Here is an example conversation for booking an event in Turkish.

<p align="center"> 
      <img width="523" alt="Ekran Resmi 2021-06-20 15 00 44" src="https://user-images.githubusercontent.com/52889449/122673287-64d8c100-d1d8-11eb-8694-e46359ee8055.png">
</p>
 
<p align="center"> 
      <img width="523" alt="Ekran Resmi 2021-06-20 15 00 57" src="https://user-images.githubusercontent.com/52889449/122673289-66a28480-d1d8-11eb-9845-0cf0f428023d.png">
</p>

<p align="center"> 
      <img width="523" alt="Ekran Resmi 2021-06-20 15 01 06" src="https://user-images.githubusercontent.com/52889449/122673291-67d3b180-d1d8-11eb-98cc-9ae7bf856697.png">
</p>


# Turkish Dataset

Due to the small number of chatbots in the Turkish language, Turkish datasets are also less. For this reason, we prepared a Turkish dataset from scratch while doing this project. In the end, we have 93 intents 29 entities in total and average 7 sentences for each intent.

<p align="center"> 
<img width="550" alt="Ekran Resmi 2021-06-20 15 08 45" src="https://user-images.githubusercontent.com/52889449/122673598-ce0d0400-d1d9-11eb-802a-9177eee58bdf.png">
</p>

# RASA

Rasa is an open source python library for constructing conversational software with minimal (or no) initial training data. It consists of two parts: Rasa NLU and Rasa Core. Dialogue management problem can be handled as a classification problem. At each iteration, Rasa Core predicts which action to take from a predefined list. On the other hand, #Rasa NLU# is a tool for natural language understanding. It combines a number of natural language processing and machine learning libraries in a consistent API.



# Best Configuration



