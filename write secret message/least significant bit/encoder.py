

def main():
    print("Insert the path to COVER IMAGE (grayscale recommended)")
    path = input(">> ")

    print("Type the message you want to embedd")
    message = input(">> ")

    path_sm = path.split(".")[0] + "_stego." + path.split(".")[1]

    sm_bytes = bytes(message, "UTF-8")
    sm_bits = list()

    for b in sm_bytes:
        cb = b
        for i in range(8):
            sm_bits.append(cb & 1)
            cb = cb >> 1

    print(sm_bits)


    with open(path, "rb") as cm:
        sm = open(path_sm, "wb")
        b = cm.read(14)     # starts after the header
        sm.write(b)

        i = 0
        for l in cm:
            c = bytearray()
            for b in l:
                if i < len(message):
                    c.append(b | sm_bits[i])
                    i += 1
                else:
                    c.append(b)

            sm.write(bytes(c))
        sm.close()


if __name__ == '__main__':
    main()