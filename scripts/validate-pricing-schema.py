"""Check the repository's local pricing schema and documented example."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator

root = Path(__file__).resolve().parents[1]
schema = json.loads((root / "schemas/custom-pricing.schema.json").read_text())
example = json.loads((root / "examples/custom-pricing.json").read_text())
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema)
validator.validate(example)
for invalid in (
    {"provider_overrides": [{"provider_id": "unknown", "model_id": "m", "pricing": {"input_cost_per_token": 1}}]},
    {"provider_overrides": [{"provider_id": "p", "model_id": "m", "pricing": {"input_cost_per_token": None}}]},
    {"provider_overrides": [{"provider_id": "p", "model_id": "m", "pricing": {"input_cost_per_tokne": 1}}]},
):
    assert not validator.is_valid(invalid), invalid
print("Pricing schema and examples are valid; invalid examples rejected.")
