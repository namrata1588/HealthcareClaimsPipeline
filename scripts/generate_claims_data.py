import pandas as pd
import random
from datetime import datetime, timedelta


# Generate random sample data
def generate_claims(num_records=100):
    claim_ids = [f"C{1000 + i}" for i in range(num_records)]
    patient_ids = [f"P{random.randint(1, 100):03}" for _ in range(num_records)]
    provider_ids = [f"D{random.randint(1, 50):03}" for _ in range(num_records)]
    claim_dates = [datetime(2024, 1, 1) + timedelta(days=random.randint(0, 300)) for _ in range(num_records)]
    claim_amounts = [round(random.uniform(500, 10000), 2) for _ in range(num_records)]
    diagnoses = random.choices(["Fever", "Diabetes", "Injury", "Allergy", "Flu"], k=num_records)
    procedures = random.choices(["PROC_210", "PROC_112", "PROC_307", "PROC_118"], k=num_records)
    statuses = random.choices(["Submitted", "Approved", "Denied"], k=num_records)
    approved_amounts = [amt if status == "Approved" else 0 for amt, status in zip(claim_amounts, statuses)]
    created_times = [dt.strftime("%Y-%m-%d %H:%M:%S") for dt in claim_dates]

    df = pd.DataFrame({
        "claim_id": claim_ids,
        "patient_id": patient_ids,
        "provider_id": provider_ids,
        "claim_date": [d.strftime("%Y-%m-%d") for d in claim_dates],
        "claim_amount": claim_amounts,
        "diagnosis": diagnoses,
        "procedure_code": procedures,
        "claim_status": statuses,
        "approved_amount": approved_amounts,
        "created_timestamp": created_times
    })

    return df



df = generate_claims(100)
df.to_csv(r"F:\HealthcareClaimsPipeline\data\raw\claims_raw.csv", index=False)
print("✅ claims_raw.csv created successfully!")
