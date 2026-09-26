#!/bin/bash
set -e

# Start the Phoenix collector & UI in the background on port 6006.
python -m phoenix.server.main serve &

# Give Phoenix a moment to bind its HTTP listener before the app starts sending traces.
sleep 3

# Run Streamlit in the foreground so it becomes the container's main process.
exec streamlit run src/app.py \
    --server.port=8501 \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --browser.gatherUsageStats=false