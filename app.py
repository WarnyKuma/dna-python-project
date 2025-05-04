from flask import Flask, render_template, request, flash
from src.dna_utils import *

app = Flask(__name__)
app.secret_key = 'wefhnoijwempfonouvbnweodicfmewkdnxcwescjfkieorfgnbruoefer'


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        action = request.form['action']
        sequence = request.form['sequence']

        if action == 'translate':
            if not sequence.strip():
                flash("Please enter DNA sequence for translation.")
            else:
                protein = translate_dna_to_protein(sequence)
                result = f"Translated Protein Sequence:\n{protein}"
        elif action == 'crop':
            if not sequence.strip():
                flash("Please enter DNA sequence for cropping.")
            else:
                try:
                    start = int(request.form.get('start', 0))
                    end = int(request.form.get('end', len(sequence)))
                    cropped = crop_sequence(sequence, start, end)
                    result = f"Cropped Sequence (from {start} to {end}):\n{cropped}"
                except (ValueError, TypeError) as e:
                    flash("Error: Invalid start or end index.")
        elif action == 'pattern':
            pattern = request.form.get('pattern', '').strip()
            if not sequence.strip():
                flash("Please enter DNA sequence to search for a pattern.")
            elif not pattern:
                flash("Please enter a pattern to search for.")
            else:
                indices = find_pattern(sequence, pattern)
                if indices:
                    result = f"Pattern '{pattern}' found at indices: {indices}"
                else:
                    result = f"No occurrences of pattern '{pattern}' found."
        elif action == 'mutations':
            sample_sequence = request.form.get('sample_sequence', '').strip()
            if not sequence.strip() or not sample_sequence:
                flash("Please enter both reference and sample DNA sequences for mutation detection.")
            else:
                mutations = detect_mutations(sequence, sample_sequence)
                if mutations:
                    result = "Mutations Detected:\n" + "\n".join(mutations)
                else:
                    result = "No mutations found. Sequences are identical."
        elif action == 'reverse':
            if not sequence.strip():
                flash("Please enter DNA sequence to reverse.")
            else:
                reversed_seq = reverse_sequence(sequence)
                result = f"Reversed Sequence:\n{reversed_seq}"
        elif action == 'reverse_complement':
            if not sequence.strip():
                flash("Please enter DNA sequence to get reverse complement.")
            else:
                rev_comp = reverse_complement(sequence)
                result = f"Reverse Complement:\n{rev_comp}"

    return render_template('index.html', result=result)
