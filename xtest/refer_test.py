import pickle

data = pickle.load(open('refs(unc).p', 'rb+'))
print(data[0])
""" ref_id无所谓的，只是个排序
{
    "sent_ids": [
        0,
        1,
        2
    ],
    "file_name": "COCO_train2014_000000581857_16.jpg",
    "ann_id": 1719310,
    "ref_id": 0,
    "image_id": 581857,
    "split": "train",
    "sentences": [
        {
            "tokens": [
                "the",
                "lady",
                "with",
                "the",
                "blue",
                "shirt"
            ],
            "raw": "THE LADY WITH THE BLUE SHIRT",
            "sent_id": 0,
            "sent": "the lady with the blue shirt"
        },
        {
            "tokens": [
                "lady",
                "with",
                "back",
                "to",
                "us"
            ],
            "raw": "lady w back to us",
            "sent_id": 1,
            "sent": "lady with back to us"
        },
        {
            "tokens": [
                "blue",
                "shirt"
            ],
            "raw": "blue shirt",
            "sent_id": 2,
            "sent": "blue shirt"
        }
    ],
    "category_id": 1
}
"""