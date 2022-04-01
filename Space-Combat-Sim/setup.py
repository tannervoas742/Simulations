from setuptools import setup

setup(
    name="SpaceSim",
    packages=[
        "SpaceSim",
        "SpaceSim.Ammunition",
        "SpaceSim.Components",
        "SpaceSim.Entities",
        "SpaceSim.Simulation",
    ],
    package_data={
#        "SpaceSim.Ammunition": [
#        ],
#        "SpaceSim.Components": [
#        ],
#        "SpaceSim.Entities": [
#        ],
    },
    install_requires=[
        "cupy-cuda115",
    ],
    author="Tanner Voas",
    version="0.1.1"
)
