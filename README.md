# Retail Data ETL Pipeline

An educational ETL (Extract, Transform, Load) pipeline designed to process, clean, and aggregate retail sales data. This project demonstrates modular Python architecture, defensive data cleaning with Pandas, and automated testing with `pytest`.

## Architecture & Project Structure

The project is organized into distinct modules to separate orchestration from business logic, adhering to the principle of **Separation of Concerns**.

* `main.py`: The entry point that orchestrates the workflow.
* `src/business.py`: The "Brain" of the project. Contains pure functions for data transformation and aggregation.
* `src/etl.py`: Handles I/O operations (reading from Parquet and CSV and writing to disk).
* `data/`: Organized into `raw/` (immutable source data) and `processed/` (pipeline artifacts).
* `tests/`: A comprehensive test suite using **Pytest Fixtures** for efficient, DRY unit and integration testing.



## Key Data Engineering Patterns

### 1. Defensive Data Transformation
The pipeline handles real-world data issues commonly encountered in retail datasets:
* **Forward Filling**: Handles missing records across multiple columns by propagating the last valid observation forward.
* **Type Casting**: Safely converts string-based dates into `datetime` objects for time-series extraction.

### 2. Validated Aggregation
To prepare data for downstream financial reporting, the pipeline:
* Filters out noise by retaining only records with `Weekly_Sales` ≥ $10,000.
* Groups by `Month` and calculates the mean sales.
* Rounds currency values to two decimal places for reporting precision.

### 3. Automated Quality Assurance
The project implements a two-tier testing strategy:
* **Unit Tests**: Verify the logic of `transform` and `aggregate` functions using isolated mock DataFrames.
* **Integration Tests**: Verify that the `load` phase produces files with the correct schema, file paths, and data types (e.g., ensuring `Month` remains an integer after CSV I/O).



## Quickstart (macOS / zsh)

1. **Environment Setup**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Execute the Pipeline**:
    ```bash
    python main.py
    ```

3. **Run Tests**:
    ```bash
    pytest
    ```



## Data Contract

| Table | Source | Primary Key / Join Key |
| :--- | :--- | :--- |
| **Raw Sales** | `grocery_sales.csv` | `index` |
| **Extra Features** | `extra_data.parquet` | `index` |

**Final Output (`agg_data.csv`):**
* **Month**: Integer (1-12)
* **Weekly_Sales**: Float (Rounded to 2 decimals)

## Engineering Notes
* **Performance**: Used Pytest fixtures with a tiered dependency chain to ensure transformation logic is only executed once per test session.
* **Maintainability**: Utilized `if __name__ == "__main__":` blocks to ensure the pipeline is safely importable for testing without accidental execution.

## Future Roadmap
- [ ] **CI/CD Integration**: Implement GitHub Actions to run the test suite automatically on every push.
- [ ] **Logging**: Replace print statements with the `logging` library to track pipeline telemetry.
- [ ] **Containerization**: Wrap the pipeline in a Docker container for environment parity.

## Author

Ivan Espinosa — igeg1
