# my_project



- [my_project](#my_project)
  - [Getting Started](#getting-started)

## Getting Started

1. Clone project to local folder

2. Configure conda environment:

   ```sh
   # create new environment
   mamba env create --name  -f ./environment-dev.yaml
   python -m pip install --no-deps -r requirements.txt
   python -m pip install --no-deps -r ds_utils-requirements.txt
   # may require Azure Token when prompted for password

   # or update existing environment
   conda activate 
   mamba env update --name  -f ./environment.yaml
   ```

