# from getpass import getpass
# import pyrebase

# firebaseConfig={
#     "apiKey": "AIzaSyDG9LX4CI6Rsef49D1VTMmA_9QHg5zHywo",
#     "authDomain": "first-db-77609.firebaseapp.com",
#     "databaseURL": "https://first-db-77609-default-rtdb.firebaseio.com",
#     "projectId": "first-db-77609",
#     "storageBucket": "first-db-77609.appspot.com",
#     "messagingSenderId": "820407820543",
#     "appId": "1:820407820543:web:62a2c15e88e30ef6346cca",
#     "measurementId": "G-NGK0NGTGJX"
# }

# firebase = pyrebase.initialize_app(firebaseConfig)

# auth = firebase.auth()

# # auth = firebase.auth()

# # Log the user in


# # Get a reference to the database service
# db = firebase.database()

# # data to save
# data = {
#     "name": "Red Hair"
# }

# # Pass the user's idToken to the push method



# def signup():
#     email = input("Enter email: ")
#     password = input("Enter Password: ")
    
#     user = auth.create_user_with_email_and_password(email, password)
#     auth.send_email_verification(user['idToken'])

#     # results = db.child("users").child(user['localId']).push(data)
#     # print(results)
    


    
#     # print("Successfully created account")

# def login():
#     email = input("Enter Email: ")
#     password = getpass("Enter Password: ")
    
#     lila = auth.sign_in_with_email_and_password(email, password)
#     auth.send_email_verification(lila['idToken'])

    

#     # useri = db.child("users").child(user['localId']).get()
#     # for i in useri.each():
#     #     print(i.val()['name'])
    

#     print("Successfully signed in")
    
            

# choice = input("Login?: ")
# if choice == 'y':
#     login()
# elif choice == 'n':
    
#     signup()