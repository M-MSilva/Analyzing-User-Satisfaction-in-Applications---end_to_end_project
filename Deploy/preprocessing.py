#we create a preprocessing layer
import string
import tensorflow as tf
from tensorflow import keras
@tf.keras.utils.register_keras_serializable()
def custom_standardization(initial_string):
    """ Remove everything that is not a character or string in the data """

    no_uppercased = tf.strings.lower(initial_string, encoding='utf-8')

    Aux_data = tf.strings.regex_replace(no_uppercased, rb"<br\s*/?>", b" ")

    change_token = tf.strings.regex_replace(Aux_data, "[UNK]", b"True")

    Clean_data = tf.strings.regex_replace(change_token, b"[^a-zA-Z']", b" ")    
    
    no_punctuations = tf.strings.regex_replace(Clean_data, f"([{string.punctuation}])", r" ")


    return no_punctuations
