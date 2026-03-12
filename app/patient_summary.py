def generate_patient_summary(name, age, symptoms):

    summary = {
        "name": name,
        "age": age,
        "symptoms": symptoms,
        "observation": "The symptoms indicate a possible mild illness or infection.",
        "advice": "Patient should consult a healthcare professional for proper diagnosis."
    }

    return summary