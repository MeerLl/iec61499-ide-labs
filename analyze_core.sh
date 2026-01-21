#!/bin/bash
echo "Поиск core-файлов:"
find . -name "core*" -type f 2>/dev/null

echo "Введите путь к core-файлу:"
read core_file

if [ -f "$core_file" ]; then
    gdb python "$core_file" -ex "bt" -ex "info registers" -ex quit
    strings "$core_file" | tail -20
else
    echo "Файл не найден"
fi