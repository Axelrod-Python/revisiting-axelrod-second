import axelrod as axl
import axelrod_fortran as axlf

assert axl.__version__ == "3.3.0"
assert axlf.__version__ == "0.3.1"

repetitions = 500

implemented_strategies = [axlf.characteristics[name]['axelrod-python_class']
                          for name in axlf.second_tournament_strategies]

pbs_files = []
for strategy_index, strategy in enumerate(axl.strategies):

    if strategy not in implemented_strategies:

        pbs_files.append("{index:03d}.pbs".format(index=strategy_index))

        pbs_file ="""
#!/bin/bash
#PBS -q workq
#PBS -N xtra{index}
#PBS -P PR350
#PBS -o xtra{index}-out.txt
#PBS -e xtra{index}-err.txt
#PBS -l select=1:ncpus=16:mpiprocs=16
#PBS -l place=scatter:excl
#PBS -l walltime=70:00:00

export MPLBACKEND="agg"
export LD_LIBRARY_PATH=$$LD_LIBRARY_PATH:/home/smavak/TourExec/bin
# Run std
cd /scratch/smavak/revisiting-axelrod-second/src
        """.format(index=strategy_index)

        for seed in range(5):
            pbs_file += """
/home/smavak/anaconda3/envs/rrr-axl/bin/python run_original_tournament_with_extra_strategy.py {seed} {repetitions} {strategy_index}
        """.format(seed=seed,
                   repetitions=repetitions,
                   strategy_index=strategy_index)

        with open(pbs_files[-1], "w") as f:
            f.write(pbs_file)

with open("submit_all.sh", "w") as f:
    for pbs_file in pbs_files:
        f.write("qsub {}\n".format(pbs_file))
