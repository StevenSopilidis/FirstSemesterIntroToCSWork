import random, hashlib
am="21153"
tmp=hashlib.sha256(am.encode()).hexdigest()
seed=int(tmp,16)
random.seed(seed)
lst=list(range(1,13))
random.shuffle(lst)
print(lst[:4])