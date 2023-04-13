from ic.principal import Principal
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import Types
from ic.candid import encode, decode
import tensorflow as tf
import h5py
import numpy as np



#Load the .h5 file
model = tf.keras.models.load_model('H2.h5')

#Extract the model parameters
weights = model.get_weights()

#Print the extracted weights
for i in range(len(weights)):
    if i == (len(weights)-1) :
        w2= weights[i][0]
        #print(w2)



def convert(v,t):
    return t(v)

w2= convert(w2,float)


p2 = Principal.anonymous() # create anonymous principal
# Identity and Client are dependencies of Agent
iden = Identity()
client = Client()
agent = Agent(iden, client)


#send model weights
params = [
{'type': Types.Float64, 'value': w2}
]
data = encode (params)
result = agent.update_raw("6zfvq-kiaaa-aaaab-qacra-cai", "set2", encode(params))
print ('Model weights sent to the Canister')


#send permission
params2 = [
{'type': Types.Nat, 'value':1 }
]
data = encode (params2)
result = agent.update_raw("6zfvq-kiaaa-aaaab-qacra-cai", "permit2", encode(params2))


############################################################

# get updated model weights
params = []
data = encode(params)
result = agent.update_raw("6zfvq-kiaaa-aaaab-qacra-cai", "getWeight", encode(params))
print ("Global weights received.")

#Update the local model
weights1 = weights
weights1[9][0]=result[0]['value']
model.set_weights(weights1)
print("Model updated.")
model.save('model_cnn.h5')
 
############################################################


#Http Connection establishment

import requests

canister_id = "6zfvq-kiaaa-aaaab-qacra-cai"
method_name = "hello"
arguments = {"name": "Alice"}
ic_api_endpoint = "https://6zfvq-kiaaa-aaaab-qacra-cai.ic0.app"
# Create the HTTP request URL.
url = f"{ic_api_endpoint}/api/v2/canister/{canister_id}/{method_name}"
# Set the request headers and body.
headers = {"Content-Type": "application/json"}
data = {"arg": arguments}
# Send the HTTP request to the Internet Computer's HTTP API endpoint.
response = requests.post(url, headers=headers, json=data)
# Get the response data.
#result = response.json()
# Print the result.
#print(result)