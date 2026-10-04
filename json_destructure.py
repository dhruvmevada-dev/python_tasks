import json

data = json.loads("""
{
  "company": "TechCorp",
  "employees": [
    {"id": 1, "name": "Alice", "skills": ["Python", "Flutter"],
     "address": {"city": "Ahmedabad", "pin": "380001"}},
    {"id": 2, "name": "Bob", "skills": ["Unity", "C#"],
     "address": {"city": "Mumbai", "pin": "400001"}}
  ],
  "departments": ["Engineering", "Design"],
  "meta": {"founded": 2015, "active": true}
}
""")


def destructure(obj, path=""):
    """Recursively walk a mix of dicts/lists and print every value with its path."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            destructure(value, f"{path}.{key}" if path else key)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            destructure(item, f"{path}[{i}]")
    else:
        print(f"{path} = {obj!r}")


def flatten(obj, path="", out=None):
    """Return the same information as a flat dict."""
    out = {} if out is None else out
    if isinstance(obj, dict):
        for key, value in obj.items():
            flatten(value, f"{path}.{key}" if path else key, out)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            flatten(item, f"{path}[{i}]", out)
    else:
        out[path] = obj
    return out


if __name__ == "__main__":
    # 1. Direct destructuring (unpacking) of known structure
    company = data["company"]
    first, second = data["employees"]
    dept1, dept2 = data["departments"]
    founded = data["meta"]["founded"]
    city = first["address"]["city"]
    skill1, skill2 = first["skills"]

    print("Company:", company)
    print("First employee:", first["name"], "| city:", city, "| skills:", skill1, skill2)
    print("Second employee:", second["name"])
    print("Departments:", dept1, dept2)
    print("Founded:", founded)

    # 2. Generic recursive destructuring (works for any structure)
    print("\n--- All values with paths ---")
    destructure(data)

    print("\n--- Flattened dict ---")
    print(json.dumps(flatten(data), indent=2))
