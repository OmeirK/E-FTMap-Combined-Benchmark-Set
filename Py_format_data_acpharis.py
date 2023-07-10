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
   db_dirs = glob.glob(f'{args.orig_db}/set*/')
   for sd in db_dirs:
      #print(sd)
      set_name = os.path.basename(sd[:-1]).split('_')[1]
      #new_dir = f'{args.prefix}_{os.path.basename(sd[:-1])}'
      new_dir = f'{args.prefix}_{set_name}'
      #print(new_dir)
      apo_pdb = glob.glob(f'{sd}/*_base.pdb')[0]
      
      apo_data = os.path.basename(apo_pdb).split('_')
      if apo_data[0] == 'base':
         print(f'{sd} has no apo structure! Skipping it.')
         continue

      frag_pdb = glob.glob(f'{sd}/*_fragbound.pdb')[0]
      lead_pdb = glob.glob(f'{sd}/*_maxlig.pdb')[0]
      frag_sdf = glob.glob(f'{sd}/*_frag.sdf')[0]
      lead_sdf = glob.glob(f'{sd}/*_maxlig.sdf')[0]


      os.mkdir(f'{new_dir}')
      os.system(f'cp {apo_pdb} {new_dir}/apo.pdb')
      os.system(f'cp {frag_pdb} {new_dir}/frag_bound.pdb')
      os.system(f'cp {lead_pdb} {new_dir}/lead_bound.pdb')
      os.system(f'cp {frag_sdf} {new_dir}/frag_1.sdf')
      os.system(f'cp {lead_sdf} {new_dir}/lead.sdf')







if __name__=='__main__':
   main()
