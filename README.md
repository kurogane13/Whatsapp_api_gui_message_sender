# Whatsapp_api_gui_message_sender

This is is a python gui to send messages to a user without the need to have them in your contacts list
------------------------------------------------------------------------------------------------------------

Description and functionallity of the program:

- Basic python easygui for opearating systems (Windows; Linux), which enables you to send a message to a contact, without the need to have it in your contact list.

- The program only asks for a parameter, which is the phone number, and should be provided in the following format:

  Country code + area code + cell phone number. Example +5491122223333
  
Once the phone is provided in the correct format, the whatsapp api will be called, to attempt to redirect you to the whatsapp client, or whatsapp web portal for a message to be sent.

Requirements
-----------------------------------------------------------------------------------------------------------

- Python3.x installed (tested with python3)
- easygui library installed
- os library installed
- Whatsapp client installed (preferred), or whatsapp web
