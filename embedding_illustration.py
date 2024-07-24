"""
@author: tsdj

"""


import torch
import torchtext

from torch import Tensor
from sklearn.manifold import TSNE

import numpy as np

from matplotlib import pyplot as plt


def find_corresponding(
        vocab: torchtext.vocab.Vectors,
        starting_word: str,
        subtraction_word: str | None = None,
        addition_word : str | None = None,
        subtraction_weight: float = 1.0,
        addition_weight: float = 1.0,
        ) -> str:
    qvec = vocab.vectors[vocab.stoi[starting_word]]

    if subtraction_word is not None:
        qvec = qvec - subtraction_weight * vocab.vectors[vocab.stoi[subtraction_word]]

    if addition_word is not None:
        qvec = qvec + addition_weight * vocab.vectors[vocab.stoi[addition_word]]

    distances = torch.sum((vocab.vectors - qvec) ** 2, dim=1)
    closest = torch.argmin(distances)

    return vocab.itos[closest]


def get_tsne_embeddings(
        embeddings: np.ndarray,
        dimensions: int = 2,
        ):
    assert 2 <= dimensions <= 3, dimensions

    tsne = TSNE(n_components=dimensions, random_state=0)

    tsne_embeddings = tsne.fit_transform(embeddings)

    # Scale vectors to uniform length (easier to visualize)
    lens = sum(tsne_embeddings[:, i] ** 2 for i in range(dimensions)) ** 0.5

    tsne_embeddings_s = tsne_embeddings.copy()
    tsne_embeddings_s[:, 0] /= lens
    tsne_embeddings_s[:, 1] /= lens

    if dimensions == 3:
        tsne_embeddings_s[:, 2] /= lens

    return tsne_embeddings, tsne_embeddings_s


def draw_arrow(
        x_coord: float,
        y_coord: float,
        color: str,
        label: str,
        linestyle: str = '-',
        x_base: float = 0.0,
        y_base: float = 0.0,
        ):
    plt.arrow(
        x=x_base,
        y=y_base,
        dx=x_coord,
        dy=y_coord,
        color=color,
        linestyle=linestyle,
        label=label,
        length_includes_head=True,
        )


def arrow_plot(
        vocab: np.ndarray | Tensor,
        embeddings: np.ndarray,
        starting_word: str,
        subtraction_word: str,
        addition_word : str,
        target_word: str,
        xlim_lower: float = 0,
        ylim_lower: float = 0,
        xlim_upper: float | None = None,
        ylim_upper: float | None = None,
        draw_new: bool = True,
        draw_direction: bool = False,
        fname: str | None = None,
        ):
    embedding_startw = embeddings[vocab.stoi[starting_word]]
    embedding_subq = embeddings[vocab.stoi[subtraction_word]]
    embedding_addw = embeddings[vocab.stoi[addition_word]]
    embedding_tarw = embeddings[vocab.stoi[target_word]]

    direction = embedding_addw - embedding_subq
    new = embedding_startw + direction

    fig, ax = plt.subplots()

    draw_arrow(*embedding_startw, color='blue', label=starting_word)
    draw_arrow(*embedding_subq, color='gray', label=subtraction_word)
    draw_arrow(*embedding_addw, color='green', label=addition_word)
    draw_arrow(*embedding_tarw, color='orange', label=target_word)

    if draw_new:
        draw_arrow(*new, color='red', label=f'{starting_word} + {addition_word} - {subtraction_word}')

    if draw_direction:
        draw_arrow(*direction, color='purple', label=f'{addition_word} - {subtraction_word}', x_base=embedding_startw[0], y_base=embedding_startw[1])

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.grid(True)

    ax.set_xlim(xlim_lower, xlim_upper)
    ax.set_ylim(ylim_lower, ylim_upper)

    plt.legend()

    if fname is not None:
        plt.savefig(fname, dpi=400)

    plt.show()


