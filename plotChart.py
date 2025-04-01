#!/usr/bin/env python
# coding: utf-8

import os  # Import os for file path handling
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import pandas as pd
import numpy as np
from PIL import Image  # Use Pillow for image handling

file_name = 'example_month_2'  # Example date, replace with the dates you want to process
file_path = os.path.join('/Users/gerb5/vscode-projects/nfp-creighton-model-chart/data', f'{file_name}.xlsx')

# Load the Excel file into a DataFrame
try:
    df = pd.read_excel(file_path)
    df = df.fillna('')  # Fill NaN values with empty strings
    required_columns = ['Date', 'Intercourse', 'Discharge', 'Sticker']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Missing required columns: {', '.join(required_columns)}")
    print(f'Cycle Length: {df.shape[0]} days')  # Using f-strings for cleaner output
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

def plot_chart(df, file_name):
    print(f"Attempting to open {file_path}")
    # Function to plot sticker images
    def plot_image(x, y, path, zoom):
        try:
            img = Image.open(path)  # Use Pillow to read the image
            imagebox = OffsetImage(img, zoom=0.05) # 0.05 - reduce the size of the image to fit the cell
            xy = [x, y]
            ab = AnnotationBbox(imagebox, xy, xybox=(0, 0), xycoords='data', boxcoords="offset points", frameon=False)
            ax.add_artist(ab)
        except FileNotFoundError:
            print(f"Warning: Sticker image not found at {path}")

    # Configure axes
    fig = plt.gcf()
    fig.clf()
    plt.figure(figsize=(7 * 5 / 2, 1.85), dpi=150)
    ax = plt.subplot(111)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.axis('off')

    # Plot grid
    plt.text(6.5, 0.15, 'BSE', ha='center', size=7, weight='bold')
    linewidth1 = 0.5
    linewidth2 = 0.5
    yrange = [0, 2, 3.75, 4.7]
    for x in range(0, 7 * 6 + 1):
        for y in yrange:
            if x % 7 == 0:
                plt.plot([x, x], [0, y], '-k', linewidth=linewidth2)
            else:
                plt.plot([x, x], [0, y], '-k', linewidth=linewidth1)

            if y == yrange[1]:
                plt.plot([0, x], [y, y], '-k', linewidth=linewidth1)
            else:
                plt.plot([0, x], [y, y], '-k', linewidth=linewidth2)
        if x < 42:
            plt.text(x + 0.5, 4.1, x + 1, ha='center', size=9)

    # Plot day number, date, and observation text
    for row in range(0, df.shape[0]):
        date = df.loc[row, 'Date']
        intercourse = df.loc[row, 'Intercourse']
        discharge = df.loc[row, 'Discharge'].rstrip()
        plt.text(row + 0.5, 1.5, f"{date.month}/{date.day}", ha='center', fontname='Verdana', size=6)
        if 'I' in intercourse:
            if row == 6:
                plt.text(row + 0.5, 0.5, intercourse, ha='center', fontname='Verdana', size=7)
            else:
                plt.text(row + 0.5, 0.1, intercourse, ha='center', fontname='Verdana', size=7)
        if len(discharge) < 5:
            plt.text(row + 0.5, 1, discharge, ha='center', fontname='Verdana', size=7)
        else:
            space = discharge.find(' ')
            plt.text(row + 0.5, 1, discharge[0:space], ha='center', fontname='Verdana', size=7)
            row2 = discharge[space + 1:]
            if len(row2) < 6:
                plt.text(row + 0.5, 0.55, row2, ha='center', fontname='Verdana', size=7)
            else:
                space = row2.find(' ')
                plt.text(row + 0.5, 0.55, row2[0:space], ha='center', fontname='Verdana', size=7)
                plt.text(row + 0.5, 0.35, row2[space:], ha='center', fontname='Verdana', size=7)

        # Call plot_image function
        df['Sticker'] = df['Sticker'].fillna('blank')  # Replace NaN with 'blank'
        sticker = str(df.loc[row, 'Sticker']).lower()
        sticker_path = f"Stickers/{sticker}.png" if len(sticker) > 0 else "Stickers/blank.png"
        # uncomment the next line to validate the sticker image path
        #print(f"Sticker path for row {row}: {sticker_path}")
        plot_image(row + 0.5, 2.85, sticker_path, 0.125)

    # Save & show plot
    output_path = os.path.join('/Users/gerb5/vscode-projects/nfp-creighton-model-chart/charts', f'{file_name}.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print('Chart saved successfully.')

# -------------------------------------------------------
plot_chart(df, file_name)
print('Done.')