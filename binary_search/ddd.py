import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))


if __name__ == '__main__':
    lines = ["3 3000
                395 15425
                3500 -2934
                5000 1283"]
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)