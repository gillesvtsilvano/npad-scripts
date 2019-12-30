#!/bin/bash 
#SBATCH --nodes=1
##SBATCH --partition=gpu
##SBATCH --nodelist=service10
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10      #Quantidade de núcleos
##SBATCH --exclusive            #Se cpus-per-task=32, deixe apenas 1 # no início dessa linha
#SBATCH --time=4-00:00          #Tempo máximo do job no formato DIAS-HORAS:MINUTOS
#SBATCH --hint=compute_bound
#SBATCH --mail-type=all
#SBATCH --mail-user=gillesvtsilvano@gmail.com

#module load softwares/python/3.6-anaconda-5.0.1  #Carregue o seu módulo python preferido
#module load softwares/python/3.6.1-gnu-4.8  #Carregue o seu módulo python preferido

#O ideal é utilizar um python versão anaconda
#Para ver os módulos python existentes, use: module av

## Parametros iniciais
XDG_RUNTIME_DIR=""
ipnport=$(shuf -i10000-12000 -n1)
ipnip=$(hostname -i)

## Imprime na saída slurm-{jobid}.out
echo -e "
    Copy/Paste this in your local terminal to ssh tunnel with remote
    Copie e cole no terminal local da sua máquina o comando abaixo
    -----------------------------------------------------------------
    ssh -N -L $ipnport:$ipnip:$ipnport -p4422 $USER@sc.npad.imd.ufrn.br
    -----------------------------------------------------------------
    "

## start an ipcluster instance and launch jupyter server
## Inicia servidor Jupyter
jupyter-lab --no-browser --port=$ipnport --ip=$ipnip 
