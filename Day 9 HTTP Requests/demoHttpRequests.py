# https://jsonplaceholder.typicode.com/posts
# https://jsonplaceholder.typicode.com/posts/i/comments
import requests
respon = requests.get("http://localhost:3000/posts")
# print(respon.status_code)

json = respon.json()
# print(json)
# print(json["name"])
# print(json)

test = map(lambda a: a["title"], json)
# listdata = []
# for a in json:
#   listdata.append(a["title"])
# print(list(test))
# print(listdata)

# data_new = {}
# data_new["title"] = "sql server"
# data_new["author"] = "abi"
# post_comments = requests.post("http://localhost:3000/posts", data=data_new)
# post_comments.raise_for_status()


data = {}
data["id"] = 2
query = requests.get("https://jsonplaceholder.typicode.com/comments", params=data)
print("\n")
print(query.json())

