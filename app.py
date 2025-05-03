from flask import Flask, render_template, request
from src.dna_utils import crop_sequence, find_pattern, translate_dna_to_protein, detect_mutations

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        action = request.form['action']
        sequence = request.form['sequence']

        if action == 'translate':
            protein = translate_dna_to_protein(sequence)
            result = f"Translated Protein Sequence:\n{protein}"
        elif action == 'crop':
            start = int(request.form.get('start', 0))
            end = int(request.form.get('end', len(sequence)))
            cropped = crop_sequence(sequence, start, end)
            result = f"Cropped Sequence (from {start} to {end}):\n{cropped}"
        elif action == 'pattern':
            pattern = request.form['pattern']
            indices = find_pattern(sequence, pattern)
            if indices:
                result = f"Pattern '{pattern}' found at indices: {indices}"
            else:
                result = f"No occurrences of pattern '{pattern}' found."
        elif action == 'mutations':
            sample_sequence = request.form['sample_sequence']
            mutations = detect_mutations(sequence, sample_sequence)
            if mutations:
                result = "Mutations Detected:\n" + "\n".join(mutations)
            else:
                result = "No mutations found. Sequences are identical."

    return render_template('index.html', result=result)
