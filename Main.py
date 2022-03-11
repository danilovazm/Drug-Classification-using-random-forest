import argparse
from sklearn.ensemble import RandomForestClassifier
from PreProcess import preProcessAndSplit

def main(args):
    x_train, y_train, x_test, y_test = preProcessAndSplit(args.path)
    RF = RandomForestClassifier(criterion=args.criterion, max_depth=args.depth)
    RF.fit(x_train, y_train)
    score = RF.score(x_test, y_test)
    print(f"O modelo teve uma acuracia total de {score}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='./drug200.csv')
    parser.add_argument('--criterion', type=str, default='gini')
    parser.add_argument('--depth', type=int, default=None)

    args = parser.parse_args()
    main(args)