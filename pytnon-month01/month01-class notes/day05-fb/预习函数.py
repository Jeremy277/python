#1.定义询问yes or no 的函数:
def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

go_first = ask_yes_no("你希望先走第一步棋吗？ (y/n): ")
if go_first == "y":
    print("\n你走第一步棋。")
else:
    print("\n你很勇敢，我先来。.")

#2.定义函数: