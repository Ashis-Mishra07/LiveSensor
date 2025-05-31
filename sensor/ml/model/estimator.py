import os

class TargetValueMapping:
    def __init__(self):
        self.neg: int = 0
        self.pos: int = 1

    def to_dict(self):
        return self.__dict__

    def reverse_mapping(self):
        mapping_resp = self.to_dict()
        return dict(zip(mapping_resp.values(), mapping_resp.keys()))    



class SensorModel:
    def __init__(self , preprocessor , model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise Exception(f"Error initializing SensorModel: {e}")
        
    def predict(self, X):
        try:
            X_transformed = self.preprocessor.transform(X)
            y_pred = self.model.predict(X_transformed)
            return y_pred
        except Exception as e:
            raise Exception(f"Error during prediction: {e}")