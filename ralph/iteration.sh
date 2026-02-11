#!/bin/bash

APPLICATION_DIR=$(pwd)
ITERATION=$1
PROMPT_FILE="$APPLICATION_DIR/../ralph/PROMPT.md"
git config --global user.email "$GIT_USER_EMAIL"
git config --global user.name "$GIT_USER_NAME"
git config --global --add safe.directory /workspace/application
git config --global --add safe.directory /workspace

# 1. DETERMINE ITERATION NUMBER
if [ -z "$ITERATION" ]; then
    LAST_COMMIT=$(git log --all --grep="Ralph Wiggum Iteration" --format="%s" -n 1 2>/dev/null)
    
    if [ -n "$LAST_COMMIT" ]; then
        LAST_ITERATION=$(echo "$LAST_COMMIT" | grep -oE '[0-9]+$')
        if [ -n "$LAST_ITERATION" ]; then
            ITERATION=$((LAST_ITERATION + 1))
            echo "Found last iteration: $LAST_ITERATION, using iteration: $ITERATION"
        else
            ITERATION=1
            echo "No valid iteration number found in git history, starting from: $ITERATION"
        fi
    else
        ITERATION=1
        echo "No previous Ralph Wiggum commits found, starting from: $ITERATION"
    fi
else
    echo "Using provided iteration: $ITERATION"
fi

# 2. PROMPT CHECK
if [ ! -n "${PROMPT_FILE+x}" ]; then
    echo "Error: $PROMPT_FILE not found at $PROMPT_FILE"
    exit 1
fi

# 3. CORE WORK
if [ -n "${BOBSHELL_API_KEY+x}" ]; then
    cat "$PROMPT_FILE" | bob \
        --auth-method api-key \
        --allowed-tools read_file,write_todos,write_to_file,run_shell_command \
        --output-format=stream-json
else
    cat "$PROMPT_FILE" | gemini \
        --yolo
        --output-format=stream-json
fi

# 4. COMMIT
git config --global user.email "$GIT_USER_EMAIL"
git config --global user.name "$GIT_USER_NAME"
git config --global --add safe.directory /workspace/application
git config --global --add safe.directory /workspace
git add .
git commit -m "Ralph Wiggum Iteration $ITERATION" --allow-empty