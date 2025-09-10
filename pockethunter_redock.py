# Smina Docking Simulations
import subprocess
import os

pdb_ids = ["4A4L","2YAC","4J52","3FC2","2rku_A_prod_R3_fit_4180","2rku_A_prod_R3_fit_1752","2rku_A_prod_R3_fit_3147"]
current_directory = os.getcwd()
ligands_pdbqt_dir = f"{current_directory}/ligands_pdbqt"    

for pdb in pdb_ids:
    #all ligands under the ligands_pdbqt_dir

    for lig in os.listdir(ligands_pdbqt_dir):
        ligf = lig.split(".")[0] 
        print(pdb, ligf)

        #docking directory
        docking_dir = f"{current_directory}/docking2/{pdb}/{ligf}"
        
        # before running the smina docking command, check if out file already exists
        out_file = f"{docking_dir}/{pdb}_{ligf}_out.pdbqt"
        if os.path.exists(out_file):
            print(f"Output file {out_file} already exists. Skipping docking.")
            continue
        subprocess.call(f"smina --config {docking_dir}/config.txt --cpu 48", shell = True)