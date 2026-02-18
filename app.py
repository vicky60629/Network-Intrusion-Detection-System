import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]

    int_features[4]=np.log(int_features[4])
    int_features[5]=np.log(int_features[5])
    int_features[6]=np.log(int_features[6])
    int_features[7]=np.log(int_features[7])
    int_features[8]=np.log(int_features[8])
    int_features[9]=np.log(int_features[9])
    int_features[10]=np.log(int_features[10])
    int_features[11]=np.sqrt(int_features[11])
    int_features[12]=np.sqrt(int_features[12])
    int_features[13]=np.sqrt(int_features[13])
    int_features[14]=np.square(int_features[14])



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
