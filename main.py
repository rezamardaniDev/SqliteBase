from database import db

# run this file for create Database

db.add_user('reza', 'mardani')
print('data added seccessfully!')

try:
    db.delete_user('reza')
    print("data deleted seccessfully!")
except:
    print("Error")
