import os
import json

# Path to the notebooks folder
notebooks_folder = 'notebooks/src'

# Iterate through all files in the notebooks folder
for filename in os.listdir(notebooks_folder):
    if filename.endswith('.ipynb'):
        filepath = os.path.join(notebooks_folder, filename)
        
        # Open and read the notebook file
        with open(filepath, 'r', encoding='utf-8') as file:
            notebook = json.load(file)
            
            # Iterate through the cells in the notebook
            for cell in notebook.get('cells', []):
                # Process each cell
                cell_metadata = cell.get('metadata', {})
                lang = cell_metadata.get('lang')
                tags = cell_metadata.get('tags', [])
                if lang:
                    tags.append(lang)
                    cell_metadata['tags'] = tags
                    del cell_metadata['lang']
            # Save the modified notebook back to the file
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(notebook, file, indent=2)