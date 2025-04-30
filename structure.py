import os

base_dir = "ISLP-Labs"

chapters = {
    1: "Introduction",
    2: "Statistical_Learning",
    3: "Linear_Regression",
    4: "Classification",
    5: "Resampling_Methods",
    6: "Linear_Model_Selection_Regularization",
    7: "Moving_Beyond_Linearity",
    8: "Tree_Based_Methods",
    9: "Support_Vector_Machines",
    10: "Deep_Learning",
    11: "Survival_Analysis",
    12: "Unsupervised_Learning",
    13: "Multiple_Testing"
}

if __name__ == "__main__":

    # Create base directory
    os.makedirs(base_dir, exist_ok=True)

    # Create chapter folders with README.md and lab.ipynb
    for num, name in chapters.items():
        folder = f"Chapter_{num:02d}_{name}"
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

        # Write chapter README
        with open(os.path.join(folder_path, "README.md"), "w") as f:
            f.write(f"# Chapter {num}: {name.replace('_', ' ')}\n\n"
                    f"Contains the Python lab notebook and brief description for Chapter {num}.\n")

        # Create empty lab notebook file
        open(os.path.join(folder_path, "lab.ipynb"), "w").close()

    # Create datasets folder
    datasets_path = os.path.join(base_dir, "datasets")
    os.makedirs(datasets_path, exist_ok=True)

    # Write main project README
    with open(os.path.join(base_dir, "README.md"), "w") as f:
        f.write("# ISLP Labs in Python 🧠\n\n"
                "This repository contains lab implementations for all chapters of the book\n"
                "**An Introduction to Statistical Learning with Applications in Python (ISLP)**.\n\n"
                "## Structure\n"
                "- 13 Chapters with individual labs\n"
                "- Each chapter includes a Jupyter notebook and chapter-specific README\n"
                "- `datasets/` folder contains all required CSV data\n\n"
                "## Resources\n"
                "- 📘 Book: https://doi.org/10.1007/978-3-031-38747-0\n"
                "- 🔗 Datasets: https://www.statlearning.com\n"
                "- 🐍 ISLP Python Package: https://github.com/ISLPed\n")

    print(f"✅ Structure created at: {base_dir}")