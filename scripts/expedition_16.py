import configparser, sys
def load_config(path):
    cfg = configparser.ConfigParser()
    cfg.read(path)
    return {s: dict(cfg[s]) for s in cfg.sections()}
if __name__ == "__main__":
    print(load_config(sys.argv[1]))
