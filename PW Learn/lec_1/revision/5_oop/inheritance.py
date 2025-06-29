class parent:
    def method(self):
        print("parent method")
class child(parent):           #inherit
    pass

if __name__ == "__main__":
    child_obj = child()
    child_obj.method()
