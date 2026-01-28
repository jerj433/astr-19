import numpy as np


def main():
    xvals = np.linspace(0.0, 2.0, 1000)
    print("x\t\tsin(x)")
    for x in xvals:
        print(f"{x:.6f}\t{np.sin(x):.6f}")

if __name__ == "__main__":
    main()
