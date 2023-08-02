import json
comparison_string = '2022-02-11'
# Replace 'file_name.json' with the path to your JSON file
with open('metadata_aggregate.json', 'r') as file:
    data = json.load(file)

# Iterate over the items in the JSON data
for item in data:
    print(item)


ai_tooling_values = data.get("AI_Tooling.md")
if ai_tooling_values is not None:
    #print(ai_tooling_values)
    date_of_evaluation = ai_tooling_values.get("Date of Evaluation")
    if date_of_evaluation is not None:
        print(f"Date of Evaluation for AI_Tooling.md: {date_of_evaluation}")
        # Compare the value to another string
        if date_of_evaluation == comparison_string:
            print("The Date of Evaluation matches the comparison string.")
        else:
            print("The Date of Evaluation does not match the comparison string.")
    else:
        print("Key 'Date of Evaluation' not found in the AI_Tooling.md object.")
else:
    print("Key 'AI_Tooling.md' not found in the JSON data.")
