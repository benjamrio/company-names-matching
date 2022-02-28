from main import predict
import pandas as pd


def evaluate_acc(predictions, outputs):
    """Compute accuracy score by comparing two lists
    of same length element-wise

    Arguments:
        predictions {series} -- first list to be compared with the second one
        outputs {series} -- same length as predictions
    """
    assert len(predictions) == len(outputs), "Lists have different size"
    return (predictions == outputs).sum()/len(predictions)


def load_test_data():
    df = pd.read_csv("data/top500verifCom.tsv",
                     names=["companyName", "postCode", "city", "CA"], sep="\t")
    test_inputs = df["companyName"]
    return test_inputs, []


def main():
    siren_table_path = "data/siren_table.csv"
    test_inputs, test_outputs = load_test_data()
    predictions = predict(test_inputs, siren_table_path)
    print(pd.DataFrame(test_inputs, predictions))


if __name__ == "__main__":
    main()
