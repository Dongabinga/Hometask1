yzhebilo = []
def modern_print(string):
    if string not in yzhebilo:
        print(string)
        yzhebilo.append(string)
modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")