def main():
    vocab = torchtext.vocab.GloVe(name='6B', dim=50)

    # Equal weights
    find_corresponding(vocab, 'father', 'man', 'woman')
    find_corresponding(vocab, 'brother', 'man', 'woman')
    find_corresponding(vocab, 'son', 'boy', 'girl')
    find_corresponding(vocab, 'paris', 'france', 'italy')

    # With some tweaking
    find_corresponding(vocab, 'king', 'man', 'woman', addition_weight=1.3)
    find_corresponding(vocab, 'prince', 'man', 'woman', addition_weight=1.3)

    # 2d t-SNE embeddings for 10,000 most common "words" (tokens)
    embeddings_50d = np.array([vocab.vectors[i].numpy() for i in range(10_000)])
    tsne_embeddings, tsne_embeddings_s = get_tsne_embeddings(embeddings_50d, 2)

    # Illustrating father - man + woman = mother
    arrow_plot(vocab, tsne_embeddings_s, 'father', 'man', 'woman', 'mother', draw_new=False, fname='./figs/father-to-mother-1.png')
    arrow_plot(vocab, tsne_embeddings_s, 'father', 'man', 'woman', 'mother', xlim_lower=0.6, ylim_lower=0.6, xlim_upper=0.75, ylim_upper=0.75, draw_new=False, fname='./figs/father-to-mother-2.png')
    arrow_plot(vocab, tsne_embeddings_s, 'father', 'man', 'woman', 'mother', xlim_lower=0.6, ylim_lower=0.6, xlim_upper=0.75, ylim_upper=0.75, draw_new=False, draw_direction=True, fname='./figs/father-to-mother-3.png')
    arrow_plot(vocab, tsne_embeddings_s, 'father', 'man', 'woman', 'mother', xlim_lower=0.6, ylim_lower=0.6, xlim_upper=0.75, ylim_upper=0.75, draw_new=True, draw_direction=True, fname='./figs/father-to-mother-4.png')

    # Illustrating son - man + woman = daugther
    arrow_plot(vocab, tsne_embeddings_s, 'son', 'man', 'woman', 'daughter', draw_new=False, fname='./figs/son-to-daughter-1.png')
    arrow_plot(vocab, tsne_embeddings_s, 'son', 'man', 'woman', 'daughter', xlim_lower=0.6, ylim_lower=0.6, xlim_upper=0.75, ylim_upper=0.75, draw_new=False, fname='./figs/son-to-daughter-2.png')
    arrow_plot(vocab, tsne_embeddings_s, 'son', 'man', 'woman', 'daughter', xlim_lower=0.6, ylim_lower=0.6, xlim_upper=0.75, ylim_upper=0.75, draw_new=False, draw_direction=True, fname='./figs/son-to-daughter-3.png')
    arrow_plot(vocab, tsne_embeddings_s, 'son', 'man', 'woman', 'daughter', xlim_lower=0.6, ylim_lower=0.6, xlim_upper=0.75, ylim_upper=0.75, draw_new=True, draw_direction=True, fname='./figs/son-to-daughter-4.png')

    # Illustrating Paris to Rome (not perfect in 2d, works in 50d)
    arrow_plot(vocab, tsne_embeddings_s, 'paris', 'france', 'italy', 'rome', draw_new=False, fname='./figs/paris-to-rome-1.png')
    arrow_plot(vocab, tsne_embeddings_s, 'paris', 'france', 'italy', 'rome', xlim_lower=0.55, ylim_lower=0.6, xlim_upper=0.75, ylim_upper=0.85, draw_new=False, fname='./figs/paris-to-rome-2.png')
    arrow_plot(vocab, tsne_embeddings_s, 'paris', 'france', 'italy', 'rome', xlim_lower=0.55, ylim_lower=0.6, xlim_upper=0.75, ylim_upper=0.85, draw_new=False, draw_direction=True, fname='./figs/paris-to-rome-3.png')
    arrow_plot(vocab, tsne_embeddings_s, 'paris', 'france', 'italy', 'rome', xlim_lower=0.55, ylim_lower=0.6, xlim_upper=0.75, ylim_upper=0.85, draw_new=True, draw_direction=True, fname='./figs/paris-to-rome-4.png')

    #
    arrow_plot(vocab, tsne_embeddings_s, 'doctor', 'hospital', 'school', 'teacher', draw_new=False, xlim_lower=-1)
    arrow_plot(vocab, tsne_embeddings_s, 'doctor', 'hospital', 'school', 'teacher', draw_new=False, draw_direction=True, xlim_lower=-1)


if __name__ == '__main__':
    main()
