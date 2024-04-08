# Random Test Data Generator

This project is a simple Python application that generates random test data. The data can be of three types: numeric, string, and datetime. The quantity of data to be generated can be specified by the user.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- pip

### Installing

Clone the repository to your local machine:

```bash
git clone https://github.com/TurgayArif/random_test_data_generator.git
```

Navigate to the project directory:

```bash
cd random_test_data_generator
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the tests

The project includes a suite of unit tests that can be run using Python's built-in `unittest` module. To run the tests, navigate to the project directory and run the following command:

```bash
python -m unittest tests/main.py
```

## Usage

The `generate_test_data` function in `random_test_data_generator.py` can be used to generate random test data. The function takes two parameters: `data_type` and `quantity`.

- `data_type`: The type of data to generate. Can be 'numeric', 'string', or 'datetime'.
- `quantity`: The number of data items to generate.
- `format`: The output format of the data.

Here is an example of how to use the function:

```python
from random_test_data_generator import generate_test_data

# Generate 10 random integers
data = generate_test_data('numeric', 10)
```

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- Python
- unittest
- random
- datetime
