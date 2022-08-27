#Importing Libraries
from flask import Flask, render_template, request
from FindElem import FindElem
from MolarMass import MolarMass
import re
from sympy import Matrix, lcm

#Flask Initialization
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

#Homepage
@app.route('/index')
def homepage():
    return render_template("index.html")

#Homepage 2
@app.route('/')
def homepage2():
    return render_template("index.html")

#Combustion
@app.route('/combustion', methods = ["POST", "GET"])
def combustion():

    if request.method == "POST":
        ch = 1 #Number of CH Atoms (Reac)
        o2 = 1 #Number of O2 Atoms (Reac)
        co2 = 1 #Number of CO2 Atoms (Prod.)
        h2o = 1 #Number of H2O Atoms (Prod.)

        reac_carbon = request.form.get('reac_carbon', type=int) #Number of Carbon Atoms in CH compound (Reactants)
        reac_hydrogen = request.form.get('reac_hydrogen', type=int)#Number of Hydrogen Atoms in CH compound (Reactants)

        prod_oxygen = 3 #Number of Oxygen Atoms in H2O compound (Products)

        #equation
        co2 = reac_carbon

        if int(reac_hydrogen) % 2 == 0:
            h2o = (reac_hydrogen / 2)
        else:
            ch = 2
            co2 *= 2
            h2o = int(reac_hydrogen)
        prod_oxygen += ((co2 - 1) * 2) + h2o - 1

        if prod_oxygen % 2 == 0:
            o2 = prod_oxygen / 2
        else:
            ch *= 2
            o2 = int(prod_oxygen)
            co2 *= 2
            h2o *= 2

        h2of = int(h2o)
        o2f = int(o2)

        return render_template("combustion.html", ch = ch, co2 = co2, o2 = o2, h2o = h2o, reac_carbon = reac_carbon, reac_hydrogen = reac_hydrogen, h2of = h2of, o2f = o2f)
    else:
        return render_template("combustion.html")

#Molar Mass
@app.route('/molarmass', methods = ["POST", "GET"])
def molarmass():
    if request.method == "POST":
        compound = request.form.get("compound")
        total = 0

        ele = []
        nums = []

        i = 0
        while i < len(compound):
        	if ((compound[i] >= 'A' and compound[i] <= 'Z') and (compound[i + 1] >= 'a' and compound[i + 1] <= 'z')):
        		ele.append(compound[i:i+2])
        		i += 1
        	elif (compound[i] >= 'A' and compound[i] <= 'Z'):
        		ele.append(compound[i:i+1])
        	elif (compound[i] >= '1' and compound[i] <= '9'):
        		nums.append(int(re.search(r'\d+', compound[i]).group()))
        	i += 1

        j = 0
        while j < len(nums):
        	total += FindElem.findMass(ele[j]) * nums[j]
        	j += 1

        formatted_mm = format(total, ".2f")

        return render_template("molarmass.html", formatted_mm = formatted_mm, compound = compound)
    else:
        return render_template("molarmass.html")

#Percent Composition
@app.route('/percentcomp', methods = ["POST", "GET"])
def percentcomp():
    if request.method == "POST":
        compound = request.form.get("compound")
        element = request.form.get("element")

        index = compound.index(element)

        massOfCompound = MolarMass.calcMass(compound)

        total = 0.0

        elementLength = len(element)
        if elementLength == 2:
        	massOfElement = FindElem.findMass(element) * int(re.search(r'\d+', compound[index + 2]).group())
        else:
        	massOfElement = FindElem.findMass(element) * int(re.search(r'\d+', compound[index + 1]).group())

        mm = ((massOfElement/massOfCompound) * 100)
        f_mm = format(mm, '.2f')
        return render_template("percentcomp.html", f_mm = f_mm, element = element, compound = compound)
    else:
        return render_template("percentcomp.html")

