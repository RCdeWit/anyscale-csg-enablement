# anyscale-csg-enablement
Toybox repository for Ray and Anyscale learning sessions

## How to run

### Set up

1. Create a new venv: `python3 -m venv .venv`
2. Install uv: `pip install uv`
3. Sync the environment: `uv sync`

### Launch cluster

1. Authenticate AWS
2. Launch the cluster on EC2 with `ray up cluster.yaml`
3. Open up port `6379` on the head node and allow TCP traffic
3. Copy over the head node IP and port forward the Ray dashboard: `ray dashboard cluster.yaml`. Keep this terminal running.
4. You can now access the Ray dashboard on `http://localhost:8265`
5. `export RAY_ADDRESS="http://127.0.0.1:8265"`
6. Launch the job: `ray job submit --working-dir . -- python main.py`
