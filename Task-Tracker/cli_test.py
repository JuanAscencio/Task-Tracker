# To run in windows you have to put in the power shell: python3 prueba.py -n "Name" -l "English/Spanish" -a Number
# Example: python3 prueba.py -n "Juan" -l "Spanish" -a 99

def hello(name, age, lang):
    text = {
        "English": f"Hello {name}, I know you are {age} y/o and speak {lang}" ,
        "Spanish": f"Hola {name}. Se que tienes {age} años, y hablas {lang} (Español en ingles)"
    }
    msg = text[lang]
    print(msg)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="A test of argparse library"
    )

    parser.add_argument(
        "-n", "--name",
        required=True, help="Some name"
    )

    parser.add_argument(
        "-l", "--lang",
        required=True, choices=["Spanish", "English"],
        help="The language someone speaks"
    )

    parser.add_argument(
        "-a", "--age",
        required=True, help="The age of some person"
    )
    
    args = parser.parse_args()

    hello(args.name, args.age, args.lang)
