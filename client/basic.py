import requests

# res = requests.get('http://localhost:8000/api')
# res = requests.get('http://localhost:8000/api/data/', json={'name':"suman sharma"})
# res = requests.get('http://localhost:8000/api/params/',params={'id_num':"7802"}, json={'name':"suman sharma"})
res = requests.post('http://localhost:8000/api/post/', json={"roll_number":"28", "full_name":"suman sharma"})

print(res.text)