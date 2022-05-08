def main():

    txt = ""

    with open("../assets/encoded_text_im.bmp", "rb") as f_enc:
        f_enc.read(5000)   # the first 80 bytes are the header and ignored

        sz = int(f_enc.read(4).decode("utf-8"))  # reads the len
        print("Len of message: ", sz)

        b = f_enc.read(1)
        txt += str(b.decode("utf-8"))
        msg_over = False
        i = 1
        k = 1
        while b and not msg_over and k < sz:
            b = f_enc.read(1)
            if i % 10 == 0:
                try:
                    txt += b.decode("utf-8")
                    k += 1
                except:
                    msg_over = True
            i += 1

        print(txt)



if __name__ == "__main__":
    main()
