import json
import requests

r = requests.get("https://www.dcard.tw/service/api/v2/forums/food/posts?popular=true&limit=10")
apple = json.loads(r.text)
for a in apple:
    banana = {"Title:" : a['title'],
            "Topic:" : a['topics'],
            "Gender" : a['gender'],
            "School" : a['school']}
    with open("b.json", "a", encoding="utf-8") as f:
        json.dump(banana, f, ensure_ascii=False)
        f.write("\n")