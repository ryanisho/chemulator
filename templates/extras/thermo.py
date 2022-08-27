@app.route("/thermo", methods = ["POST", "GET"])
def thermochemistry():

    if request.method == "POST":
        choose = request.form.get("choose")
        total = 0.0

        reactants = []
        products = []

        if choose.lower() == "enthalpy":
            compound1 = request.form.get("compound1")
            num1 = request.form.get("num1")
            reactant1 = (compound1, num1)
            reactants.append(reactant1)

            compound2 = request.form.get("compound2")
            num2 = request.form.get("num2")
            reactant2 = (compound2, num2)
            reactants.append(reactant2)

            compound3 = request.form.get("compound3")
            num3 = request.form.get("num3")
            product1 = (compound3, num3)
            products.append(product1)

            compound4 = request.form.get("compound4")
            num4 = request.form.get("num4")
            product2 = (compound4, num4)
            products.append(product2)

            k = 0
            while k < len(products):
            	product_i = products[k]
            	total += FindElem.findEnth(product_i[0]) * int(re.search(r'\d+', product_i[1]).group())
            	k += 1

            r = 0
            while r < len(reactants):
            	reactant_i = reactants[r]
            	total -= FindElem.findEnth(reactant_i[0]) * int(re.search(r'\d+', reactant_i[1]).group())
            	r += 1

            f_total = format(total, '.2f')
            print(f_total)

        elif choose.lower() == "entropy":
            compound1 = request.form.get("compound1")
            num1 = request.form.get("num1")
            reactant1 = (compound1, num1)
            reactants.append(reactant1)

            compound2 = request.form.get("compound2")
            num2 = request.form.get("num2")
            reactant2 = (compound2, num2)
            reactants.append(reactant2)

            compound3 = request.form.get("compound3")
            num3 = request.form.get("num3")
            product1 = (compound3, num3)
            products.append(product1)

            compound4 = request.form.get("compound4")
            num4 = request.form.get("num4")
            product2 = (compound4, num4)
            products.append(product2)

            k = 0
            while k < len(products):
            	product_i = products[k]
            	total += FindElem.findEntr(product_i[0]) * int(product_i[1])
            	k += 1

            r = 0
            while r < len(reactants):
            	reactant_i = reactants[r]
            	total -= FindElem.findEntr(reactant_i[0]) * int(reactant_i[1])
            	r += 1

            f_total = format(total, '.2f')
            print(f_total)

        else:
            compound1 = request.form.get("compound1")
            num1 = request.form.get("num1")
            reactant1 = (compound1, num1)
            reactants.append(reactant1)

            compound2 = request.form.get("compound2")
            num2 = request.form.get("num2")
            reactant2 = (compound2, num2)
            reactants.append(reactant2)

            compound3 = request.form.get("compound3")
            num3 = request.form.get("num3")
            product1 = (compound3, num3)
            products.append(product1)

            compound4 = request.form.get("compound4")
            num4 = request.form.get("num4")
            product2 = (compound4, num4)
            products.append(product2)

            k = 0
            while k < len(products):
            	product_i = products[k]
            	total += FindElem.findGibbs(product_i[0]) * int(product_i[1])
            	k += 1

            r = 0
            while r < len(reactants):
            	reactant_i = reactants[r]
            	total -= FindElem.findGibbs(reactant_i[0]) * int(reactant_i[1])
            	r += 1

            f_total = format(total, '.2f')
            print(f_total)

        return render_template("thermo.html")
    else:
        return render_template("thermo.html")
