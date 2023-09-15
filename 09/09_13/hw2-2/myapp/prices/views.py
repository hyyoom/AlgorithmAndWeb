from django.shortcuts import render

# Create your views here.

def price(r,thing,cnt):
    # print(thing, cnt)
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    
    if thing in product_price:
        price = product_price[thing] * cnt

    if thing in product_price:
        context={
            'thing' : thing,
            'cnt' : cnt,
            'product_price' : product_price,
            'price' : price,
        }
    else:
        context={
            'price' : "asdf",
            'thing' : thing,
            # 'cnt' : cnt,
            # 'product_price' : product_price,
        }
    return render(r, "prices/price.html",context)