# Mypythoncodes
My Python Scripts

# Steps to Create Virtual Environment

1. Install *virtualenv*
   ```bash
        pip install virtualenv
   ```
2. create a Virtual Environment
   ```bash
        virtualenv $envname
   ```
3. Activate the Environment
   ```bash
        #Windows 
        virtualFolder\Scripts\activate
        #Linunx & Mac
        source virtualFolder/bin/activate
4.  Deactivate the Environment
   ```bash
                deactivate
   ```

# Check the python version 
   ```bash
                which python
   ```

# pip freeze dependency
  ```bash
        #Freeze
       pip freeze > reqirements.txt
       #install from reqirements.txt
        pip install -r reqirements.txt 
  ```
