#!/bin/bash
random_pair() {
    local fileA="$1"
    local fileB="$2"

    # Verify files exist
    [[ -f "$fileA" ]] || {
        echo "Error: $fileA not found." >&2
        return 1
    }

    [[ -f "$fileB" ]] || {
        echo "Error: $fileB not found." >&2
        return 1
    }

    # Count lines
    local linesA linesB
    linesA=$(wc -l < "$fileA")
    linesB=$(wc -l < "$fileB")

    # Ensure equal length
    if [[ "$linesA" -ne "$linesB" ]]; then
        echo "Error: Files have different numbers of lines." >&2
        return 1
    fi

    # Generate random line (1..N)
    local line=$(( RANDOM % linesA + 1 ))

    # Extract matching entries
    local valueA valueB

    valueA=$(sed -n "${line}p" "$fileA")
    valueB=$(sed -n "${line}p" "$fileB")

    # Output desired format
    printf "'%s:%s'\n" "$valueA" "$valueB"
}

random_pair A.txt B.txt
