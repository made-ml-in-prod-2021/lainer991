import pandas as pd
from sklearn.preprocessing import StandardScaler


def get_features_labels(X):
    cols_df = X.nunique().to_frame().reset_index()
    cols_df = cols_df.rename(columns={'index': 'column_name', 0: 'num_uniq'})

    all_feats = cols_df['column_name'].tolist()
    cat_feats = cols_df[cols_df['num_uniq'] < 10]['column_name'].tolist()
    num_feats = [x for x in all_feats if x not in cat_feats]

    return cat_feats, num_feats


def one_hot_transform(X, cat_feats):
    for i in cat_feats:
        X[i] = X[i].astype('str')

    one_hot_part = pd.get_dummies(X[cat_feats], prefix=cat_feats)
    return one_hot_part


def scaling_transform(X, num_feats):
    st_scaler = StandardScaler()
    scaling_part = pd.DataFrame(st_scaler.fit_transform(X[num_feats]))
    scaling_part.columns = num_feats

    return scaling_part


def full_transform(X):
    cat_cols, num_cols = get_features_labels(X)
    hot = one_hot_transform(X, cat_cols)
    scal = scaling_transform(X, num_cols)
    full_transformed_df = pd.concat([hot, scal], axis=1)
    return full_transformed_df
