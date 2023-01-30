story1 = {
    "start":"One day Ilyas was playing football at the park and he was feeling unwell. He had a severe headache and was constantly in his own head second guessing his decisions on the pitch.",
    "middle":"He ended up realising these voices weren't his own but he was actually telepathic reading the minds of his opponents! Ilyas started going by Mystique and began working with the police and other agencies to make the world a better place and quickly became a household name for his heroic acts and incredible superpower.?",
    "end":"As he aged Mystique retired from his duties having inspired the younger generation of heroes and having made the world a safer place."
}
print(story1.items())
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1.get("start"))
print(story1.get("middle"))
print(story1.get("start"))
story1["hero"] = "Mystique"