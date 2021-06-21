import numpy as np
import joblib

vectorizer = joblib.load('vectorizer.joblib')
model = joblib.load('model.joblib')

def _get_profane_prob(prob):
    return prob[1]

def predict(texts):
    return model.predict(vectorizer.transform(texts))

def predict_prob(texts):
    return np.apply_along_axis(_get_profane_prob, 1, model.predict_proba(vectorizer.transform(texts)))

print(predict_prob(['Serious question, what can NA viewers do to inspire change to NA (other than magically increase player population)? Id straight up rather see 5 rookies on each NA team get shitstomped than watch the same mix-matched washed players lose, at least watching some rookies get perfect gamed would be hilarious, and the result would be no different than what we get already with these washed-up losers. Its the same complaints every year about NA (overpaid players, complacency, retirement home for other regions, etc...). Do we straight up just have to stop watching the spring and summer split games?']))