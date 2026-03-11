def generate_patient_summary(name, age, symptoms):

    summary = f"""
Patient Summary Report

Patient Name: {name}
Age: {age}

Reported Symptoms:
{symptoms}

Possible Medical Observation:
Symptoms may indicate a common illness or infection. Proper clinical examination is recommended.

Advice:
Patient should consult a healthcare professional for accurate diagnosis and treatment.
"""

    return summary