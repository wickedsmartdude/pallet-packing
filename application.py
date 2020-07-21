from flask import Flask,flash, redirect, url_for,request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# recursive function to return permutations of a list
def permutation(lst):

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]

       for p in permutation(remLst): # Generating all permutations where m is first element
            l.append([m] + p)

    return l

@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    # for standard EUR type pallet
    LENGTH = 800
    BREADTH = 1200
    HEIGHT = 1500

    # Getting the dimensions
    length = request.form.get("length")
    breadth = request.form.get("breadth")
    height = request.form.get("height")

    # for cuboid portion
    data = [length, breadth, height]
    permutations = [] # All possible alignments
    no_of_boxes = [] # Number of boxes that can be fit for each alignment



    for p in permutation(data):
        permutations.append(p)

    print("Permutations:= ")
    print(permutations)

    for p in permutations:
        l = int(LENGTH/int(p[0]))
        b = int(BREADTH/int(p[1]))
        h = int(HEIGHT/int(p[2]))
        no_of_boxes.append(l*b*h)

    print("Number of the Boxes := ")
    print(no_of_boxes)

    # finding which alignment will have maximu number of boxes in the cuboid portion
    alignment = permutations[no_of_boxes.index(max(no_of_boxes))]

    return render_template("calculate.html",alignment=alignment, stackings = max(no_of_boxes))





