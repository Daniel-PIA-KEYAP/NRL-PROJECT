# NRL Try Scorer Predictor Documentation

## Features
- Predicts try scorers for NRL matches based on historical data.
- User-friendly interface for data input and output.
- Supports various NRL season data.

## Installation
To install the NRL Try Scorer Predictor, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Daniel-PIA-KEYAP/NRL-PROJECT.git
cd NRL-PROJECT
pip install -r requirements.txt
```

## Usage
After installation, you can run the predictor as follows:

```bash
python predictor.py --input <path_to_input_file> --output <path_to_output_file>
```

## API Endpoints
- **POST /predict**: Accepts match data and returns predicted try scorers.
- **GET /history**: Fetches historical prediction data.

### Request Example:
```json
{
    "match_id": "123",
    "team_a": "Team A",
    "team_b": "Team B",
    "date": "2026-03-20"
}
```

### Response Example:
```json
{
    "predicted_scorers": ["Player 1", "Player 2"],
    "confidence": 0.85
}
```

## Examples
### Example Usage:
```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"match_id": "123", "team_a": "Team A", "team_b": "Team B", "date": "2026-03-20"}'
```

### Expected Response:
```json
{
    "predicted_scorers": ["Player 1", "Player 2"],
    "confidence": 0.85
}
```

## Troubleshooting
- **Issue:** Unable to run the predictor.
  **Solution:** Ensure all dependencies are installed correctly and Python is in your PATH.

- **Issue:** API not responding.
  **Solution:** Check if the server is running and accessible.

For further assistance, please open an issue in the GitHub repository or contact the maintainers.