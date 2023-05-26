#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
import tkinter as tk

# Define possible user inputs and corresponding bot responses
responses = {
    "Hello": "Hello! Welcome to the best place to gain interesting knowledge about business strategies. How can I assist you today?",
    "What is the best business strategy?": "The best business strategy depends on various factors such as your industry, target market, and goals. Can you provide more details?",
    "How can I increase sales?": "There are several ways to increase sales, such as improving marketing efforts, offering promotions, enhancing customer experience, or expanding your product line. What specific area would you like advice on?",
    "Thank you": "You're welcome! If you have any more questions, feel free to ask.",
    "Bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, but I didn't understand. Can you please rephrase your question or should I connect you to our customer care agent?",
    "What are some effective ways to differentiate my business from competitors?": "Focus on unique product features, exceptional customer service, innovative marketing campaigns, or exclusive partnerships.",
    "How can I determine the optimal pricing strategy for my products or services?":"Analyze market demand, production costs, competition, and perceived value to determine the optimal pricing strategy.",
    "What steps should I take to expand my business into new markets?":"Conduct market research, evaluate competition, develop a market entry strategy, and tailor marketing and sales approaches to the target market.",
    "How can I effectively manage cash flow in my business?":"Forecast and budget accurately, control expenses, manage receivables, optimize inventory, and explore financing options when needed.",
    "How are you?":"I'm good. What can I help you with today?"
    
}

# Function to handle user inputs and generate bot responses
def get_bot_response(user_input):
    for key in responses:
        if key.lower() in user_input.lower():
            return responses[key]
    return responses["default"]


# Function to handle button click event
def on_send_button_click():
    user_input = user_entry.get()
    bot_response = get_bot_response(user_input)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chat_log.insert(tk.END, "Bot: " + bot_response + "\n")
    user_entry.delete(0, tk.END)
    
# Function to handle Enter key press event
def on_enter_key_press(event):
    on_send_button_click()

# Create GUI window
window = tk.Tk()
window.title("Business Advisor Chatbox")

# Create reminder message label
reminder_label = tk.Label(window, text="Note: Please remember to put question marks (?) after every question.")
reminder_label.pack()

# Create chat log text widget
chat_log = tk.Text(window, height=20, width=50)
chat_log.pack()

# Create user input entry widget
user_entry = tk.Entry(window, width=50)
user_entry.pack()

# Bind the Enter key press event to the user entry widget
user_entry.bind("<Return>", on_enter_key_press)

# Create send button
send_button = tk.Button(window, text="Send", command=on_send_button_click)
send_button.pack()

# Main GUI loop
window.mainloop()


# In[2]:


pip install tk


# In[ ]:




