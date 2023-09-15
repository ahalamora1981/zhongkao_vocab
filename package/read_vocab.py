import pandas as pd
import os

from resource.zhongkao_vocab import zhongkao_vocab


vocab = zhongkao_vocab

def read_vocab(vocab_file='resource/zhongkao_vocab.csv'):
    if vocab_file not in os.listdir('resource'):
        with open(vocab_file, 'w') as f:
            f.write(vocab)
            
    df = pd.read_csv(vocab_file)
    df = df[['英文', '中文']]

    return df

if __name__ == '__main__':
    print(read_vocab())