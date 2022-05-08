def main():

    txt = ""

    with open("../assets/encoded_tex_im.bmp", "rb") as f_enc:
        f_enc.read(80)   # the first 80 bytes are the header and ignored
        b = f_enc.read(1)

        txt += str(b.decode("utf-8"))
        msg_over = False
        i = 1
        while b and not msg_over:
            b = f_enc.read(1)
            if i % 10 == 0:
                try:
                    txt += b.decode("utf-8")
                except:
                    msg_over = True
            i += 1

        print(txt)



if __name__ == "__main__":
    main()
