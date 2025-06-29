
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("hello world")


hello() # call greet function
# if not define @greet and when decoraor add so calling this type
# greet(hello)()


def add(a,b):
    print(a + b)

