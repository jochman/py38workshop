"""
For use as a Demisto automation (Script).

Use Walrus assignment, Positional arguments only and debugging statement in this script. 
"""
forms = [
    {"severity": 6, "factor": 1, "active": 2},
    {"severity": 6, "factor": 2, "active": 4},
    {"severity": 6, "factor": 3, "active": 0},
]
def calc(severity, factor, divider):
    return severity * (factor / divider)

readable = ""
for form in forms:
    divider = form["active"]
    if divider == 0:
        divider = 1
    severity = form["severity"]
    if severity < 7:
        severity = 5
    factor = form["factor"]
    calculated_severity = calc(severity, divider=divider, factor=factor)
    readable += f"calculated_severity={calculated_severity}\n"

return_outputs(readable)
