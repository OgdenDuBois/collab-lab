"""Anonymous project-id generator - OgdenDuBois style.
Ogden has no bio and only empty project-xxxx repos,
so this makes a new one: project-<8 random chars>,
and scaffolds an empty folder with just a README.
Usage: python persona_ogden_project_id.py
"""
import os, random, string

def new_id():
    return "project-" + "".join(random.choices(string.ascii_lowercase + string.digits, k=8))

def main():
    pid = new_id()
    os.makedirs(pid, exist_ok=True)
    with open(os.path.join(pid, "README.md"), "w") as f:
        f.write(f"# {pid}\n")
    print(pid)

if __name__ == "__main__":
    main()
