# Doctor  is prompting the patient to eat the thergran tablet to keep the pateint full of nutrients from some artifical resource. 
# The patient insists on eating fruits to boost immunity but the doctor loses it perheps he wanted to create some sales for the pharmacy at his clinic which is empty as always.

# WE are using dics to solve this problem

# Dialogue 1
# Doctor: You must take this Theragran tablet—perfect nutrients, no effort.
# Patient: Or I could just eat an orange… you know, natural vitamins?
# Doctor: Natural? This is scientifically manufactured perfection!

# Dialogue 2
# Patient: I’ll just have fruits—apples, bananas, maybe some dates.
# Doctor: Fruits? FRUITS?! Do you want uncalculated vitamins in your body?!
# Patient: Pretty sure humans survived on those for centuries…

# Dialogue 3
# Doctor: Look, just buy the tablet from my clinic pharmacy.
# Patient: The one with zero customers?
# Doctor: That’s because people keep choosing fruits like you!

# Dialogue 1
# Doctor: This tablet gives you Vitamin A – 1200 mcg and Beta Carotene – 600 mcg!
# Patient: Or I could just eat carrots…
# Doctor: Carrots don’t come with a receipt from my pharmacy!

# Dialogue 2
# Doctor: You’re low on immunity—this has Vitamin C – 90 mg and Vitamin D – 10 mcg.
# Patient: Or I could get sunlight and oranges?
# Doctor: Sunlight doesn’t help my sales!

# Dialogue 3
# Doctor: Look! Iron – 27 mg, Calcium – 40 mg, Magnesium – 100 mg—all in one tablet!
# Patient: Sounds like food… but compressed.
# Doctor: Exactly! Efficient… and profitable.

# Dialogue 4
# Doctor: It even includes Vitamin B1 and B6 – 3 mg, and B12 – 9 mcg!
# Patient: I can get those from a balanced diet.
# Doctor: Balanced diet doesn’t pay my clinic rent!

# Dialogue 5
# Doctor: You also get Zinc – 15 mg, Copper – 2 mg, and Selenium – 10 mcg!
# Patient: That sounds like a chemistry lab.
# Doctor: Yes—and you’re the experiment!


def main():
    nutrients = {
        "Vitamin A": 4000,
        "Beta Carotene": 1000,
        "Vitamin D": 400,
        "Vitamin E": 30,
        "Vitamin C": 90,
        "Vitamin B1": 3,
        "Vitamin B2": 9,
        "Vitamin B6": 10,
        "Vitamin B12": 3.4,
        "Magnesium": 150,
    }
    nutrients.update({
        "Zinc": 90,
        "Sulfer": 31,
        "Chloride": 92
    })
    nutrients["Selenium"] = 72
    print("Doctor: You must take this Theragran tablet—perfect nutrients, no effort.\nPatient: Or I could just eat an orange… you know, natural vitamins?\nDoctor: Natural? This is scientifically manufactured perfection!\n\nPatient: I’ll just have fruits—apples, bananas, maybe some dates.\nDoctor: Fruits? FRUITS?! Do you want uncalculated vitamins in your body?!\nPatient: Pretty sure humans survived on those for centuries…\n\nDoctor: Look, just buy the tablet from my clinic pharmacy.Patient: The one with zero customers?Doctor: That’s because people keep choosing fruits like you!"
    )
    benefits(nutrients)
    print(benefits(nutrients))



def benefits(report):
    return f"""
                              
                              ##Doctor acting as a Chemist##

        Doctor: This tablet gives you {report["Vitamin A"]}IU of Vitamin A  and {report["Beta Carotene"]}IU of Beta Carotene!
        Patient: Or I could just eat carrots…
        Doctor: Carrots don’t come with a receipt from my pharmacy!


        Doctor: You also get {report.get("Chloride", "I don't know how much BUT")}g of Chloride, as well as {report.get("Copper", "I don't know how much BUT")} Copper!         
        Patient: That sounds like a chemistry lab.
        Doctor: Yes—and you’re the experiment!

        Doctor: PLEASE BUY IT MATE, YOU WILL {report.get("Selenium", "some amount")} OF SELENIUM AS WELL.
        YOU WILL SAVE A LOT MORE MONEY BY BUYING A TABLET RATHER THAN EATING FRUITS.
        Patient: At least I ll eat healthy.`
"""



main()
