import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,Area,Num_of_bathrooms,Num_of_bedrooms,CarParking,Gasconnection):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Area
    x[1] = Num_of_bathrooms
    x[2] = Num_of_bedrooms
    x[3] = CarParking
    x[4] = Gasconnection
    if loc_index >= 0:
        x[loc_index] = 1

    return round( __model.predict([x])[0],2)


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts....start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]

    global __model
    with open("./artifacts/mumbai_house_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")



if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('kharghar',1000,1,1,1,0))
    print(get_estimated_price('kamothe',400,1,1,0,0))
    print(get_estimated_price('karjat', 1000, 2,3,2,0)) # other location
    print(get_estimated_price('koproli', 600, 1, 1, 2, 0))  # other location
