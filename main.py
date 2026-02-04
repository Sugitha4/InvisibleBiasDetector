import os
from train_ai import train_model
from bias_detector import bias_score

print("Current working directory:", os.getcwd())

model, vectorizer = train_model()

total_bias = []
shortlisted_bias = []
report_lines = []

for file in os.listdir("resumes"):
    with open(os.path.join("resumes", file), "r") as f:
        text = f.read()

    vector = vectorizer.transform([text])
    decision = model.predict(vector)[0]

    bias = bias_score(text)
    total_bias.append(bias)

    status = "Shortlisted" if decision == 1 else "Rejected"

    if decision == 1:
        shortlisted_bias.append(bias)

    report_lines.append(
        f"{file} | {status} | Bias Detected: {bias}%"
    )

overall_bias = round(sum(total_bias) / len(total_bias), 2)
shortlist_bias = round(
    sum(shortlisted_bias) / len(shortlisted_bias), 2
) if shortlisted_bias else 0

# 🔥 FORCE OUTPUT DIRECTORY
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "bias_report.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("=== INVISIBLE BIAS AUDIT REPORT ===\n\n")
    for line in report_lines:
        f.write(line + "\n")

    f.write("\n--------------------------------\n")
    f.write(f"Overall AI Bias Percentage: {overall_bias}%\n")
    f.write(f"Shortlisted Candidates Bias Percentage: {shortlist_bias}%\n")

print("✅ Bias audit completed.")
print("📄 Report saved at:", os.path.abspath(output_path))