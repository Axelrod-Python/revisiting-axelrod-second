import axelrod as axl
assert axl.__version__ == "3.3.0"

# Low reps because this tournament is huge
repetitions = 200

pbs_files = []

for seed in range(20):  # Total of 4000 repetitions
    pbs_files.append("full_{seed:02d}.pbs".format(seed=seed))

    pbs_file ="""
#!/bin/bash
#PBS -q workq
#PBS -N full{seed}
#PBS -P PR350
#PBS -o full{seed}-out.txt
#PBS -e full{seed}-err.txt
#PBS -l select=1:ncpus=16:mpiprocs=16
#PBS -l place=scatter:excl
#PBS -l walltime=70:00:00

export MPLBACKEND="agg"
export LD_LIBRARY_PATH=$$LD_LIBRARY_PATH:/home/smavak/TourExec/bin
# Run std
cd /scratch/smavak/revisiting-axelrod-second/src
    """.format(seed=seed)

    pbs_file += """
/home/smavak/anaconda3/envs/rrr-axl/bin/python run_full_tournament.py {seed} {repetitions}
""".format(seed=seed,
           repetitions=repetitions)

    with open(pbs_files[-1], "w") as f:
        f.write(pbs_file)

with open("submit_all.sh", "w") as f:
    for pbs_file in pbs_files:
        f.write("qsub {}\n".format(pbs_file))
