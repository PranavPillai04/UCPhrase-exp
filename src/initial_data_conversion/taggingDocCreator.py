import json

input_file = "/shared/data2/ppillai3/test/UCPhrase-exp/data/kpWater/standard/preprocess-cs_roberta_base/annotate.CoreAnnotator/tokenized.kpWater.train.jsonl"
output_file = "/shared/data2/ppillai3/test/UCPhrase-exp/data/kpWater/standard/kpWater.tagging.human_0.json"

# data = JsonLine.load(input_file)
with open(input_file) as rf:
    lines = rf.read().splitlines()
data = [json.loads(l) for l in lines]


output_data = {}
for i in range(len(data)):
    asin = data[i]['_id_']
    phrases = []
    
    sents = data[i]['sents']
    for sent in sents:
        try:
            cleaned_phrases_entry = []
            phrases_entry = sent['phrases']
            for phrase in phrases_entry:
                # if (asin == "B0814BBV3W"):
                cleaned_phrase = [phrase[0][0], phrase[0][1], phrase[1]]
                phrases.append(cleaned_phrase)            
            # phrases.append(cleaned_phrases_entry)
        except:
            pass
    if (asin == "B0814BBV3W"):
        print(phrases)

    output_data[asin] = (phrases)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)