"zomato_order"

order_price = input("enter your zamato order price: ")
price = float(order_price)

gst = price * 18/100

final_price = price + gst

print("Order price: ", price)
print("GST(18%): ", gst)
print("final bill amount :", final_price)