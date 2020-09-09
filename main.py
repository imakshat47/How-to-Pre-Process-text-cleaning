import re
import preprocessing as prep
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
from textblob import TextBlob


def make_textString(text):
    # convert tokens to a single blob of text
    return ' '.join(text) + "\n"

# save list to file


def save_list(data, filename):
    # open file
    file = open(filename, 'a', encoding='UTF')
    # write text
    file.write(data)
    # close file
    file.close()

# Initiate's Pre Processing


def process_init(text):
    try:
        #  Convert text to lower
        lower_text = text.lower()
        # Handle Emojis
        emojis_text = prep.handle_emojis(lower_text)
        # Cleaning text
        processed_text = prep.preprocess_text(emojis_text)

        # tokenize
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(processed_text)

        # remove remaining tokens that are not alphabetic
        tokens = [word for word in tokens if word.isalpha()]

        # filter out stop words
        stop_words = set(stopwords.words('english'))
        tokens = [w for w in tokens if not w in stop_words]

        # tokens = [word for word in tokens if len(word) > 1]

        return tokens

    except Exception:
        pass


def return_sentiment(text):
    polar = TextBlob(text).sentiment.polarity

    if polar > 0:
        if polar > 0.3:
            print("Positive")
        else:
            print("Neutral")
    elif polar < 0:
        if polar < -0.3:
            print("Negative")
        else:
            print("Neutral")
    else:
        print("Neutral")


if __name__ == "__main__":
    print("Pre Processiong ... \n")

    text_list = [
        "haan bhai I will be there don't worry",
        "सरकार ने देश के लोगों को एक बार फिर से गिरा दिया है कब तक चलेगा तु? कितिनी भ्रष्टाचार हो राय है",
        "PUBG MOBILE SEASON 15 OFFICIAL ROYALE PASS REWARDS ",
        "@PUBGMOBILE merhabalar facebook hesab\u0131m hacklendi. Facebook hesab\u0131ma eri\u015femiyorum. Facebook yetkilileri covid 19 da\u2026 https://t.co/8QeBv4Ci3x",
        "RT @IreshaMadhusha9: \ud83d\udd3bAkshay Kumar's name was found in Sushant's diary.\n\ud83d\udd3b SSR was working on AI game &amp; covid app.\n\ud83d\udd3bHis data was stolen on 8\u2026",
        "I havv goood speling!",
        'RT @SteffiDHFM: Indians PubG aadatam valla china ki 1.12 lak crores income anta.\nCovid tho prapanchaanni SarvaNashanam chesina china ki mir\u2026'
    ]

    for text in text_list:
        # Initiate Pre-Processing
        preprocessed_text = process_init(text)
        # Make Tokens list => String
        preprocessed_string = make_textString(preprocessed_text)
        # writes tweet String to file
        save_list(preprocessed_string, 'output.txt')
        # Prints tweets
        print(preprocessed_string, end =" => ")        
        # return Sentiment of tweet
        return_sentiment(preprocessed_string)

    print('\nDone!!')
