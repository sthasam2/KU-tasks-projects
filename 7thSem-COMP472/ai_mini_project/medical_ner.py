import sys
import pprint
import spacy
import spacy_stanza

from spacy import displacy
from spacytextblob.spacytextblob import SpacyTextBlob


def extract_data(filename):
    """
    Extract Data from a given record
    """

    with open(filename, "r") as inp:
        file_content = inp.read()

    ner_pipeline = spacy_stanza.load_pipeline(
        "en",
        processors={
            "ner": [
                "i2b2",
                "radiology",
                "ontonotes",
            ],
            "tokenize": "combined",
        },
        package="",
    )

    sentiment_pipeline = spacy.load("en_core_web_lg")
    sentiment_pipeline.add_pipe("spacytextblob")

    ner_doc = ner_pipeline(file_content)
    sentiment_doc = sentiment_pipeline(file_content)

    extracted_record = {}
    for entity in ner_doc.ents:
        if entity.label_ in extracted_record:
            if str(entity) not in extracted_record[entity.label_]:
                extracted_record[entity.label_].append(str(entity))
        else:
            extracted_record[entity.label_] = [str(entity)]

    extracted_record["SENTIMENT"] = round(sentiment_doc._.blob.polarity, 5)

    return extracted_record


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: medical_ner.py <filename>")
    else:
        pprint.pprint(extract_data(sys.argv[1]))