S = input()

dashboard = {
    ":-)": 0,
    ":-(": 0
}


for imoji in [":-)", ":-("]:
    for idx in range(len(S)-3):
        if S[idx:idx+3] == imoji:
            dashboard[imoji] += 1


if dashboard[":-)"] > dashboard[":-("]:
    print("happy")
elif dashboard[":-)"] < dashboard[":-("]:
    print("sad")
elif dashboard[":-)"] != 0 and dashboard[":-)"] == dashboard[":-("]:
    print("unsure")
else:
    print("none")
