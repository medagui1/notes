import requests
from requests.exceptions import ConnectionError
import json


base_url = 'http://localhost:8000/notes/'

def delete_note(id) :
    choice = input("Are you sure you want to delete this note? y/N: > ")
    delete_note = False
    while True :
        if choice == 'y' or choice == 'Y' :
            delete_note = True
            break
        elif choice == 'n' or choice == 'N' or choice == '' :
            delete_note = False
            break
        else :
            print("You have entred wrong input. Try again!")

    if delete_note == True :
        response = requests.delete(base_url + str(id))
        if response.status_code == 204 :
            print("Note deleted successfully")
        else :
            print("There was some error while performing your request!")
            print(f'Status code: {response.status_code}')


def edit_delete_note(id) :
    print("1) To edit this note")
    print("2) To delete this note")
    note_choice = input("Type your choice: ")

    while True :
        if note_choice == '1' :
            pass
            break
        elif note_choice == '2' :
            delete_note(id)
            break
        

def list_note_formatted_by_id(id) :

    
    response = requests.get(base_url + str(id))
    data = response.json()

    if response.status_code == 200 :
        id = data['id']
        title = data['title']
        content = data['content']
        created = data['created']

        print(f"""
====================================
Note N°{id}
{title}
Posted on {created}
{content}
====================================
""")

        edit_delete_note(id)

    elif response.status_code == 404 :
        print("You have entred a non valid id")
    



def get_notes() :
    try :
        response = requests.get(base_url)
        data = response.json()
        notes_string = json.dumps(data)
        notes_list = json.loads(notes_string)

        note_content = ""
        

        for note in notes_list :

            if len(note.get("content")) < 41 :
                note_content = note.get("content")
            elif len(note.get("content")) >= 41 :
                note_content = note.get("content")[:41] + '...'

            print(f"""               
Note N°{note['id']}
{note.get('title')}
Posted on {note.get('created')}
{note_content}
""")
            print("====================================")
        # print(notes_list) 
            # print(note)

        print(list_note_formatted_by_id(get_detailled_note()))
    
    except ConnectionError as e :
        print("There was a connection error. Please verify your internet connection.")
        print(f"error: {e}")



def post_notes() :
    data = get_user_note()
    response = requests.post(base_url, data)
    if response.status_code == 201 :
        print("Note created successfully")
    else :
        print(f"Failed to create note. Status code: {response.status_code}")

def get_user_note() :
    title = input('Enter the title: ')
    content = input('Enter your note content: ')
    data = {
        'title' : title,
        'content' : content
    }
    return data

def welcome() :

    try : 
        response = requests.get(base_url)
    except ConnectionError as e :
        print("Failed to connect to the server. Try again later!")
        return 

    print("Welcome to the cli client of the daily notes application.")
    print("")
    print("1) To create a new note.")
    print("2) To list all of your note in a nice format")
    print("3) To get the details of a note given its id")
    # print("q) to quit the client.")

    while True:
        user_input = input("Type your choice: ")
        if user_input == '1' :
            post_notes()
            break
        elif user_input == '2' :
            get_notes()
            break
        elif user_input == '3' :
            note_id = input("Enter your note id: ")
            list_note_formatted_by_id(note_id)
            break
        elif user_input == '4' :
            note_id = input("Enter your note id: ")

        else :
            print("You have entered a non supported input!")

def edit_note(id) :
    pass

def get_detailled_note() :
    chosen_note = input("Type the id of the desired note, to see it in detail: > ")
    return chosen_note
        
welcome()