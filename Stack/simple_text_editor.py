# Simple text editor

def simple_text_editor():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    q = int(data[0])
    s = ""
    history = []

    for i in range(1, q + 1):
        parts = data[i].split()
        op = parts[0]

        if op == "1":
            # append
            history.append(s)
            s += parts[1]
        elif op == "2":
            # delete
            history.append(s)
            k = int(parts[1])
            s = s[:-k]
        elif op == "3":
            # print
            k = int(parts[1])
            print(s[k - 1])
        elif op == "4":
            # undo
            s = history.pop()

# Run the function
simple_text_editor()
