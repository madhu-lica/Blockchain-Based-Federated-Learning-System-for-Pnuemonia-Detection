Blockchain based federated learning model for Pneumonia detection using Chest X-rays
====================================================================================

Dataset Source (Kaggle)
------------------------

https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

Software and Hardware Requirements
-----------------------------------

Hardware : 3 systems with active internet connection
Software : Colab, Python3 ,Internet Computer blockchain, Motoko playground

Instructions to execute the source code
---------------------------------------
1. In the 'Source Code' folder, open the 'Models' folder. Upload each .ipynb file into Colab and run the code snippets. This will build our local model for the three hospital systems.
2. Download the local models in the 3 respective systems as .h5 files. These .h5 files are also available in the 'source Code' folder.
3. Open the 'Hospitals' folder, and upload the .py file in the respective sysetms in any prefered IDE. (We have used VScode)
4. Make sure you have installed python3,TensorFlow, Keras, Numpy, ic-py using pip install commands in the command prompt/terminal.
        
     * Refer the following link for Python3 Set-up : https://realpython.com/installing-python/
     * TensorFlow installation : pip3 install -upgrade tensorflow  
     * Keras installation : pip install keras
     * Numpy installation : pip install numpy
     * ic-py installation : pip3 install ic-py

5. Open motoko playground in the browser. In the 'Source Code' folder, upload the smart_contact.mo file in the motoko playground.
6. Deploy the smart contract(Canister) using the deploy button in the top right corner.
7. A unique canister ID will be generated which will be valid for 20 mins. Copy this new canister ID and replace it with the old canister ID in each .py file in the respective hospital systems.
8. Run each python file parallelly in all the systems.
9. Open motoko playground and receive the model weights using the Candid UI on the right using call button under the get1,get2 and get3 functions(for respective hospitals)in the Candid UI. 
10. After receiving all the three weights, aggregate the weights using update_weights button. 
11. Send the aggaregated weights back to the hospitals by using get_weight button.
12. After receiving the updated weights from the canister, run each python file again by uncommenting the part of the code highlighted. (Replaces the received weights with the old weights in the respective .h5 file)
12. We can now use this .h5 file(model) to detect Pnuemonia at each hospital. 
