def test(name,web_site,age):
    print(name)
    print(web_site)
    print(age)

info ={
    "name":"王老师",
    "web_site":"www.1234.com",
    "age":13
}

test(**info)