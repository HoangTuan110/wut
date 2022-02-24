# TOML

TOML aims to be a minimal configuration file format that's easy to read due to obvious semantics.
TOML is designed to map unambiguously to a hash table.
TOML should be easy to parse into data structures in a wide variety of languages.

## Example:
```toml
# This is a TOML document.

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00 # First class dates

[database]
server = "192.168.1.1"
ports = [ 8000, 8001, 8002 ]
connection_max = 5000
enabled = true
```
