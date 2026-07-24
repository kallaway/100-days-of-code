
# Cria pastas dia-1 até dia-100
set -euo pipefail

START=1
END=100

for i in $(seq "$START" "$END"); do
	dir="dia-$i"
	if [ -d "$dir" ]; then
		printf "%s já existe\n" "$dir"
	else
		mkdir $dir
		printf "Criada: %s\n" "$dir"
	fi
done

exit 0
