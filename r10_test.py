import ray
import pickle

df = pickle.load(open('./artifacts/cnn_mnist/example_mnist_agingevosearch_state.pickle', 'rb'))

# pickle.dump(df, open('out.txt', 'wb'))

# with open('out.txt', 'wb') as out:
#     out.write(print(df))

print(df)