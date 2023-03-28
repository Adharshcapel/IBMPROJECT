import pickle
import numpy as np

from flask import Flask, render_template,request
# class, methods, inheritance,Polymorphism, Abstratction, encapusalation, decorators,

app=Flask(__name__)
model=pickle.load(open('upsample_data_equal.pkl','rb'))
@app.route('/') # to provide endpoints
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='The average price of the room will be $ {}'.format(output))

if __name__=='__main__':
    app.run(debug=True)