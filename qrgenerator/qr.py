import qrcode

def main():
    print("===== QR GENERATOR =====\n")
    print("Enter Your Link (Youtube/Tiktok/etc.)")
    link = input("> ")
    
    if not link:
        print("Link cannot be empty.")
        return
        
    img = qrcode.make(link)
    
    user_filename = input("Enter QR code file name (without extension): ")
    if not user_filename:
        print("File name cannot be empty.")
        return
        
    img.save(f"{user_filename}.png")
    print("QR Generated Successfully!")

if __name__ == "__main__":
    main()
