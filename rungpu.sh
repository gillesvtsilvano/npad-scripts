#!/bin/bash

srun -N1 -n1 -p gpu --exclusive --time=4-00:00 --pty bash -i
