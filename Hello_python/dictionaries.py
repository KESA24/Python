# Helps us store "key value" pairs.

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    0: "Nekesa",
    1: "Drileba",
}

# Access the entries
print(monthConversions["Nov"])
print(monthConversions.get("Jun"))

print(monthConversions.get("Luv", "Not a valid key"))

print(monthConversions.get(1))
