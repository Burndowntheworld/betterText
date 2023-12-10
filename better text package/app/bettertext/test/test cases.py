import bettertext
betterText = bettertext.betterText
print(betterText.foreground.red("hello"))
print(betterText.background.green("hello"))
betterText.typewrite("hello world!")
print(betterText.reverse("hello"))
print(betterText.flip("hello world!"))
print(betterText.vertical("hello"))
print(betterText.number("This is a test for the better text number function in python"))
print(betterText.toadify("this is some random text for toadify"))
print(betterText.repeat("toad",139," "))
print(betterText.hashtag("hello everyone"))
print(betterText.abbreviate("hello world","-",False))
betterText.blink("hello world",0.5,10)