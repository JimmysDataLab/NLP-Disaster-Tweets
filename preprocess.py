import re
import numpy as np
import pandas as pd
from typing import Union

class PreProcess:
    

    def add_hashtags(text: str) -> Union[str, float]:
        tags = re.findall(r'#\w+', text)
        tags = ','.join([e.replace('#', '') for e in tags])
        tags = tags.lower()

        return tags if tags != '' else np.nan


    def add_mentions(text: str) -> Union[str, float]:
        tags = re.findall(r'@\w+', text)
        tags = ','.join([e.replace('@', '') for e in tags])

        return tags if tags != '' else np.nan


    def text_processing(text: str) -> str:
        # Remove links
        text = re.sub(r'http[s]?://\S+', '', text)
        text = re.sub(r'#\w+', '', text)
        text = re.sub(r'@\w+', '', text)
        text = text.lower()

        return text


    def preprocess(X: pd.DataFrame) -> pd.DataFrame:
        X_copy = X.copy()
        # extract hashtag words without hashtag
        X_copy['hashtags'] = X_copy['text'].apply(PreProcess.add_hashtags)
        # extract mention words
        X_copy['mentions'] = X_copy['text'].apply(PreProcess.add_mentions)
        # process text
        X_copy['gist'] = X_copy['text'].apply(PreProcess.text_processing)

        return X_copy[['keyword', 'location', 'hashtags', 'mentions', 'gist']]

    
if __name__ == '__main__':
    print('preprocess called directly')
    