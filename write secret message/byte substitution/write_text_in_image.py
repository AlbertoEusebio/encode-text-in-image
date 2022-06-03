

def main():
    img = input("Select the '.bmp' image you want to use for encoding(path): ")
    txt = input("Text: ")

    encoded_text_im = open("../assets/encoded_text_im.bmp", "wb")    # saves in a specific folder for reading
    i = 0
    k = 0
    with open(img, "rb") as f_im:
        b = f_im.read(5000)   # the first 10 lines of a bmp file are the ones we need
        encoded_text_im.write(b)

        l = f"{len(txt)}"
        sz = "0"*(4-len(l))+l
        encoded_text_im.write(bytes(sz, "utf-8"))  # writes the len of the text
        b = f_im.read(1)  # the first 10 lines of a bmp file are the ones we need
        encoded_text_im.write(bytes(txt[k], "utf-8"))
        i = 1
        k = 1
        while b:
            b = f_im.read(1)
            if i % 10 == 0 and k < len(txt):
                encoded_text_im.write(bytes(txt[k], "utf-8"))
                k += 1
            else:
                encoded_text_im.write(b)
            i += 1
        if k == len(txt):
            print("Success")
    encoded_text_im.close()


if __name__ == "__main__":
    main()