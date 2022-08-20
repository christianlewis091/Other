"""
This library is where I want to store all the ingredients and quantities of food for my
grocery list maker GUI project
"""
import pandas as pd
master_list = []

# Chicken Katsu: https://www.justonecookbook.com/tonkatsu-sauce-recipe/#wprm-recipe-container-60845
chicken_katsu = pd.DataFrame({"chicken_breast": 270, "egg": 50, "canola_oil": -999, "ap_flour": '3 Tbsp', "panko": 60, "ketchup": '1 Tbsp', "worcestershire_sauce":'1 Tbsp', "oyster_sauce": '1 Tbsp'}, index = [0])
master_list.append(chicken_katsu)

# Corn Ramen in Breville Fast Slow Cook: https://breville-production-aem-assets.s3-us-west-2.amazonaws.com/BPR680ANZ/BPR680_ANZ_Recipes_ebook.pdf
corn_ramen = pd.DataFrame({"dried_shiitake":35, "boiling_water": 1000, "corn": 250, "green_onion": '4 ea', "sesame_oil": '2 Tbsp', "garlic": '4 cloves', "ginger": '1 Tbsp', "swiss_mushroom": 200, "miso_paste": 80, "soy_sauce": 60, "mirin": 60, "soy_milk": 500, "soba_noodle": 270}, index = [0])
master_list.append(corn_ramen)



