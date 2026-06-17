import numpy as pi

rdm = pi.random.default_rng()
emojis = pi.array(["🙂", "😁", "😭", "🫠", "😝", "💀"])
emoji = rdm.choice(emojis, size=(3, 3))
print(emoji)
