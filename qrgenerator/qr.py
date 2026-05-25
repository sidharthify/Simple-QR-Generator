import qrcode




print("===== QR GENERATOR =====\n")

print("Enter Your Link (Youtube/Tiktok/etc.)")
link = input("> ")
img = qrcode.make(link)
type(img)
user_filename = input("Enter QR code file name: ")
img.save(f"{user_filename}.png")

print("QR Generated Successfully!")


 
