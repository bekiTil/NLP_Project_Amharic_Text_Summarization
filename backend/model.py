from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
class Model:
  """A model class to lead the model and tokenizer"""

  def __init__(self) -> None:
    pass
  
  def load_model():
    model = AutoModelForSeq2SeqLM.from_pretrained("Text-Summarization-Amharic-model")
    return model

  def load_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained("tokenizer")
    return tokenizer