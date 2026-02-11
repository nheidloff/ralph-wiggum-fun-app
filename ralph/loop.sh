#!/bin/bash

MAX_ITERATIONS=5
ITERATION=0
APPLICATION_DIR=$(pwd)
PLAN_FILE="$APPLICATION_DIR/ralph/IMPLEMENTATION_PLAN.md"

echo "--- Starting Ralph Wiggum Loop ---"

while true; do
    if [ -f "$PLAN_FILE" ]; then
        if ! grep -q "\- \[ \]" "$PLAN_FILE"; then
            echo "✅ Success! No unchecked tasks found in $PLAN_FILE."
            echo "Ralph says: 'I finished helping!'"
            break
        fi
    fi

    # 2. MAX ITERATION CHECK
    if [ $MAX_ITERATIONS -gt 0 ] && [ $ITERATION -ge $MAX_ITERATIONS ]; then
        echo "🛑 Reached max iterations: $MAX_ITERATIONS"
        break
    fi

    echo "--- Running Iteration $ITERATION ---"

    # 3. CALL THE ITERATION SCRIPT
    /workspace/ralph/iteration.sh "$ITERATION"

    ITERATION=$((ITERATION + 1))
done