from sklearn.impute import SimpleImputer
def imputation_moyenne(df, colonne):
    imputer = SimpleImputer(strategy='mean')
    df[[colonne]] = imputer.fit_transform(df[[colonne]])
    return df

def imputation_mediane(df, colonne):
    imputer = SimpleImputer(strategy='median')
    df[[colonne]] = imputer.fit_transform(df[[colonne]])
    return df