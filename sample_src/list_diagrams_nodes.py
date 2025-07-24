import pkgutil
import diagrams

def list_submodules(package):
    return [name for _, name, _ in pkgutil.iter_modules(package.__path__)]

def list_all_nodes():
    import diagrams
    modules = list_submodules(diagrams)
    print("Top-level modules under diagrams:")
    print(modules)
    print("\nListing submodules and nodes in 'diagrams' submodules:\n")

    for module_name in modules:
        try:
            mod = __import__(f"diagrams.{module_name}", fromlist=[''])
            submodules = list_submodules(mod)
            if submodules:
                print(f"{module_name}: {submodules}")
            else:
                # Try to list attributes (classes/icons) if no submodules
                attrs = [attr for attr in dir(mod) if not attr.startswith("_")]
                if attrs:
                    print(f"{module_name}: {attrs}")
        except Exception as e:
            print(f"Failed to load diagrams.{module_name}: {e}")

if __name__ == "__main__":
    list_all_nodes()
