# -*- coding: utf8 -*-
import os
from BDRApi import BDRAClient

_ocr_image = '''/9j/4AAQSkZJRgABAQEAYABgAAD/4QCoRXhpZgAATU0AKgAAAAgABQESAAMAAAABAAEAAAExAAIA
AAAVAAAASgEyAAIAAAAUAAAAYAITAAMAAAABAAEAAIdpAAQAAAABAAAAdAAAAABBQ0QgU3lzdGVt
cyDK/cLrs8nP8QAAMjAxNTowNjoxMiAxNDo1NzoyMAAAA5KQAAIAAAAENTA0AKACAAQAAAABAAAA
86ADAAQAAAABAAAATgAAAAAAAP/bAEMAAgEBAgEBAgICAgICAgIDBQMDAwMDBgQEAwUHBgcHBwYH
BwgJCwkICAoIBwcKDQoKCwwMDAwHCQ4PDQwOCwwMDP/bAEMBAgICAwMDBgMDBgwIBwgMDAwMDAwM
DAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDP/AABEIAC8AOAMBIgAC
EQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAA
AX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4
OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaan
qKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQAD
AQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEG
EkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpT
VFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4
ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APuDx78d
m0b4geJrubxv4b8A6T4buz4SeTxR5cmn3+pS2VlqVvPFmWIqVhnuI2TzR5uAcgxiuR8Q/tD+MtR8
Kw6l4P8AjB8EfGaw+IdB0rUI9G8OTXHkRahq1vafMyatIFykkpAKndsOOxDNX0bxPqHx11y/8KaL
Y67eaL8XY7u4jvb6SxtYYW8CQwGSaZIpmjUPMijEbnc6A7c7hW+L2heN5/FviDxF4v8AD+j6Hb6j
qnw20+zk0vWX1S3neDxa7yhpHgt2RkFzEcGPaQ6lWJ3BQDrP2tv2z7H4DbdNsfE/wqsdYa/0zT5o
9d8RBbvTVvLu3gNw9iNjvHGk3nEedHlI2OR96uL079vWxs5PiLPD8WPg3rl94f1+zg0+xv8AXLTT
rTUrIaPpstwbaZZXZC1zJeYeXzwpj8okBdy9h+2Rc+OdS0W3t4bPwzo/hm38aeE/J1J7uW71C+kb
XtL5NuI40hCSEDLSyFgp+VSwcZvjK2k8XftS6La6d4u1HRdF8U6fZW1xrNswt7jxFPpVxdXKabaz
oFj/AHi3jPKU+9FbyRxg/vmhAPdLb4r+GLrwxoOtL4g0ddJ8Utbx6RdyXiRxam9woaBImJHmPIvK
qMse3pXQV5/8UPFfh2/0LwPqV74RvvG1nquu6e+kyWmjR6iujTSbmh1N9x/0eKIcmdRlN445r0Aj
H/1xQAUUUUAecfEP4m+Ef2Z9Tub+70fxjLeeNLtr66l8PeENY8QtPPDb21sXn/s+2uBBmGKFFD7d
4jJXcVc15n8Q/wBov4N/FfWtB1HxB4H+MGpX3hfUIdV0u4f4PeMFktZ4juibK6aNyo/zhGygZUbG
5EI9S+N/7SOh/Ar7Yuo2mqXs1n4b1bxTLHZxI/l2enLE0u7cy4Z2mVEXgEhuynG/B8SLWf4kJ4WF
nfLqP9k/2vMxEZhtY2m8pEkcPxI5Eu0KCpETnd0FAHiPjf8Aaq/Zx8ba5oupfETUNL8H3/h+6W80
Wb4k6Fe+D5JJU3DNmdWhtvtIi37mWLzBG0kTOFZo82viF+25+yv8WPCU2heJvjP8CNa0m4KmS1uv
GmlyLvRgyup87KujKrK64ZWUFSCAR7N4x+Ilt4Q1vQtO+yXWoXmu6hHYRwWpj3WwaKeUzSB3XbEq
W0pz1OzaFY4U1W+MGlt8R7fw7ClzdNJobeIJ9RiMbWNnbF1jhMkm/hpsSsm0OrLbTEspUZAPKfhh
+3H+zt4Ri8C/DvwP8UPCHiW4vZ7fw54f0bw3rR8T3x2wsVEi2zTzpDHFExkuJiIo1QeZIFwa+gMY
7596peH9Mn0fT5IbjUrzVpJLme4E90sKyIkkzyJCBEiLsiVliQlS5SNS7SOWdrtABRRRQB8L/tm+
GNa8b/Gf4p+HLmw8Ua9r3j7wtp/h3wppmja6dKWwea28UuGuGS4gSeF/sPmSJKxXa6rscoobPi+H
nhz4i+JIdPtx8SPC998Rtei0O00288caoLyWz0rV70a5BcPDfSpMDHHdMW8xuL8BW3HJ+kPiX+yX
F8XPj7J4r1TUL+30yztNK+ww6Xqdxpl5JdWkeuxOJJ4CskcLR6uhBicMxjZWGzIfBj/YbutA8MWN
9oHi2+0Xxh4b1C61Hw7e3Lz6naaT9suZbi7gmSSUS3iXBnkWV5JBI2yF1ZHjUgAw/ih4F8O61+2Z
4kTV/g03xXWz8C+HY4JZLTSLxtOX7frnDPqNxE2ZMZJTdkoSxB5PjNp8M/AOjfsC2P8AwlvgXRda
1/XPgv8A2loWt3mkQ3cFqlloif6DE7KWtWjDCcDJWVpLiRGBzGv1drn7PPiLX/jZqni63+Imu+Gf
t3h3S9Fmi0OxsMXE9rPfzPKwvLe5KqftoCKjDBD7i2Q1Z3jL9nHxDF+xnpvwj8P6jo91b/8ACMQe
DdS1LUYpIG+w/ZltZ7iNEL5lMJkdYm+UuVBcAZIB634V0GHwv4X0/S7WGO3tdNtorWKFFxHGiKER
QMY2gYA4GMgAADB0K83/AGrPgJD+0r8IpvCUkjWpvLuCeG9ivri1n0ySGRXS6haEqWmiZd6K5CM4
UNlMivSOe5yfWgAooooA/9k='''

if __name__ == "__main__":
    api = BDRAClient()
    print api.get("iplookupservice/iplookup/", ip="117.89.35.58")
    print api.get("currencyservice/currency", fromCurrency="CNY", toCurrency="USD", amount="0.1")
    print api.get("/mobilephoneservice/mobilephone", tel="13800138000")
    print api.post("idlocr/ocr",
                   languagetype="CHN_ENG",
                   imagetype="1",
                   image=_ocr_image,
                   fromdevice="pc",
                   clientip="127.0.0.1",
                   detecttype="LocateRecognize")
    print api.get("aqiservice/aqi", city="成都")
    print api.get("apistore/pullword/words", source="清华大学是好学校", param1=0, param2=1).decode('u8')
    #print api.get("http://apis.baidu.com/yi18/hospital/search", page=1, limit=20, keyword="成都")
    print api.get("http://appyun.sinaapp.com/index.php", app='mobile', controller='index', action='api', outfmt='json', mobile='13800138000')

    os.system("pause")
