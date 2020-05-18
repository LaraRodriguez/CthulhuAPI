import json
import os
from pathlib import Path

try:
    base_path = Path(__file__).parent
    file_path = (base_path / "guardianmanual.json").resolve()
    with open(file_path, 'r', encoding='utf-8') as file:
        # json.load. devuelve un objeto de tipo diccionario sobre el que se puede iterar.
        datos = json.load(file)

    while True:
        os.system("cls")
        print("Achtung Cthulhu Guardian Manual, Lara Rodriguez")
        print("*---------------------------------------------*")
        print("Welcome Guardian, start your new journey")
        print("*--------------------------------------*")
        print("\t 1. Personal sheet")
        print("\t 2. Weapons")
        print("\t 3. Equipement")
        print("\t 4. Myths")
        print("\t 5. Spells")
        print("\t 6. Mental illnesses")
        print("\t 7. Locations")
        print("\t 8. Exit")
        opcion = int(input())

        if opcion == 1:
            while True:
                os.system("cls")
                print("*------------*")
                print("Personal sheet")
                print("*------------*")
                print("\t 1. Personal characteristics")
                print("\t 2. Skills")
                print("\t 3. Nacionality")
                print("\t 4. Jobs")
                print("\t 5. Languages")
                print("\t 6. Go back")
                opcion = int(input())

                if opcion == 1:
                    print("*------------*")
                    print("\t 1. Complete list")
                    print("\t 2. Search by name")
                    opcion = int(input())

                    if opcion == 1:
                        for caracteristica in datos['personal_characteristics']:
                            print(caracteristica['name'])
                        input("Click to continue")
                    elif opcion == 2:
                        print("Insert the name of the characteristic")
                        name = input()
                        print(name)
                        for caracteristica in datos['personal_characteristics']:
                            if caracteristica['name'] == name:
                                print("Name::", caracteristica['name'])
                                print("Description:",
                                      caracteristica['description'])

                        input("Click to continue")
                elif opcion == 2:
                    print("*------------*")
                    print("\t 1. Complete list")
                    print("\t 2. Search by name")
                    opcion = int(input())

                    if opcion == 1:
                        for caracteristica in datos['skills']:
                            print(caracteristica['name'])
                        input("Click to continue")
                    elif opcion == 2:
                        print("Input the name to search")
                        skill = input()
                        for caracteristica in datos['skills']:
                            if caracteristica['name'] == skill:
                                print("Name:", caracteristica['name'])
                                print("Description:",
                                      caracteristica['description'])
                        input("Click to continue")
                elif opcion == 3:
                    print("*------------*")
                    print("\t 1. Complete list")
                    print("\t 2. Search by name")
                    opcion = int(input())

                    if opcion == 1:
                        for caracteristica in datos['nacionality']:
                            print(caracteristica['name'])
                        input("Click to continue")
                    elif opcion == 2:
                        print("Input the name to search")
                        nac = input()
                        for caracteristica in datos['nacionality']:
                            if caracteristica['name'] == nac:
                                print("Name:", caracteristica['name'])
                                print("Description:",
                                      caracteristica['description'])
                        input("Click to continue")
                elif opcion == 4:
                    print("*------------*")
                    print("\t 1. Complete list")
                    print("\t 2. Search by name")
                    opcion = int(input())

                    if opcion == 1:
                        for caracteristica in datos['jobs']:
                            print(caracteristica['name'])
                        input("Click to continue")
                    elif opcion == 2:
                        print("Input the name to search")
                        job = input()
                        for caracteristica in datos['jobs']:
                            if caracteristica['name'] == job:
                                print("Name:", caracteristica['name'])
                                print("Description:",
                                      caracteristica['description'])
                        input("Click to continue")
                elif opcion == 5:
                    print("*------------*")
                    print("\t 1. Complete list")
                    print("\t 2. Search by name")
                    opcion = int(input())

                    if opcion == 1:
                        for caracteristica in datos['languages']:
                            print(caracteristica['name'])
                        input("Click to continue")
                    elif opcion == 2:
                        print("Input the name to search")
                        lan = input()
                        for caracteristica in datos['languages']:
                            if caracteristica['name'] == lan:
                                print("Name:", caracteristica['name'])
                                print("Description:",
                                      caracteristica['description'])
                        input("Click to continue")
                elif opcion == 6:
                    break
                else:
                    print("Error, try again")
                    input("Click to continue")
        elif opcion == 2:
            print("*------------*")
            print("\t 1. Complete list")
            print("\t 2. Search by name")
            opcion = int(input())

            if opcion == 1:
                for caracteristica in datos['weapons']:
                    print(caracteristica['name'])
                input("Click to continue")
            elif opcion == 2:
                print("Input the name to search")
                wea = input()
                for caracteristica in datos['weapons']:
                    if caracteristica['name'] == wea:
                        print("Name:", caracteristica['name'])
                        print("Description:", caracteristica['description'])
                input("Click to continue")
        elif opcion == 3:
            print("*------------*")
            print("\t 1. Complete list")
            print("\t 2. Search by name")
            opcion = int(input())

            if opcion == 1:
                for caracteristica in datos['equipement']:
                    print(caracteristica['name'])
                input("Click to continue")
            elif opcion == 2:
                print("Input the name to search")
                equ = input()
                for caracteristica in datos['equipement']:
                    if caracteristica['name'] == equ:
                        print("Name:", caracteristica['name'])
                        print("Description:", caracteristica['description'])
                input("Click to continue")
        elif opcion == 4:
            print("*------------*")
            print("\t 1. Complete list")
            print("\t 2. Search by name")
            opcion = int(input())

            if opcion == 1:
                for caracteristica in datos['myths']:
                    print(caracteristica['name'])
                input("Click to continue")
            elif opcion == 2:
                print("Input the name to search")
                myth = input()
                for caracteristica in datos['myths']:
                    if caracteristica['name'] == myth:
                        print("Name:", caracteristica['name'])
                        print("Description:", caracteristica['description'])
                input("Click to continue")
        elif opcion == 5:
            print("*------------*")
            print("\t 1. Complete list")
            print("\t 2. Search by name")
            opcion = int(input())

            if opcion == 1:
                for caracteristica in datos['spells']:
                    print(caracteristica['name'])
                input("Click to continue")
            elif opcion == 2:
                print("Input the name to search")
                spell = input()
                for caracteristica in datos['spells']:
                    if caracteristica['name'] == spell:
                        print("Name:", caracteristica['name'])
                        print("Description:", caracteristica['description'])
                input("Click to continue")
        elif opcion == 6:
            while True:
                os.system("cls")
                print("*--------------*")
                print("Mental illnesses")
                print("*--------------*")
                print("\t 1. Mental illness")
                print("\t 2. Loss of sanity")
                print("\t 3. Go back")
                opcion = int(input())

                if opcion == 1:
                    print("*------------*")
                    print("\t 1. Complete list")
                    print("\t 2. Search by name")
                    opcion = int(input())

                    if opcion == 1:
                        for caracteristica in datos['mental_illness']:
                            print(caracteristica['name'])
                        input("Click to continue")
                    elif opcion == 2:
                        print("Input the name to search")
                        ill = input()
                        for caracteristica in datos['mental_illness']:
                            if caracteristica['name'] == ill:
                                print("Name:", caracteristica['name'])
                                print("Description:",
                                      caracteristica['description'])
                        input("Click to continue")
                elif opcion == 2:
                    print("*------------*")
                    print("\t 1. Complete list")
                    print("\t 2. Search by name")
                    opcion = int(input())

                    if opcion == 1:
                        for caracteristica in datos['loss_of_sanity']:
                            print(caracteristica['name'])
                        input("Click to continue")
                    elif opcion == 2:
                        print("Input the name to search")
                        san = input()
                        for caracteristica in datos['loss_of_sanity']:
                            if caracteristica['name'] == san:
                                print("Name:", caracteristica['name'])
                                print("Description:",
                                      caracteristica['description'])
                        input("Click to continue")
                elif opcion == 3:
                    break
                else:
                    print("Error, try again")
                    input("Click to continue")
        elif opcion == 7:
            print("*------------*")
            print("\t 1. Complete list")
            print("\t 2. Search by name")
            opcion = int(input())

            if opcion == 1:
                for caracteristica in datos['locations']:
                    print(caracteristica['name'])
                input("Click to continue")
            elif opcion == 2:
                print("Input the name to search")
                loc = input()
                for caracteristica in datos['locations']:
                    if caracteristica['name'] == loc:
                        print("Name::", caracteristica['name'])
                        print("Description:", caracteristica['description'])
                input("Click to continue")
        elif opcion == 8:
            break
        else:
            print("Error, try again")
            input("Click to continue")
except:
    print("Error")
