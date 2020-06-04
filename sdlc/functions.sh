#!/bin/bash
set -eEu
set -o pipefail

################################################################################
# Be kind to new Python users.
################################################################################

# to trap ERR requires BASH, not POSIX shell
# https://www.gnu.org/software/bash/manual/html_node/Bash-Variables.html
trap 'err $? ${LINENO} "${BASH_SOURCE}" "${BASH_COMMAND}"' ERR
trap 'finish $?' EXIT

finish() {
    echo
    if [[ "$1" = "0" ]]; then
        echo "[PASS] $0 OK"
    else
        echo "[FAIL] See errors above for $0"
    fi
    echo
}

err() {
    echo
    echo
    echo "[ERROR] caught error $1 on line $2 of $3: $4"
    exit "$1"
}

if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
    PYTHON_MAJOR_VER="$(python -c "import sys; print(sys.version_info[0])")"
    if [[ "${PYTHON_MAJOR_VER}" -ne "3" ]]; then
        echo "[FAIL] Could not find python version 3+"
        exit 1
    fi
fi

PYTHON_USER_BASE="$("${PYTHON}" -c "import site; print(site.USER_BASE)")"
if ! grep "${PYTHON_USER_BASE}/bin" <(printenv PATH) &>/dev/null; then
    echo "[INFO] Adding Python user path to PATH from $0"
    export PATH="${PATH}:${PYTHON_USER_BASE}/bin"
fi

if command -v pip3 &>/dev/null; then
    PIP=pip3
else
    PIP=pip
fi
export PIP
