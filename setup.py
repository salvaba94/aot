import setuptools
import os.path
import glob

metadata = {
    "__name_program__": "deaotpy",
    "__name_module__": "aot",
    "__version__": "1.0.0",
    "__url__": "https://github.com/yoxu515/aot-benchmark",
    "__description__": "Decoupling Features in Hierarchical Propagation for Video Object Segmentation.",
    "__python_requires__": ">=3.10",
    "__license__": "BSD 3-Clause License",
    "__classifiers__": [
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: BSD 3-Clause License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    "__keywords__": "machine-learning, deep-learning, pytorch, "
                    "vision, object segmentation, video"
}
setup_dir = os.path.dirname(__file__)


if __name__ == "__main__":
    with open(os.path.join(metadata["__name_module__"], "README.md"), "r") as f:
        long_description = f.read()

    with open(os.path.join(metadata["__name_module__"], "LICENSE"), "r", encoding="utf-8") as f:
        license = f.read()

    setuptools.setup(
        name=metadata["__name_program__"],
        version=metadata["__version__"],
        description=metadata["__description__"],
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=metadata["__url__"],
        license=license,
        python_requires=metadata["__python_requires__"],
        packages=setuptools.find_packages(),
        include_package_data=True,
        classifiers = metadata["__classifiers__"],
        keywords=metadata["__keywords__"]
    )