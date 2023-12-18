def main():
    text = input("Welke text wilt u hashen? ")
    hashes = []
    while text != "":
        opgeslagen = False
        toHash = text
        while not opgeslagen:
            newHash = hash(str(toHash))
            gelijkenis = False
            for prevText in hashes:
                if newHash == prevText["hashWaarde"]:
                    gelijkenis = True


            if gelijkenis:
                print(f"er was een hash collision{toHash}.{newHash}")
                toHash = newHash
                print(f"er was een hash collision{toHash}.{hash(newHash)}")
            else:
                hashes.append({"brontext": text,
                               "hashWaarde": newHash})
                opgeslagen = True
        text = input("Welke nieuwe text wilt u hashesn? niets om te stoppen.")
    print(hashes)


if __name__ == "__main__":
    main()

