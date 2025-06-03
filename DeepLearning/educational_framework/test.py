if __name__ == "__main__":
    import sys
    sys.path.append(r"d:\\data\\yuukilight-note\\DeepLearning")
    from sklearn.datasets import fetch_california_housing
    from sklearn.datasets import fetch_openml
    import matplotlib.pyplot as plt
    import numpy as np

    from educational_framework import Placeholder, dnn, measure, Session
    from educational_framework.optimizer import SGD

    from educational_framework import view

    # X, Y = fetch_california_housing(return_X_y=True)
    X, Y = fetch_openml(name="boston", version=1, as_frame=True, return_X_y=True, parser="pandas")
    X = X.to_numpy()
    Y = Y.to_numpy()
    X = X.astype(np.float64)
    Y = Y.astype(np.float64)

    np.random.seed(123)
    sample_num = X.shape[0]
    ratio = 0.8
    offline = int(ratio * sample_num)
    indexes = np.arange(sample_num)
    np.random.shuffle(indexes)

    train_X, train_Y = X[indexes[:offline]], Y[indexes[:offline]].reshape([-1, 1])
    test_X, test_Y = X[indexes[offline:]], Y[indexes[offline:]].reshape([-1, 1])
    # from sklearn.model_selection import train_test_split
    # train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.3, random_state=1001)


    X = Placeholder()
    Y = Placeholder()

    out1 = dnn.Linear(13, 8, act="relu")(X)
    out2 = dnn.Linear(8, 4, act=None)(out1)
    out3 = dnn.Linear(4, 1, act=None)(out2)

    loss = measure.mean_square_error(predict=out3, label=Y)

    session = Session()
    optimizer = SGD(learning_rate=1e-8)

    losses = []
    for epoch in range(30):
        session.run(root_op=loss, feed_dict={X : train_X, Y : train_Y})
        losses.append(loss.numpy)
        optimizer.minimize(loss)
        print(f"\033[32m[Epoch:{epoch}]\033[0m loss:{loss.numpy}")

    session.run(root_op=loss, feed_dict={X : test_X, Y : test_Y})
    view.view_graph()
    predict = out3.numpy

    plt.style.use("seaborn")
    plt.subplot(1, 2, 1)
    plt.plot(losses, "-o")
    plt.xlabel("number of iteration")
    plt.ylabel("mean loss")
    plt.grid(True)
    plt.subplot(1, 2, 2)
    plt.plot(test_Y.reshape(-1), "r", label="ground truth", alpha=0.5, linewidth=3.)
    plt.plot(predict.reshape(-1), "b.", label="predict", alpha=0.5)
    plt.xlabel("sample id")
    plt.ylabel("price")
    plt.legend()
    plt.grid(True)
    plt.show()