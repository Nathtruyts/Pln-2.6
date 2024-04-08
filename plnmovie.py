import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.metrics.distance import edit_distance
from collections import Counter

nltk.download('movie_reviews')

corpus = movie_reviews.words()

freq_dist = Counter(corpus)

def corretor_ortografico(frase):

    palavras = word_tokenize(frase.lower())

    palavras_corrigidas = []
    for palavra in palavras:
        if palavra not in freq_dist:

            palavras_similares = [(edit_distance(palavra, palavra_corpus), palavra_corpus) for palavra_corpus in freq_dist]
            palavra_corrigida = min(palavras_similares)[1]
            palavras_corrigidas.append(palavra_corrigida)
        else:
            palavras_corrigidas.append(palavra)

    return ' '.join(palavras_corrigidas)


def verificar_correcao(frase_original, frase_corrigida):
    if frase_original == frase_corrigida:
        return "A frase parece estar correta."
    else:
        return f"Palavras potencialmente incorretas foram corrigidas: {frase_corrigida}"


def main():
    frase_usuario = input("Digite uma frase: ")

    frase_corrigida = corretor_ortografico(frase_usuario)

    resultado = verificar_correcao(frase_usuario, frase_corrigida)

    print(resultado)


if __name__ == "__main__":
    main()
