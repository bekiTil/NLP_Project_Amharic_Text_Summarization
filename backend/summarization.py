import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import pipeline, set_seed
# tokenizer = AutoTokenizer.from_pretrained("tokenizer")
# model_name = "csebuetnlp/mT5_multilingual_XLSum"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# pipe = pipeline('summarization', model = model_name )
# model_name = "csebuetnlp/mT5_multilingual_XLSum"
tokenizer = AutoTokenizer.from_pretrained("backend/tokenizer")
model = AutoModelForSeq2SeqLM.from_pretrained("backend/Text-Summarization-Amharic-model")

input_ids = tokenizer(
    ["የኢትዮጵያ የፖለቲካ ፓርቲዎች የጋራ ም/ቤት በኢትዮጵያና በሶማሊላንድ መካከል የተደረሰውን ስምምነት እንደሚደግፍ አስታወቀ፡፡ምክር ቤቱ ዛሬ ሐሙስ ባወጣው መግለጫ “ለስምምነቱ ውጤታማነት በጋራ በመቆም ሚናችንን ለመወጣት ያለንን ቁርጠኝነት ዳግም እናረጋግጣለን” ብሏል፡፡ መንግሥት ስምምነቱን “ውጥረቶችን በሚያረግብ እና ሀገሪቱን ለጉዳት በማያጋልጥ መንገድ” ተግባራዊ ማድረግ እንዳለበትም ፓርቲዎቹ አሳስበዋል፡፡"],
    return_tensors="pt",
    padding="max_length",
    truncation=True,
    max_length=512
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    max_length=84,
    no_repeat_ngram_size=2,
    num_beams=4
)[0]

summary = tokenizer.decode(
    output_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)
print(summary)
# from transformers import AutoModelForSequenceClassification, TFAutoModelForSequenceClassification, AutoTokenize

# class Model:
#   """A model class to lead the model and tokenizer"""

#   def __init__(self) -> None:
#     pass
  
#   def load_model():
#     model = AutoModelForSequenceClassification.from_pretrained("./models/roberta-base/")
#     return model

#   def load_tokenizer():
#     tokenizer = AutoTokenize.from_pretrained("./models/roberta-base/")
#     return tokenizer