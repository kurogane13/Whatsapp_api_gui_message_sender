
import easygui
from easygui import *
import os
import sys

def exit_program():

    warning = "warning.png"
    msg = "Do you want to Quit the Program?"
    title = "Quit Program?"
    choice = buttonbox(msg, title, image=warning, choices=["Yes", "No"])
    if choice == "Yes":
        os._exit(0)
    if choice == "No":
        main_program()
 
loop = 0
while(loop==0):
    
    def main_program():
        
        msg = "                        PYTHON WHATSAPP API MESSAGE SENDER              \n\n   To use the app, please provide:\n\n     - Country code\n     - Area code\n     - Phone number\n\n     Example: +54 9 11 1111 1111.\n\n          The numbers must be entered all together with no spaces"
        title = "PYTHON WHATSAPP"
        whatsapp_icon = "Whatsapp_icon.png"
        choice = buttonbox(msg=msg, title=title, image=whatsapp_icon, choices=["START", "EXIT PROGRAM"])

        if choice == "START":
            def phone_input():

                provide_number_title="Provide number"
                message_text="Please enter the phone number to send a message to.\n\nPhone number format example: +5491111112222"

                try:
                    accepted_characters = ['+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    provide_phone = enterbox(message_text, provide_number_title)
                    for item in accepted_characters:
                        if not item in provide_phone:
                            title_error="ERROR INVALID PHONE NUMBER"
                            message="Invalid phone number format, press ok to get back to phone number prompt"
                            error_image="redcross.png"
                            messagebox=msgbox(title=title_error, msg=message, image=error_image)
                            phone_input()
                        else:
                            title_confirm="                        SEND A MESSAGE TO PHONE NUMBER                        "
                            message_confirm="\n\n     To send a message to the phone number: "+provide_phone+", press Go"

                            choice = buttonbox(message_confirm, title_confirm, image=whatsapp_icon, choices=["Go", "Cancel", "Back to phone input"])
                            if choice == "Go":
                                url = "https://api.whatsapp.com/send?phone="+provide_phone
                                google_command="google-chrome "
                                os.system(google_command+url)
                                title_google="OPEN GOOGLE CHROME"
                                message_google="\n\n  Go to the app to send the message to phone number: "+provide_phone+"\n\n           To get back to main menu click OK"
                                messagebox=msgbox(title=title_google, msg=message_google, image=whatsapp_icon)

                                main_program()
                            if choice == "Cancel":
                                main_program()

                            if choice == "Back to phone input":
                                phone_input()


                    main_program()
                except:
                    exit_program()
                url = "https://api.whatsapp.com/send?phone="+phone_number

            phone_input()

        if choice == "EXIT PROGRAM":
            exit_program()
    main_program()
