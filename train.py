import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt


def train(model, train_X_vec, train_y):
    epochs = 6
    learning_rate = 1e-3
    loss_fn = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)
    batch_size = 1024

    final_losses = []

    for i in range(epochs):
        
        batch_idx = 0

        while (batch_idx+1)*batch_size < train_X_vec.shape[0]:
            
            batch_X = train_X_vec[batch_idx*batch_size:(batch_idx+1)*batch_size].toarray()
            batch_y = train_y[batch_idx*batch_size:(batch_idx+1)*batch_size]
            y_pred = model.forward(torch.Tensor(batch_X))

            loss = loss_fn(y_pred, torch.Tensor(np.array(batch_y)))
            final_losses.append(loss)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            batch_idx += 1
            del batch_X
            del batch_y

            print(f'Epoch #{i+1}; Batch #{batch_idx+1}; Loss: {loss.item()}')

    torch.save(model, 'fake_model_l.pt')
    torch.save(model.state_dict(), 'fake_model_state_dict.pt')

    plt.plot(range(len(final_losses[:400])), final_losses[:400])
    plt.xlabel('Batches')
    plt.ylabel('Loss')
    plt.show()