import xgboost as xgb
import pandas as pd
from sklearn.metrics import roc_auc_score, confusion_matrix, recall_score, accuracy_score, precision_score, f1_score

def xgb_model_train(train_data, valid_data, xgb_model_path, y_col_name='label',
                    gamma=0, max_depth=6, subsample=0.7, min_child_weight=1, scale_pos_weight=1, eta=0.3):
    
    # Data preparation
    traindata_x = train_data.drop([y_col_name], axis=1)
    traindata_y = train_data[y_col_name]

    validdata_x = valid_data.drop([y_col_name], axis=1)
    validdata_y = valid_data[y_col_name]

    dtrain = xgb.DMatrix(traindata_x, label=traindata_y)
    dvalid = xgb.DMatrix(validdata_x, label=validdata_y)

    # Model setting and training
    params = {
        'objective': 'binary:logistic',
        'gamma': gamma,
        'max_depth': max_depth,
        'subsample': subsample,
        'min_child_weight': min_child_weight,
        'scale_pos_weight': scale_pos_weight,
        'eta': eta,
        'seed': 42,
        'eval_metric': 'auc'
    }
    
    num_round = 100
    res = {}
    xgb_model = xgb.train(params, 
                          dtrain,
                          num_round,
                          evals=[(dtrain, "train"), (dvalid, "valid")], 
                          early_stopping_rounds=30, 
                          evals_result=res,
                          verbose_eval=False)
    
    xgb_model_final = xgb.train(params, 
                                dtrain,
                                xgb_model.best_iteration+1,
                                evals=[(dtrain, "train"), (dvalid, "valid")], 
                                evals_result=res,
                                verbose_eval=False)
    
    # Print the parameters used for model training
    print("Using the following parameters for model training:")
    print(f"y_col_name: {y_col_name}")
    print(f"gamma: {gamma}")
    print(f"max_depth: {max_depth}")
    print(f"subsample: {subsample}")
    print(f"min_child_weight: {min_child_weight}")
    print(f"scale_pos_weight: {scale_pos_weight}")
    print(f"eta: {eta}")

    xgb_model_final.save_model(xgb_model_path)

    return xgb_model_final

# Example usage
# xgb_model = xgb_model_train(train_data, valid_data, y_col_name='label',
#                             gamma=0, max_depth=6, subsample=0.7, min_child_weight=1, scale_pos_weight=1, eta=0.3)
