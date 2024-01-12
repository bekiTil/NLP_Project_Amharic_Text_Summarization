from model import Model

class SummarizationModel:
  def __init__(self):
    self.model = Model.load_model()
    self.tokenizer = Model.load_tokenizer()

  def get_summary(self, text: str):
    input_ids = self.tokenizer(
    [text],
    return_tensors="pt",
    padding="max_length",
    truncation=True,
    max_length=512)["input_ids"]

    output_ids = self.model.generate(
        input_ids=input_ids,
        max_length=84,
        no_repeat_ngram_size=2,
        num_beams=4
    )[0]

    summary = self.tokenizer.decode(
        output_ids,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )
    return summary