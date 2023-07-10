import os
import copy
import glob
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--orig_db', '-d', help='A path to the original processed database')
parser.add_argument('--prefix', '-p', help='A prefix to add to the new directories')

args = parser.parse_args()

def main():
   loglines = []
   db_dirs = glob.glob(f'{args.orig_db}/*/')
   for sd in db_dirs:
      #print(sd)
      set_name = os.path.basename(sd[:-1])
      new_dir = f'{args.prefix}_{set_name}'
      print(new_dir)

      apo_pdb = glob.glob(f'{sd}/apo.pdb')[0]
      frag_pdb = glob.glob(f'{sd}/fragment.pdb')[0]
      lead_pdb = glob.glob(f'{sd}/lead.pdb')[0]
      frag_sdf = glob.glob(f'{sd}/frag*.sdf')
      lead_sdf = glob.glob(f'{sd}/maxlig.sdf')[0]

      os.mkdir(f'{new_dir}')
      os.system(f'cp {apo_pdb} {new_dir}/apo.pdb')
      os.system(f'cp {frag_pdb} {new_dir}/frag_bound.pdb')
      os.system(f'cp {lead_pdb} {new_dir}/lead_bound.pdb')
      i = 1
      for frag in frag_sdf:
         os.system(f'cp {frag} {new_dir}/frag_{i}.sdf')
         i += 1
         


      os.system(f'cp {lead_sdf} {new_dir}/lead.sdf')







if __name__=='__main__':
   main()
