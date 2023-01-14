d = {"namel": "id1", "name2": "id2", "name3": "id3" }
d1 = {d[k]: k for k in d}
print(d1)