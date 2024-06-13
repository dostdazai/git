def greet_all (name1, name2, *names):
    print(f"здравствуйте, {name1}!")
    print(f"здравствуйте, {name2}!")
    for name in names:
        print(f"привет, {name}!")
        
if __name__ == "__main__":
    greet_all("вася", "петя", "коля", "оля")
    