#Stoichiometry
@app.route('/stoich', methods = ["POST", "GET"])
def stoichiometry():
    if request.method == "POST":
        compound1 = request.form.get("compound1")
        massOfCompound1 = float(MolarMass.calcMass(compound1))

        compound2 = request.form.get("compound2")
        massOfCompound2 = float(MolarMass.calcMass(compound2))

        amtOriginalEle = request.form.get("amtOriginalEle")

        coefficient1 = request.form.get("coefficient1")
        coefficient2 = request.form.get("coefficient2")

        molesOfC1 = float(amtOriginalEle) / massOfCompound1
        molesOfC2 = molesOfC1 * int(coefficient2) / int(coefficient1)
        amtOfC2 = ((float(amtOriginalEle) * int(coefficient2) * massOfCompound2) / (massOfCompound1 * int(coefficient1)))

        f_molesOfC1 = format(molesOfC1, '.2f')
        f_molesOfC2 = format(molesOfC2, '.2f')
        f_amtOfC2 = format(amtOfC2, '.2f')

        if f_molesOfC1 < f_molesOfC2:
            lr = compound1
            er = compound2
        else:
            lr = compound2
            er = compound1

        return render_template("stoich.html", er = er, lr = lr, compound1 = compound1, compound2 = compound2, amtOfC2 = amtOfC2, amtOriginalEle = amtOriginalEle, molesOfC1 = molesOfC1, molesOfC2 = molesOfC2, f_molesOfC1 = f_molesOfC1, f_amtOfC2 = f_amtOfC2, f_molesOfC2 = f_molesOfC2)

    else:
        return render_template("stoich.html")

#Balancing Equations
@app.route("/balance", methods = ["POST", "GET"])
def balance():
    if request.method == "POST":
        elementList = []
        elementMatrix = []

        reactants= request.form.get("reac")

        products=request.form.get("prod")
        reactants=reactants.replace(' ', '').split("+")
        products=products.replace(' ', '').split("+")

        def addToMatrix(element, index, count, side):
            if(index == len(elementMatrix)):
               elementMatrix.append([])
               for x in elementList:
                    elementMatrix[index].append(0)

            if(element not in elementList):
                elementList.append(element)

                for i in range(len(elementMatrix)):
                    elementMatrix[i].append(0)

            column = elementList.index(element)
            elementMatrix[index][column] += count*side

        def findElements(segment,index, multiplier, side):
            elementsAndNumbers = re.split('([A-Z][a-z]?)',segment)
            i = 0
            while(i<len(elementsAndNumbers)-1):
                  i += 1
                  if(len(elementsAndNumbers[i])>0):
                    if(elementsAndNumbers[i+1].isdigit()):
                        count = int(elementsAndNumbers[i+1]) * multiplier
                        addToMatrix(elementsAndNumbers[i], index, count, side)
                        i += 1
                    else:
                        addToMatrix(elementsAndNumbers[i], index, multiplier, side)

        def compoundDecipher(compound, index, side):
            segments = re.split('(\([A-Za-z0-9]*\)[0-9]*)',compound)
            for segment in segments:
                if segment.startswith("("):
                    segment = re.split('\)([0-9]*)',segment)
                    multiplier = int(segment[1])
                    segment = segment[0][1:]
                else:
                    multiplier = 1
                findElements(segment, index, multiplier, side)

        for i in range(len(reactants)):
            compoundDecipher(reactants[i],i,1)

        for i in range(len(products)):
            compoundDecipher(products[i],i + len(reactants),-1)

        elementMatrix = Matrix(elementMatrix)
        elementMatrix = elementMatrix.transpose()
        solution = elementMatrix.nullspace()[0]
        multiple = lcm([val.q for val in solution])
        solution = multiple * solution
        coEffi = solution.tolist()
        output = ""

        for i in range(len(reactants)):
            output+=str(coEffi[i][0])+reactants[i]
            if i < len(reactants) - 1:
               output += " + "
        output += " -> "

        for i in range(len(products)):
           output += str(coEffi[i+len(reactants)][0]) + products[i]
           if i < len(products)-1:
               output += " + "

        answer = output

        return render_template("balance.html", answer = answer, elementList = elementList)
    else:
        return render_template("balance.html")


#Flask Initiator
if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)