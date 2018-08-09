import numpy as np
import pickle

pipeline = pickle.load(open('../rf_model.pkl', 'rb'))

example = {
  'attr': 6,  #
  'sinc': 9,    #
  'intel': 7,    #
  'fun': 7,  #
  'amb': 6,  #
  'shar': 5,
    'attr_o': 6,
    'sinc_o': 8,
  'intel_o': 8,
  'fun_o': 8,
  'amb_o': 8,
  'shar_o': 6
}

def make_prediction(features):
    X = np.array([features['attr'], (features['sinc']), features['intel'],
                  features['fun'], features['amb'], features['shar'],
                  features['attr_o'], features['sinc_o'], features['intel_o'],
                  features['fun_o'], features['amb_o'], features['shar_o']]).reshape(1,-1)
    prob_matched = pipeline.predict_proba(X)[0, 1]

    result = {
        'prediction': int(prob_matched> 0.5),
        'prob_matched': prob_matched
    }

    return result


if __name__ == '__main__':
    print(make_prediction(example))
