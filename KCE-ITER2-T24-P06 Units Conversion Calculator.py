p = None
ch = None

def units_calc(expr):
    expr = expr.replace('+', '  +  ')
    expr = expr.replace('-', '  -  ')
    parts = expr.split()
    result = float(0)
    sign = 1
    for p in parts:
        if p == "+":
            sign = 1
        elif p == "-":
            sign = -1
        else:
            num = ""
            unit = ""
            for ch in p:
                if ch.isdigit() or ch == ".":
                    num += ch
                elif ch.isalpha():
                    unit += ch
            if unit == "m":
                value = float(num)
            elif unit == "cm":
                value = float(num) / 100
            elif unit == "km":
                value = float(num) * 1000
            else:
                print("invalid input")
                value = 0
            result += sign * value
    return result

if __name__ == "__main__":
    print("Enter expressions (blank to quit)")
    while True:   # run until blank input
        line = input("> ").strip()
        if line == "":
            break
        try:
            print("= ", units_calc(line), "meters")
        except Exception as e:
            print("Error:", e)
