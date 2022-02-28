import pandas as pd


def find_siren(companyName, df):
    try:
        siren = df[df["companyName"] == companyName][0]
    except:
        siren = 0
    return siren


def predict(companies, siren_table_path):
    """Predict siren number of companies based on links
    established in the siren table

    Arguments:
        companies {list of strings} -- list of company names
        siren_table_path {string} -- path of the table containing the bijection between names and siren numbers

    Returns:
        DataFrame -- 2 columns df : companyName, predictedSiren
    """
    siren_df = pd.read_csv(siren_table_path)
    result_df = pd.DataFrame()
    for company in companies:
        result_df.loc[company, "predictedSiren"] = find_siren(
            company, siren_df)
    return result_df
