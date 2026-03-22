# Topic : Dictionary Comprehension
name = ["priya","keerthi"]
d = {n:len(n) for n in name}
print(d)

cities = {"bengaluru":40,
          "mysuru": 19,
          "mangalore":22}
c = {ci:pop for ci,pop in cities.items() if pop > 20}
print(c)