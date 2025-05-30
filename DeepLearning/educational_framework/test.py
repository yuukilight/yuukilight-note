from core import Operation, Placeholder, Node, Linear, _default_graph, Session
from tmp import view_graph
import numpy as np



if __name__ == "__main__":
    X = Placeholder()
    fc = Linear(13, 1, bias=True, act="sigmoid")
    out = fc(X)

    print("before forward:", out)
    session = Session()
    session.run(root_op=out, feed_dict={X : np.random.randn(1, 13)})
    print("after forward: ", out)