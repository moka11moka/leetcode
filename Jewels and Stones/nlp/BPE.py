import collections
import re
vocab = {'l o w </w>': 5, 'l o w e r </w>': 2, 'n e w e s t </w>': 6, 'w i d e s t </w>': 3}

def get_stats(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        alphas = word.split()
        for i in range(len(alphas)-1):
            pairs[alphas[i], alphas[i+1]] += 1
    return pairs

def merge_voc(pairs, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pairs))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pairs), word)
        v_out[w_out] = v_in[word]
    return v_out

num_merges = 100
for i in range(num_merges):
    print('----'*30)
    print(vocab)
    pairs = get_stats(vocab)
    if not pairs:
        break
    best = max(pairs, key=pairs.get)
    vocab = merge_voc(best, vocab)
    #print(best)
