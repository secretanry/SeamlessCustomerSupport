import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# path to your json file
cred = credentials.Certificate({
"type": "service_account",
  "project_id": "seamless-customer-support",
  "private_key_id": "0faab57fee0cad9be7499f6713a77787392ffd15",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQC5mgVcWbXyOhYJ\n7fdMxn8NRkXRHJAZk1cQRdYLYUtyIiZus9OhSiIAawLUJzPnjWTjuArua7BIhIKm\nB7FVLrxxg55tMS38OCWow9d7QLJiGARFu55YTpU6p/NAedGPbRwS74HTMyZqmB9g\nf5F1oMw2P5YE22vkFWGZExVR397TDiGSFdQnLHcuLc5qo76+p/rtyiluLfgNyurS\nZLnVl8BEywXyTmV+/FE2l8uPxqmIHJCf0+yOOzhpM9mhyvoUuRXwDCo5fGcJ5oRl\nGQfKIrvg9M4Vj/SU+P//UDVEBZTl0E05O3xma+gZibxWh1t8iHwhF32WWv+PPg+z\n7NP7EpWzAgMBAAECgf9I1zjK55ePtVpaTwpG2ye2hnRnnSh4LGo7JeIIdzXZlTMl\nxrjPZt9atA4r6a9IA712kogSGUB/caAQ8nt5EPynzGlv2pH1W5tN6+jDwc2LwQ5k\nqhBNxSAXTod0bB6HOqVvm9sbgLtWv+SfoEQMuPCZhvGVyTxSZXsziTq2qwebF9pu\ndJxcmS/jHmLKiSgGuGxsR36LdiPK79F5cbXMG9Uyv0mUUK/qkAxVAHXskyp9gE+n\nGOC6tOSbBIuTgycaaXjBtT4ZXMBF6TadmA7yHqVbQysBztgbyGjapDEyDQ249IBl\nvfXbNMOPtityGvBAp0mhVna0LOCMrMlf9Vf63yECgYEA+0Se9DizdhEhoe67Z3sx\nt+af0JiCU9CODJ8zZGQsrXOrYb+30EA8tWa5FlFFMbwKr4KhVtoq0upzWAVmdCd1\nRhJOsRjWymZiePdhu6vY6L0VmK4d9bJ6nM1+mSZeZD5l4vsHs7qlMwem4R1XH2VF\nT2T+QgPN/4uUeB+Njb57msUCgYEAvRjRcju6mo4t83VcyKRM8nmvDeRSXZie+7p3\nwhemeGeggJe4+fnqRBlVyyp7F9soHlLdTGcvCR8N6VC0gHYq9yfGKxSdJo+LDHwl\nZIXac/M+ZZRSTLyf1xR2NpxvGT/5bpc2K2sNXuFPwcrGCbfHC1ZiIuLCOh7iJAr6\n0hWr1hcCgYEAvYWMv3jlI/DYBWQkRnFNlwCFGrlt0/pCqpKKGPbWHB5a7mfFJXbO\nU6Ufhg3WuySyip9lQjVch6n/Ri0MkiAQ/MFiSYIKwK9pJwSw2vVLroCwgXETd/cf\nNJZrHukp2UKXZxUhQhdN86eZ38JZrHyeQrxSa0ijYFTPr6tdAcTjRmECgYBJ9/9W\nFA82jg9jgLE+uyZuYzMa2AlwG1d1WMen4OB5kO+z3aW6AwykftSUmJV2C4Bx/DAc\nxvAbPU6PycYRyiecbq6SA4pFnzjhNV7bJ5EAclIiIhbfdZmA5LwpOKAs3F2R6QyD\nh2i/iJtOTyeQfZca1DunMdSQL6x+NN1QeLGzGQKBgBeuxozZ50ZLORXkI1KyMhlh\ntNovpoLwOzZ1/Ptfl66YG7zhhGEGsSiFosUQSEiW9vw1BSV5OjJ2GAlPgMMneAah\nlPDhkYjzpoQTHPTqXImGlfZD6ihWqhJfH3Y+dxI0l3B0n+lSP76KYt0u5TQF1uh4\nvfX1e+gQEt2eDjF1KBxz\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-j8s4r@seamless-customer-support.iam.gserviceaccount.com",
  "client_id": "113425141176073502133",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-j8s4r%40seamless-customer-support.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})

# https://your-database-name.firebaseio.com
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seamless-customer-support-default-rtdb.europe-west1.firebasedatabase.app/'
})

ref = db.reference('/')

# Initialize 'history' and 'question_log' branches
history = ref.child('history')
question_log = ref.child('question_log')

# Add a user's question and answer to 'history'
user_id = '0003'
question = 'What if...?'
answer = 'Customer support.'
#history.child(user_id).push({
#    'A question': question,
#    'An answer': answer
#})
# Add a question to 'question_log'
question_log.push({
    'user_id': user_id,
    'question': question,
    'processed': False,
    'FAQ_status': 'unknown'
})


# Check if the data has been added
print(history.get())
