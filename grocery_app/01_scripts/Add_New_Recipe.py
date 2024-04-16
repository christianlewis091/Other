"""
HOW TO ADD RECIPES TO THE RECIPEBOOK! 
"""
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas as pd
from datetime import date

today = date.today()
supermarket_Dir = ('C:/Users/clewis/IdeaProjects/Other/grocery_app/01_scripts/supermarket_listV5.xlsx')
recipebook_Dir = ('RECIPES_DontChangeManually.xlsx')
output_Dir = (f'Output_{today}.xlsx')
image = ('C:/Users/clewis/IdeaProjects/Other/grocery_app/01_scripts/xyz.jpg')


class RecipeBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Book")

        # Load supermarket list and recipe book
        self.supermarket_df = pd.read_excel(f'{supermarket_Dir}')
        self.recipe_book_df = pd.read_excel(f'{recipebook_Dir}')

        # Recipe Title Entry
        self.recipe_title_label = ttk.Label(self.root, text="Recipe Title:")
        self.recipe_title_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.recipe_title_entry = ttk.Entry(self.root)
        self.recipe_title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        # Meal Type Dropdown
        self.meal_label = ttk.Label(self.root, text="Meal:")
        self.meal_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.meal_var = tk.StringVar()
        self.meal_dropdown = ttk.Combobox(self.root, textvariable=self.meal_var, values=["Breakfast", "Lunch", "Dinner", "Dessert", "Dog", "Baby/Kid"])
        self.meal_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="we")
        self.meal_dropdown.current(0)

        # Recipe Source Entry
        self.recipe_source_label = ttk.Label(self.root, text="Recipe Source:")
        self.recipe_source_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.recipe_source_entry = ttk.Entry(self.root)
        self.recipe_source_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        # Ingredients Listbox
        self.ingredients_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        self.ingredients_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        self.populate_ingredients_listbox()

        # Add to Recipe Book Button
        self.add_button = ttk.Button(self.root, text="Add to Recipe Book", command=self.add_to_recipe_book)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Info Text Label
        self.info_label = ttk.Label(self.root, text="If you can't find the ingredient you need, you have to add it to the Supermarket List.\nThis avoids annoying duplications that arise in final lists, such as (Onion, onions, yellow onion)")
        self.info_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        # Load and Resize Image
        self.image_path = f'{image}'
        self.load_and_resize_image()

    def populate_ingredients_listbox(self):
        # Clear previous items
        self.ingredients_listbox.delete(0, tk.END)

        # Get unique ingredients from the supermarket list
        ingredients = self.supermarket_df["Ingredient"].unique()

        # Populate listbox with ingredients
        for ingredient in ingredients:
            self.ingredients_listbox.insert(tk.END, ingredient)

    def add_to_recipe_book(self):
        # Get recipe title, source, and meal type
        recipe_title = self.recipe_title_entry.get()
        recipe_source = self.recipe_source_entry.get()
        meal_type = self.meal_var.get()

        # Get selected ingredients from listbox
        selected_indices = self.ingredients_listbox.curselection()
        selected_ingredients = [self.ingredients_listbox.get(idx) for idx in selected_indices]

        # Add selected ingredients to recipe book
        for ingredient in selected_ingredients:
            self.recipe_book_df = self.recipe_book_df.append({"Recipe_Title": recipe_title, "Meal": meal_type, "Ingredient": ingredient, "Source": recipe_source}, ignore_index=True)

        # Save updated recipe book
        self.recipe_book_df.to_excel(f'{output_Dir}', index=False)

        # Clear entry fields and selection in listbox
        self.recipe_title_entry.delete(0, tk.END)
        self.recipe_source_entry.delete(0, tk.END)
        self.ingredients_listbox.selection_clear(0, tk.END)

        # Show confirmation message
        messagebox.showinfo("Success", "Ingredients added to Recipe Book! Saved to {}".format(f'{output_Dir}'))

    def load_and_resize_image(self):
        # Load image
        original_image = Image.open(self.image_path)

        # Define the desired width and height
        desired_width = 200
        desired_height = 100

        # Resize image
        resized_image = original_image.resize((desired_width, desired_height), Image.ANTIALIAS)

        # Convert Image object to Tkinter PhotoImage object
        self.image = ImageTk.PhotoImage(resized_image)

        # Create label to display the resized image
        self.image_label = ttk.Label(self.root, image=self.image)
        self.image_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeBookApp(root)
    root.mainloop()













