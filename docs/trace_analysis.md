| Scenario                  | Temp | Top-P | Prompt <br/>tokens | Completion<br/>tokens  | Latency (ms/s) | Observation |
|---------------------------|------|-------|--------------------|------------------------|----------------|-------------|
| 1.Concise FAQ             | 0.1  | 0.9   | 159                | 905                    | 2s             |             |
| 2. History Analysis       | 0.1  | 0.9   | 922                | 1431                   | 3.3s           |             |
| 3A. Creative (Top-P 0.1)  | 1.0  | 0.1   | 2212               | 73                     | 534ms          |             |
| 3B. Creative (Top-P 0.95) | 1.0  | 0.95  | 2258               | 69                     | 394ms          |             |
| 4. Hallucination Pro      | 0.7  | 0.9   | 2557               | 133                    | 718ms          |             |
| 5. Hallucination Pro Max  | 1.8  | 0.9   | 2583               | 61                     | 5.4s           |             |
