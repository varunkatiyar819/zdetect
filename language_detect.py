def compare_scores(model_output, actual_output):
    with open(actual_output, "r") as f1, open(model_output, "r") as f2:
        actual = f1.readlines()
        model = f2.readlines()
        score = [x.strip()==y[:12] for x, y in zip(actual, model)]
        accuracy = (sum(score)/len(actual))
        print("accuracy - ", accuracy)

compare_scores("output.txt", "actual_output.txt")