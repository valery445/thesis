import model
import pickle

mod = model.Model(modelName="globalModel.log", server=True)
mod.checkAccuracy()
with open('model_initial.pkl', 'rb') as f:
   mi = pickle.load(f)
mod.setWeights(mi)
mod.checkAccuracy()
with open('globalModelWeights.pkl', 'rb') as f:
   mi = pickle.load(f)
mod.setWeights(mi)
mod.checkAccuracy()
