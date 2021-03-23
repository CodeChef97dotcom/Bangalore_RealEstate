import son,pickle
import numpy as np

__locations = None
__data_columns = None
__ model = None


def get_estimated_price(location,availability,sqft,bath,balcony,bua,pa,sbua,bhk): 
	try:
    	loc_index = __data_columns.index(location.lower())
    except:
    	loc_index = -1	

    x = np.zeros(len(__data_columns))
    x[0] = availability
    x[1] = sqft
    x[2] = bath
    x[3] = balcony
    x[4] = bua
    x[5] = pa
    x[6] = sbua
    x[7] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
	return __locations

def load_saved_artifacts():
	print("Loading saved artifacts")
	global __data_columns
	global __locations
	global __model

	with open("/Users/samarpanguha/Downloads/Personal_Projects/Real_Estate",'r') as f:
		__data_columns = json.laod(f)['__data_columns']
		__locations = __data_columns[10:]

	with open("/Users/samarpanguha/Downloads/Personal_Projects/Real_Estate",'rb') as f:
		__model = pickle.load(f)

	print("Loading artifacts...done")	

if __name__ == '__main__':
		load_saved_artifacts()
		print(get_location_names())
		print(get_estimated_price('1st Phase JP Nagar',1,1000,2, 2, 1,0,0,2))
