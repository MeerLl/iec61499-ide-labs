#!/bin/bash
ulimit -c unlimited
mkdir -p ~/cores
echo "core_pattern: ~/cores/core.%e.%p.%t"
sudo sysctl -w kernel.core_pattern=~/cores/core.%e.%p.%t
echo "Готово! ulimit -c: $(ulimit -c)"