from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch


class PegasusClass:

    def __init__(self):
        model_name = ""
        tokenizer = ""
        model = PegasusForConditionalGeneration

    def redditTifuModel(self):
        self.model_name = 'google/pegasus-reddit_tifu'  # ABSTRACTIVE
        torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.tokenizer = PegasusTokenizer.from_pretrained(self.model_name)
        self.model = PegasusForConditionalGeneration.from_pretrained(
            self.model_name).to(torch_device)

    def predictText(self, src_text):
        src_text = [src_text]
        torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        batch = self.tokenizer.prepare_seq2seq_batch(
            src_text, truncation=True, padding='longest', return_tensors='pt').to(torch_device)
        translated = self.model.generate(**batch)
        tgt_text = self.tokenizer.batch_decode(
            translated, skip_special_tokens=True)
        return tgt_text
