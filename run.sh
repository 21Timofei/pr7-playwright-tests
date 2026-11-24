#!/bin/sh
set -eu
cd "$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"

# Используем уже доступный Node.js 24 из окружения Codex, если он есть.
# На другом компьютере достаточно установленного поддерживаемого Node.js.
playwright_node_dir="${PLAYWRIGHT_NODE_DIR:-$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin}"
if [ -x "$playwright_node_dir/node" ]; then
  PATH="$playwright_node_dir:$PATH"
  export PATH
fi

export PLAYWRIGHT_BROWSERS_PATH="$PWD/.browsers"
export npm_config_cache="$PWD/.npm-cache"
if [ "$#" -eq 0 ]; then
  set -- test
fi
exec npm "$@"
