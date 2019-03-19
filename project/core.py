import pickle

class CoreRegressors:

    def __init__(self):
        with open('../data/objects/regressors.pkl', 'rb') as input:
            self.DT_R = pickle.load(input)
            self.RF_R = pickle.load(input)
            self.GB_R = pickle.load(input)
    def DTR_predict(self,genres_vector):
        return self.DT_R.predict(genres_vector)
    def RFR_predict(self,genres_vector):
        return self.RF_R.predict(genres_vector)
    def GBR_predict(self,genres_vector):
        return self.GB_R.predict(genres_vector)
    def prueba(self):
        print self.DT_R
        
