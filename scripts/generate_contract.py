# scripts/generate_contract.py

# This is a simple script that reads the prompt template and fills in basic details.

template = """
Draft a Mutual Non-Disclosure Agreement (NDA) between {{PartyA}} and {{PartyB}} for a term of {{Term}} years. 
The agreement must be governed by the laws of {{Jurisdiction}}. 
Include clauses for confidentiality, permitted disclosures, term, return of information, and remedies.
"""

# Replace placeholders with actual values
final_prompt = (
    template
    .replace("{{PartyA}}", "Mob Makers Pvt. Ltd.")
    .replace("{{PartyB}}", "Cartel Clothing Co.")
    .replace("{{Term}}", "3")
    .replace("{{Jurisdiction}}", "Delhi, India")
)

# Print final version
print("📝 Final Contract Draft Prompt:\n")
print(final_prompt)
