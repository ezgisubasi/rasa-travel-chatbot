# rasa-travel-chatbot

<p align="center"> 
      <img width="1000" alt="Ekran Resmi 2021-06-20 15 44 14" src="https://user-images.githubusercontent.com/52889449/122674712-0f53e280-d1df-11eb-8c33-4c3af63f5901.png">
</p>

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
      <img width="550" alt="Ekran Resmi 2021-06-20 15 00 44" src="https://user-images.githubusercontent.com/52889449/122673287-64d8c100-d1d8-11eb-8694-e46359ee8055.png">
</p>

In this figure, the chatbot is trying to learn which event the user wants to go to after the greeting.

<p align="center"> 
      <img width="550" alt="Ekran Resmi 2021-06-20 15 00 57" src="https://user-images.githubusercontent.com/52889449/122673289-66a28480-d1d8-11eb-9845-0cf0f428023d.png">
</p>

After that the chatbot asks for how many tickets the user wants and tries to make the reservation by asking for an e-mail.

<p align="center"> 
      <img width="550" alt="Ekran Resmi 2021-06-20 15 01 06" src="https://user-images.githubusercontent.com/52889449/122673291-67d3b180-d1d8-11eb-98cc-9ae7bf856697.png">
</p>

Finally, the chatbot tells the user how many tickets it has bought and sent to which e-mail address and asks if the user wants to take another action. If the user says no, chatbot finishes the conversation by saying goodbye.

# Turkish Dataset

Due to the small number of chatbots in the Turkish language, Turkish datasets are also less. For this reason, we prepared a Turkish dataset from scratch while doing this project. In order to do this, we translated the English datasets into Turkish using the Google API. In the end, we have 93 intents 29 entities in total, and an average of 7 sentences for each intent.

<p align="center"> 
<img width="550" alt="Ekran Resmi 2021-06-20 15 08 45" src="https://user-images.githubusercontent.com/52889449/122673598-ce0d0400-d1d9-11eb-802a-9177eee58bdf.png">
</p>

# RASA

Rasa is an open source python library for constructing conversational software with minimal (or no) initial training data. It consists of two parts: Rasa NLU and Rasa Core. Dialogue management problem can be handled as a classification problem. At each iteration, **Rasa Core** predicts which action to take from a predefined list. On the other hand, **Rasa NLU** is a tool for natural language understanding. It combines a number of natural language processing and machine learning libraries in a consistent API.

<p align="center"> 
     <img width="550" alt="Ekran Resmi 2021-06-20 15 17 46" src="https://user-images.githubusercontent.com/52889449/122674675-e9c6d900-d1de-11eb-94f0-937db5a811ea.png">
</p>


First a message is received and passed to Rasa NLU to extract the intent, entities, and the other structured information. Then the conversation state saved in the tracker which receives a notification that a new message has been received. In step 3, the policy receives the current state of the tracker and chooses which action to take next. Then chosen action is logged by the tracker and executed. If the predicted action is not ‘listen’, go back to step 3. After the first step all the remaining steps are performed by Rasa Core.

<p align="center"> 
      <img width="550" alt="Ekran Resmi 2021-06-20 15 17 46" src="https://user-images.githubusercontent.com/52889449/122673772-b1250080-d1da-11eb-9fc1-08376d04bf8b.png">
</p>

Here is an example of intent classification and entity extraction for a possible input sentence that chatbot can receive from user in this project.

<p align="center"> 
      <img width="550" alt="Ekran Resmi 2021-06-20 15 45 03" src="https://user-images.githubusercontent.com/52889449/122674608-92286d80-d1de-11eb-9be3-8d78ffce0adc.png">
      
</p>


# Best Configuration

We used pre-trained language model BERT for our pipeline. We compared three different pipeline configurations: a light configuration, a configuration using ConveRT, and a heavy configuration that included BERT. In each case we’re training a DIETClassifier for combined intent classification and entity recognition for 200 epochs, but in the light configuration we have CountVectorsFeaturizer, which creates bag-of-word representations for each incoming message at word and character levels. In the end, we chose config-light as the configuration of the chatbot.

# Results of the Configurations

<p align="center"> 
      <img width="571" alt="Ekran Resmi 2021-06-20 15 21 16" src="https://user-images.githubusercontent.com/52889449/122673919-7c657900-d1db-11eb-933f-430a6520ec19.png">
</p>

<p align="center"> 
      <img width="571" alt="Ekran Resmi 2021-06-20 15 21 27" src="https://user-images.githubusercontent.com/52889449/122673920-7d96a600-d1db-11eb-9851-fcf36fc4f137.png">
</p>

In the images below, there are confusion matrices created by each configuration for intent classification and entity extraction in turn.

### config-light:

<p align="center">
      <img width="400" alt="Ekran Resmi 2021-06-20 15 26 15" src="https://user-images.githubusercontent.com/52889449/122674048-247b4200-d1dc-11eb-8cb3-dceebc77d571.png">
      <img width="400" alt="Ekran Resmi 2021-06-20 15 26 36" src="https://user-images.githubusercontent.com/52889449/122674049-25ac6f00-d1dc-11eb-8e26-9be55d352701.png">
      <img width="400" alt="Ekran Resmi 2021-06-20 15 27 25" src="https://user-images.githubusercontent.com/52889449/122674040-1d543400-d1dc-11eb-9f0d-d1936ddce096.png">
      <img width="400" alt="Ekran Resmi 2021-06-20 15 27 46" src="https://user-images.githubusercontent.com/52889449/122674055-29d88c80-d1dc-11eb-837a-37982315c32b.png">
</p>


### config-convert:

<p align="center">  
      <img width="400" alt="Ekran Resmi 2021-06-20 15 30 19" src="https://user-images.githubusercontent.com/52889449/122674162-8b98f680-d1dc-11eb-8639-140cfff0a7fc.png">
      <img width="400" alt="Ekran Resmi 2021-06-20 15 30 30" src="https://user-images.githubusercontent.com/52889449/122674166-8d62ba00-d1dc-11eb-9989-7b5067375f23.png">
      <img width="400" alt="Ekran Resmi 2021-06-20 15 30 42" src="https://user-images.githubusercontent.com/52889449/122674170-8e93e700-d1dc-11eb-8990-297eecbf0ab7.png">
      <img width="400" alt="Ekran Resmi 2021-06-20 15 30 54" src="https://user-images.githubusercontent.com/52889449/122674174-8f2c7d80-d1dc-11eb-94d1-d875971e7942.png">
</p>

### config-heavy:

<p align="center">    
      <img width="400" alt="Ekran Resmi 2021-06-20 15 32 01" src="https://user-images.githubusercontent.com/52889449/122674208-c0a54900-d1dc-11eb-8534-69aa843b5f2e.png">  
      <img width="400" alt="Ekran Resmi 2021-06-20 15 32 12" src="https://user-images.githubusercontent.com/52889449/122674209-c307a300-d1dc-11eb-9dce-836d022e241d.png">    
      <img width="400" alt="Ekran Resmi 2021-06-20 15 32 22" src="https://user-images.githubusercontent.com/52889449/122674210-c4d16680-d1dc-11eb-9503-ad7f33a51bef.png">   
      <img width="400" alt="Ekran Resmi 2021-06-20 15 32 32" src="https://user-images.githubusercontent.com/52889449/122674213-c69b2a00-d1dc-11eb-8821-75aa89e2ee33.png">
</p>
