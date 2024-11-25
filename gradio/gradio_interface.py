import pickle
import gradio as gr

work_industries = ["Retail", "Energy", "CPG", "Real Estate", "Media/Entertainment", "Financial Services",
                   "Investment Management", "Technology", "Consulting", "Nonprofit/Gov",
                   "PE/VC", "Health Care", "Investment Banking", "Other"]
races = ["Unknown", "Asian", "Black", "Hispanic", "White", "Other"]
major = ["Business", "STEM", "Humanities"]

model_file = 'model.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f:
    model = pickle.load(f)

with open(dv_file, 'rb') as f:
    dv = pickle.load(f)


def process_form_data(gender, international, gpa, major, race, gmat, work_exp, work_industry):
    try:
        client_data = {
            "gender": gender,
            "international": international,
            "gpa": gpa,
            "major": major,
            "race": race,
            "gmat": gmat,
            "work_exp": work_exp,
            "work_industry": work_industry
        }

        X = dv.transform([client_data])
        y_pred = model.predict_proba(X)[0, 1]
        admit = y_pred >= 0.5

        return f"Admission Probability: {y_pred:.2f}, Admission Decision: {'Admit' if admit else 'Not admit'}"
    except Exception as e:
        return f"Error: {str(e)}"


def create_gradio_interface():
    return gr.Interface(
        fn=process_form_data,
        inputs=[
            gr.Dropdown(choices=["Male", "Female"], label="Gender"),
            gr.Checkbox(label="Is an international student?"),
            gr.Number(label="GPA Score", maximum=4, minimum=0, step=0.1),
            gr.Dropdown(choices=major, label="Major"),
            gr.Dropdown(choices=races, label="Race"),
            gr.Number(label="GMAT Score", minimum=205, maximum=805, value=205),
            gr.Number(label="Work experience", minimum=0.0),
            gr.Dropdown(choices=work_industries, label="Work Industry")
        ],
        outputs="text",
        title="Applicant Profile Information",
        description="Enter your information below."
    )


if __name__ == "__main__":
    interface = create_gradio_interface()
    interface.launch(server_name="0.0.0.0", server_port=7860, share=True)
