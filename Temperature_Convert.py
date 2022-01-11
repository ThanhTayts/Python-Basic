def CtoFConverter():
    while True:
        cTemp = input("Please enter C degree ")
        if cTemp:
            cTemp = float(cTemp)
            fTemp = cTemp*1.8 + 32
            print(f"{cTemp}C Temperature is {fTemp}F")
            break # dung break de thoat vong lap
    
        else:
            print("cTemp input is empty")
            continue # dung continue de tiep tuc vong lap    
        
def main():
    CtoFConverter()

if __name__ == "__main__":
    main()    