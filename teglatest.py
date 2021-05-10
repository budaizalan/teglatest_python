def main() -> None:

    a = int(input("Kérem a téglalap a oldalát:"))
    b = int(input("Kérem a téglalap b oldalát:"))
    c = int(input("Kérem a téglalap c oldalát:"))

    terfogat = a*b*c
    felszin = 2*(a*b+a*c+b*c)

    print("A téglalap térfogat(V):", terfogat ("m3")
    print("A téglalap felszíne(A):", felszin ("m2")


if __name__ == "__main__":
    main()
