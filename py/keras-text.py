from keras.preprocessing.text import Tokenizer

texts = ["I am a student. He is a student, too.", "She is not a student."]
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

print("与えられた文章の数 : ", tokenizer.document_count)
print("与えられた文章内の単語ごとの出現回数 : ", tokenizer.word_counts)
print(tokenizer.word_index)
