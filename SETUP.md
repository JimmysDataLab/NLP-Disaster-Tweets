### Steps done
1. Add .gitignore
	```bash
 	cd <repo>
 	touch .gitignore
 	echo ".ipynb_checkpoints/" >> .gitignore # Ignore this directory 
	echo ".DS_Store" >> .gitignore # Ignore this file
    echo ".data >> .gitignore # Do not track raw data
	```
2. Install ipykernel
	```bash
	pip install ipykernel
	```
3. Create new kernel
	```bash
	python3 -m ipykernel install --user --name=<kernelname>

 4.

